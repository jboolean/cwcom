# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('base', '0010_auto_20180107_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioimage',
            name='content_type',
            field=models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='portfolioimage',
            name='object_id',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
