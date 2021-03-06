# Generated by Django 2.2.5 on 2019-10-15 08:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20191014_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo_back',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/ichristwin/image/upload/v1571126185/wmbalgw9rof6jen0ni5q.png', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='item',
            name='photo_front',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/ichristwin/image/upload/v1571126185/wmbalgw9rof6jen0ni5q.png', max_length=255, verbose_name='image'),
        ),
        migrations.DeleteModel(
            name='CloudinaryItemPhoto',
        ),
    ]
