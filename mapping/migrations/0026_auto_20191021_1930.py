# Generated by Django 2.2.6 on 2019-10-21 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0025_auto_20191021_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappingtaskstatus',
            name='status_id',
            field=models.IntegerField(),
        ),
    ]
