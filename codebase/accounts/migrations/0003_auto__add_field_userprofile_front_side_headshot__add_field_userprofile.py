# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserProfile.front_side_headshot'
        db.add_column('accounts_userprofile', 'front_side_headshot',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'UserProfile.back_of_headshot'
        db.add_column('accounts_userprofile', 'back_of_headshot',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'UserProfile.front_full_body'
        db.add_column('accounts_userprofile', 'front_full_body',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'UserProfile.front_45_full_body'
        db.add_column('accounts_userprofile', 'front_45_full_body',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'UserProfile.front_side_full_body'
        db.add_column('accounts_userprofile', 'front_side_full_body',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'UserProfile.back_of_full_body'
        db.add_column('accounts_userprofile', 'back_of_full_body',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserProfile.front_side_headshot'
        db.delete_column('accounts_userprofile', 'front_side_headshot')

        # Deleting field 'UserProfile.back_of_headshot'
        db.delete_column('accounts_userprofile', 'back_of_headshot')

        # Deleting field 'UserProfile.front_full_body'
        db.delete_column('accounts_userprofile', 'front_full_body')

        # Deleting field 'UserProfile.front_45_full_body'
        db.delete_column('accounts_userprofile', 'front_45_full_body')

        # Deleting field 'UserProfile.front_side_full_body'
        db.delete_column('accounts_userprofile', 'front_side_full_body')

        # Deleting field 'UserProfile.back_of_full_body'
        db.delete_column('accounts_userprofile', 'back_of_full_body')


    models = {
        'accounts.cropphototool': {
            'Meta': {'object_name': 'CropPhotoTool'},
            'cropping': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'accounts.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'arm': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'back': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'back_of_full_body': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'back_of_headshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'background': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bicep': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bust': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'chest': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'default': "'1992-10-10'"}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'default': "'WH'", 'max_length': '2'}),
            'eye_colour': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'front_45_full_body': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'front_45_headshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'front_full_body': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'front_headshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'front_side_full_body': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'front_side_headshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'hair_colour': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'head': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hips': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inner_leg': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'neck': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'outer_leg': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'polls_voted': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['polls.Poll']", 'symmetrical': 'False'}),
            'shoe_size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'waist': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'wrist': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'polls.poll': {
            'Meta': {'object_name': 'Poll'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['accounts']