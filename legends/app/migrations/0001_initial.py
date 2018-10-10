# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-10-02 18:08
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Title')),
                ('slug', models.SlugField(unique=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name='Content')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
