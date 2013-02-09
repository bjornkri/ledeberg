# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Petition'
        db.create_table('petition_petition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naam', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('voornaam', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('straat', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('huisnummer', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gemeente', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('emailadres', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal('petition', ['Petition'])


    def backwards(self, orm):
        # Deleting model 'Petition'
        db.delete_table('petition_petition')


    models = {
        'petition.petition': {
            'Meta': {'object_name': 'Petition'},
            'emailadres': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'gemeente': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'huisnummer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'straat': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'voornaam': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['petition']