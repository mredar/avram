# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Campus'
        db.create_table(u'library_collection_campus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal(u'library_collection', ['Campus'])

        # Adding model 'Status'
        db.create_table(u'library_collection_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'library_collection', ['Status'])

        # Adding model 'Restriction'
        db.create_table(u'library_collection_restriction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'library_collection', ['Restriction'])

        # Adding model 'Need'
        db.create_table(u'library_collection_need', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'library_collection', ['Need'])

        # Adding model 'ProvenancialCollection'
        db.create_table(u'library_collection_provenancialcollection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from=('name', 'description'), overwrite=False)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url_local', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('url_oac', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('url_was', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('url_oai', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('hosted', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['library_collection.Status'], null=True, blank=True)),
            ('extent', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('access_restrictions', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['library_collection.Restriction'], null=True, blank=True)),
            ('metadata_level', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('metadata_standard', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('need_for_dams', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['library_collection.Need'], null=True, blank=True)),
            ('oai_set_spec', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('appendix', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('phase_one', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'library_collection', ['ProvenancialCollection'])

        # Adding M2M table for field campus on 'ProvenancialCollection'
        db.create_table(u'library_collection_provenancialcollection_campus', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('provenancialcollection', models.ForeignKey(orm[u'library_collection.provenancialcollection'], null=False)),
            ('campus', models.ForeignKey(orm[u'library_collection.campus'], null=False))
        ))
        db.create_unique(u'library_collection_provenancialcollection_campus', ['provenancialcollection_id', 'campus_id'])


    def backwards(self, orm):
        # Deleting model 'Campus'
        db.delete_table(u'library_collection_campus')

        # Deleting model 'Status'
        db.delete_table(u'library_collection_status')

        # Deleting model 'Restriction'
        db.delete_table(u'library_collection_restriction')

        # Deleting model 'Need'
        db.delete_table(u'library_collection_need')

        # Deleting model 'ProvenancialCollection'
        db.delete_table(u'library_collection_provenancialcollection')

        # Removing M2M table for field campus on 'ProvenancialCollection'
        db.delete_table('library_collection_provenancialcollection_campus')


    models = {
        u'library_collection.campus': {
            'Meta': {'object_name': 'Campus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        u'library_collection.need': {
            'Meta': {'object_name': 'Need'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'library_collection.provenancialcollection': {
            'Meta': {'object_name': 'ProvenancialCollection'},
            'access_restrictions': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['library_collection.Restriction']", 'null': 'True', 'blank': 'True'}),
            'appendix': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'campus': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library_collection.Campus']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'extent': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hosted': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata_level': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'metadata_standard': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'need_for_dams': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['library_collection.Need']", 'null': 'True', 'blank': 'True'}),
            'oai_set_spec': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'phase_one': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "('name', 'description')", 'overwrite': 'False'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['library_collection.Status']", 'null': 'True', 'blank': 'True'}),
            'url_local': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'url_oac': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'url_oai': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'url_was': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'library_collection.restriction': {
            'Meta': {'object_name': 'Restriction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'library_collection.status': {
            'Meta': {'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['library_collection']