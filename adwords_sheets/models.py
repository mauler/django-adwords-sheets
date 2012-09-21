#!/usr/bin/env python
#-*- coding:utf-8 -*-

from decimal import Decimal

from django.db import models
from django.db.models.signals import post_save

import helpers

class Campaign(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.name


class Upload(models.Model):
    csv = models.FileField(upload_to=u"adwords-sheets/%Y/%m/%d/%H/%M")
    loaded = models.BooleanField()
    dayentries = models.ManyToManyField("DayEntry", blank=True)

    def __unicode__(self):
        return self.csv.name

    @staticmethod
    def post_save(sender, instance, created, raw,  *args, **kwargs):
        if created:
            instance.load_dayentries()
            instance.loaded = True
            instance.save()

    def load_dayentries(self):
        for row in helpers.csv2rows(self.csv):
            date = row['date']
            del row['date']
            campaign, created = \
                Campaign.objects.get_or_create(name=row['campaign'])
            del row['campaign']
            row['avg_cpc'] = Decimal(row['avg_cpc'].replace(",", "."))
            row['avg_position'] = Decimal(row['avg_position'].replace(",", "."))
            row['budget'] = Decimal(row['budget'].replace(",", "."))
            row['cost'] = Decimal(row['cost'].replace(",", "."))
            DayEntry.objects.get_or_create(
                date=date, campaign=campaign, defaults=row)


post_save.connect(Upload.post_save, sender=Upload)


class DayEntry(models.Model):
    date = models.DateField()
    campaign = models.ForeignKey("Campaign")
    campaign_state = models.CharField(max_length=100)
    budget = models.FloatField()
    budget_status = models.CharField(max_length=100)
    clicks = models.PositiveIntegerField()
    impressions = models.PositiveIntegerField()
    ctr = models.CharField(max_length=10)
    avg_cpc = models.FloatField()
    cost = models.FloatField()
    avg_position = models.FloatField()
    labels = models.TextField()

    class Meta:
        unique_together = ("campaign", "date", )

    def __unicode__(self):
        return u"%s %s" % (self.date, self.campaign)

