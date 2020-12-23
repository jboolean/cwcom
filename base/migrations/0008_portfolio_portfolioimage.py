# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20170920_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('info', models.CharField(max_length=255, null=True)),
                ('description', tinymce.models.HTMLField(null=True, blank=True)),
                ('press', tinymce.models.HTMLField(null=True, blank=True)),
                ('texts', models.ManyToManyField(to='base.Text', blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='images', verbose_name='Image')),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('is_primary', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('portfolio', models.ForeignKey(to='base.Portfolio', on_delete = models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
