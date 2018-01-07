# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20180107_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioimage',
            name='caption',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='portfolioimage',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
