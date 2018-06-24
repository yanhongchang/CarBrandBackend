# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-24 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carbrand_id', models.CharField(max_length=64)),
                ('name_ch', models.CharField(max_length=64)),
                ('name_en', models.CharField(blank=True, max_length=128)),
                ('img', models.CharField(blank=True, max_length=1024)),
                ('introduction', models.TextField(blank=True)),
                ('website', models.CharField(blank=True, max_length=512)),
                ('ranking', models.IntegerField()),
                ('level', models.CharField(default=None, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_id', models.CharField(max_length=16)),
                ('country_name_ch', models.CharField(blank=True, max_length=128)),
                ('country_name_en', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('image_url', models.CharField(blank=True, max_length=1024)),
                ('guidence_price', models.CharField(max_length=128)),
                ('carbrand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carbrand.CarBrand')),
            ],
        ),
        migrations.AddField(
            model_name='carbrand',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carbrand.Country'),
        ),
    ]
