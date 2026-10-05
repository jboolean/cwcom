import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_portfolioimage_image_alter_projectimage_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentblock',
            name='image',
            field=base.models.S3UploadFieldWithPath(blank=True, dest='images', null=True, verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='contentblock',
            name='image_alt',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
