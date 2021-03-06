# Generated by Django 2.2.4 on 2019-08-06 12:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('searchterm', models.CharField(default='onbekend', max_length=30)),
                ('execution_time', models.CharField(max_length=30)),
            ],
        ),
    ]
