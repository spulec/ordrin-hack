# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sighting.item_name'
        db.add_column('ordrin_sighting', 'item_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Sighting.place_name'
        db.add_column('ordrin_sighting', 'place_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sighting.item_name'
        db.delete_column('ordrin_sighting', 'item_name')

        # Deleting field 'Sighting.place_name'
        db.delete_column('ordrin_sighting', 'place_name')


    models = {
        'ordrin.sighting': {
            'Meta': {'object_name': 'Sighting'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'item_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'place_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'thumb_280': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['ordrin']