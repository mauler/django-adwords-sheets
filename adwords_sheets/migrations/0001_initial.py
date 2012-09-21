# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Campaign'
        db.create_table('adwords_sheets_campaign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('adwords_sheets', ['Campaign'])

        # Adding model 'Upload'
        db.create_table('adwords_sheets_upload', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('csv', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('loaded', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('adwords_sheets', ['Upload'])

        # Adding M2M table for field dayentries on 'Upload'
        db.create_table('adwords_sheets_upload_dayentries', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('upload', models.ForeignKey(orm['adwords_sheets.upload'], null=False)),
            ('dayentry', models.ForeignKey(orm['adwords_sheets.dayentry'], null=False))
        ))
        db.create_unique('adwords_sheets_upload_dayentries', ['upload_id', 'dayentry_id'])

        # Adding model 'DayEntry'
        db.create_table('adwords_sheets_dayentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adwords_sheets.Campaign'])),
            ('campaign_state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('budget', self.gf('django.db.models.fields.FloatField')()),
            ('budget_status', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('clicks', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('impressions', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('ctr', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('avg_cpc', self.gf('django.db.models.fields.FloatField')()),
            ('cost', self.gf('django.db.models.fields.FloatField')()),
            ('avg_position', self.gf('django.db.models.fields.FloatField')()),
            ('labels', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('adwords_sheets', ['DayEntry'])

        # Adding unique constraint on 'DayEntry', fields ['campaign', 'date']
        db.create_unique('adwords_sheets_dayentry', ['campaign_id', 'date'])


    def backwards(self, orm):
        # Removing unique constraint on 'DayEntry', fields ['campaign', 'date']
        db.delete_unique('adwords_sheets_dayentry', ['campaign_id', 'date'])

        # Deleting model 'Campaign'
        db.delete_table('adwords_sheets_campaign')

        # Deleting model 'Upload'
        db.delete_table('adwords_sheets_upload')

        # Removing M2M table for field dayentries on 'Upload'
        db.delete_table('adwords_sheets_upload_dayentries')

        # Deleting model 'DayEntry'
        db.delete_table('adwords_sheets_dayentry')


    models = {
        'adwords_sheets.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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