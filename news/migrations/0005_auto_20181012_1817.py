# Generated by Django 2.1.1 on 2018-10-12 09:17

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20181012_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=stdimage.models.StdImageField(blank=True, upload_to='picture/news'),
        ),
    ]
