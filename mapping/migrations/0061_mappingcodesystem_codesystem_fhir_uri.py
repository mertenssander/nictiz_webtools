# Generated by Django 2.2.9 on 2020-02-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0060_auto_20200204_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='mappingcodesystem',
            name='codesystem_fhir_uri',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
    ]
