# Generated by Django 2.2.6 on 2019-10-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0002_auto_20191016_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappingcodesystem',
            name='component_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mappingcodesystem',
            name='component_title',
            field=models.CharField(max_length=500),
        ),
    ]
