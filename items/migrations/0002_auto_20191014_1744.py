# Generated by Django 2.2.5 on 2019-10-14 17:44

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='back_photo',
        ),
        migrations.RemoveField(
            model_name='item',
            name='front_photo',
        ),
        migrations.CreateModel(
            name='CloudinaryItemPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='items.Item')),
            ],
        ),
    ]
