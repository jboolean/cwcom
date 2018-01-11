# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('base', '0014_auto_20180110_1715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolioimage',
            old_name='linked_object_id',
            new_name='parent_object_id',
        ),
        migrations.RemoveField(
            model_name='portfolioimage',
            name='linked_content_type',
        ),
        migrations.AddField(
            model_name='portfolioimage',
            name='content_type',
            field=models.ForeignKey(default=1, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioimage',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioimage',
            name='parent_content_type',
            field=models.ForeignKey(related_name='parent_test_link', blank=True, to='contenttypes.ContentType', null=True),
        ),
    ]
