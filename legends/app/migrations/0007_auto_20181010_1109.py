# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-10-10 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_article_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Player name')),
                ('nickname', models.CharField(max_length=255, verbose_name='Nickname')),
                ('nation', models.CharField(max_length=255, verbose_name='nation')),
                ('born', models.DateField()),
                ('clubs', models.TextField(default='', verbose_name='Clubs played')),
                ('appeareances', models.IntegerField(verbose_name='Total appeareances')),
                ('goals', models.IntegerField(verbose_name='Total goals')),
                ('created_at', models.DateField()),
                ('modified_at', models.DateField()),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='card',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='card', to='app.Card', verbose_name='Player Card'),
        ),
    ]
