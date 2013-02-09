# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Petition.naam'
        db.delete_column('petition_petition', 'naam')

        # Adding field 'Petition.familienaam'
        db.add_column('petition_petition', 'familienaam',
                      self.gf('django.db.models.fields.CharField')(default='Familienaam', max_length=255),
                      keep_default=False)

        # Adding field 'Petition.organisatie'
        db.add_column('petition_petition', 'organisatie',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Petition.naam'
        raise RuntimeError("Cannot reverse this migration. 'Petition.naam' and its values cannot be restored.")
        # Deleting field 'Petition.familienaam'
        db.delete_column('petition_petition', 'familienaam')

        # Deleting field 'Petition.organisatie'
        db.delete_column('petition_petition', 'organisatie')


    models = {
        'petition.petition': {
            'Meta': {'object_name': 'Petition'},
            'emailadres': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'familienaam': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gemeente': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'huisnummer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organisatie': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'straat': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'voornaam': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['petition']