# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_auto_20180110_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioimage',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='portfolioimage',
            name='object_id',
        ),
        migrations.AddField(
            model_name='portfolioimage',
            name='project',
            field=models.ForeignKey(blank=True, to='base.Project', null=True),
        ),
        migrations.AddField(
            model_name='portfolioimage',
            name='system',
            field=models.ForeignKey(blank=True, to='base.System', null=True),
        ),
    ]
