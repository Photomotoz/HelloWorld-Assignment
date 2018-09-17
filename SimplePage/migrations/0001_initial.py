# Generated by Django 2.1.1 on 2018-09-17 02:52

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address_1', models.CharField(max_length=100)),
                ('address_2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', localflavor.us.models.USStateField(max_length=2)),
                ('zip', localflavor.us.models.USZipCodeField(max_length=10)),
                ('country', models.CharField(choices=[('US', 'United States')], max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
