# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sighting.review_id'
        db.add_column('ordrin_sighting', 'review_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sighting.review_id'
        db.delete_column('ordrin_sighting', 'review_id')


    models = {
        'ordrin.sighting': {
            'Meta': {'object_name': 'Sighting'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'item_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'place_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'review_id': ('django.db.models.fields.IntegerField', [], {}),
            'thumb_280': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['ordrin']