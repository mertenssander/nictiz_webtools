# Generated by Django 2.2.9 on 2020-03-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0075_auto_20200306_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappingproject',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
