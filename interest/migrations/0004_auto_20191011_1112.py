# Generated by Django 2.2.5 on 2019-10-11 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0003_auto_20191011_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='stock',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='store.Stock'),
        ),
    ]
