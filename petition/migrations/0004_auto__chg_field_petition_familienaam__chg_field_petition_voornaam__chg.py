# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Petition.familienaam'
        db.alter_column('petition_petition', 'familienaam', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Petition.voornaam'
        db.alter_column('petition_petition', 'voornaam', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Petition.organisatie'
        db.alter_column('petition_petition', 'organisatie', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Petition.familienaam'
        raise RuntimeError("Cannot reverse this migration. 'Petition.familienaam' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Petition.voornaam'
        raise RuntimeError("Cannot reverse this migration. 'Petition.voornaam' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Petition.organisatie'
        raise RuntimeError("Cannot reverse this migration. 'Petition.organisatie' and its values cannot be restored.")

    models = {
        'petition.petition': {
            'Meta': {'object_name': 'Petition'},
            'emailadres': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'familienaam': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gemeente': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organisatie': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'straat': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'voornaam': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['petition']