# Generated by Django 2.2.5 on 2019-10-05 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('interest', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField(null=True)),
                ('bank', models.CharField(choices=[('first', 'First Bank'), ('access', 'Access Bank'), ('zenith', 'Zenith Bank'), ('fidelity', 'Fidelity Bank'), ('skye', 'Skye Bank'), ('uba', 'UBA'), ('union', 'Union Bank'), ('stanbic', 'Stanbic Bank')], max_length=60)),
                ('ok', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DisburseDeposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disbursed', models.BooleanField(default=False)),
                ('editable', models.BooleanField(default=True)),
                ('acc_name', models.CharField(default='', max_length=255)),
                ('acc_number', models.IntegerField(null=True)),
                ('bank', models.CharField(choices=[('first', 'First Bank'), ('access', 'Access Bank'), ('zenith', 'Zenith Bank'), ('fidelity', 'Fidelity Bank'), ('skye', 'Skye Bank'), ('uba', 'UBA'), ('union', 'Union Bank'), ('stanbic', 'Stanbic Bank')], default='', max_length=60)),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='interest.Offer')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CollectDeposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(null=True)),
                ('date', models.DateField(null=True)),
                ('received', models.BooleanField(default=False)),
                ('trnx_id', models.CharField(default='', max_length=255)),
                ('acc_name', models.CharField(default='', max_length=255)),
                ('acc_number', models.IntegerField(null=True)),
                ('bank', models.CharField(choices=[('first', 'First Bank'), ('access', 'Access Bank'), ('zenith', 'Zenith Bank'), ('fidelity', 'Fidelity Bank'), ('skye', 'Skye Bank'), ('uba', 'UBA'), ('union', 'Union Bank'), ('stanbic', 'Stanbic Bank')], default='', max_length=60)),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='interest.Offer')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
