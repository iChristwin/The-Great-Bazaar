# Generated by Django 2.2.5 on 2019-10-09 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='acc_no',
        ),
    ]