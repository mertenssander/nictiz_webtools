# Generated by Django 2.2.13 on 2020-06-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0100_auto_20200622_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappingeclpart',
            name='failed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mappingeclpart',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
