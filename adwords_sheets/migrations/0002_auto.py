# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Campaign', fields ['name']
        db.create_index('adwords_sheets_campaign', ['name'])


    def backwards(self, orm):
        # Removing index on 'Campaign', fields ['name']
        db.delete_index('adwords_sheets_campaign', ['name'])


    models = {
        'adwords_sheets.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'adwords_sheets.dayentry': {
            'Meta': {'unique_together': "(('campaign', 'date'),)", 'object_name': 'DayEntry'},
            'avg_cpc': ('django.db.models.fields.FloatField', [], {}),
            'avg_position': ('django.db.models.fields.FloatField', [], {}),
            'budget': ('django.db.models.fields.FloatField', [], {}),
            'budget_status': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adwords_sheets.Campaign']"}),
            'campaign_state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'clicks': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'ctr': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impressions': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'labels': ('django.db.models.fields.TextField', [], {})
        },
        'adwords_sheets.upload': {
            'Meta': {'object_name': 'Upload'},
            'csv': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'dayentries': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['adwords_sheets.DayEntry']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loaded': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['adwords_sheets']