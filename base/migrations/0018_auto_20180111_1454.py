# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20180111_1441'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolioimage',
            options={'ordering': ['order'], 'verbose_name': 'Portfolio Image', 'verbose_name_plural': 'Portfolio Images'},
        ),
    ]
