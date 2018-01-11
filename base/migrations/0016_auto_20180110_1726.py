# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_auto_20180110_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioimage',
            name='parent_content_type',
        ),
        migrations.RemoveField(
            model_name='portfolioimage',
            name='parent_object_id',
        ),
        migrations.AlterField(
            model_name='portfolioimage',
            name='content_type',
            field=models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True),
        ),
        migrations.AlterField(
            model_name='portfolioimage',
            name='object_id',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
