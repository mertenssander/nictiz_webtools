# Generated by Django 2.2.6 on 2019-10-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0010_auto_20191018_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappingrule',
            name='active',
            field=models.BooleanField(max_length=50, null=True),
        ),
    ]
