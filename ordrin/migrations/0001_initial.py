# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sighting'
        db.create_table('ordrin_sighting', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('thumb_280', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('ordrin', ['Sighting'])


    def backwards(self, orm):
        # Deleting model 'Sighting'
        db.delete_table('ordrin_sighting')


    models = {
        'ordrin.sighting': {
            'Meta': {'object_name': 'Sighting'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'thumb_280': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['ordrin']