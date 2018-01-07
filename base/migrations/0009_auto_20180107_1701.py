# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_portfolio_portfolioimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='description',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='info',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='press',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='texts',
        ),
    ]
