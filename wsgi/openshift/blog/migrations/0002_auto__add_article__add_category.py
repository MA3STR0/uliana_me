# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'blog_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('content_markdown', self.gf('django.db.models.fields.TextField')()),
            ('content_markup', self.gf('django.db.models.fields.TextField')()),
            ('date_publish', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'blog', ['Article'])

        # Adding M2M table for field categories on 'Article'
        m2m_table_name = db.shorten_name(u'blog_article_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm[u'blog.article'], null=False)),
            ('category', models.ForeignKey(orm[u'blog.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['article_id', 'category_id'])

        # Adding model 'Category'
        db.create_table(u'blog_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'blog', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'blog_article')

        # Removing M2M table for field categories on 'Article'
        db.delete_table(db.shorten_name(u'blog_article_categories'))

        # Deleting model 'Category'
        db.delete_table(u'blog_category')


    models = {
        u'blog.article': {
            'Meta': {'ordering': "['-date_publish']", 'object_name': 'Article'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['blog.Category']", 'null': 'True', 'blank': 'True'}),
            'content_markdown': ('django.db.models.fields.TextField', [], {}),
            'content_markup': ('django.db.models.fields.TextField', [], {}),
            'date_publish': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.category': {
            'Meta': {'ordering': "['title']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']