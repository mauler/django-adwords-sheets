#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

from django.core.files import File
from django.test.client import Client
from django.utils import unittest

from .models import Upload, DayEntry, Campaign
from .helpers import *


class CsvTest(unittest.TestCase):
    def test_csv2rows(self):
        app_path = os.path.dirname(os.path.abspath(__file__))
        csvfile = open(os.path.join(app_path, "sample.csv"))
        rows = csv2rows(csvfile)
        self.assertEqual(rows, [{'avg_cpc': '0,06', 'ctr': '0,70%', 'campaign': 'RMKT - TV', 'labels': ' --', 'budget': '5,00', 'budget_status': 'or\xc3\xa7amento de campanha limitado', 'avg_position': '1,96', 'cost': '4,86', 'date': '2012-08-07', 'impressions': '12334', 'clicks': '86', 'campaign_state': 'ativa'}, {'avg_cpc': '0,06', 'ctr': '1,52%', 'campaign': 'Hering e Dzarm - Vestidos', 'labels': ' --', 'budget': '10,00', 'budget_status': 'qualificada', 'avg_position': '5,21', 'cost': '10,39', 'date': '2012-08-13', 'impressions': '11456', 'clicks': '174', 'campaign_state': 'ativa'}])

        upload = Upload()
        upload.csv.save(
            "sample.csv",
            File(open(os.path.join(app_path, "sample.csv"))))
        upload.load_dayentries()
        self.assertEqual(DayEntry.objects.count(), 2)

