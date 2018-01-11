# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20180110_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolioimage',
            old_name='linked_content_type',
            new_name='content_type',
        ),
        migrations.RenameField(
            model_name='portfolioimage',
            old_name='linked_object_id',
            new_name='object_id',
        ),
    ]
