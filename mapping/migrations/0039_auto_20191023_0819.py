# Generated by Django 2.2.6 on 2019-10-23 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0038_mappingeventlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='mappingeventlog',
            name='new_data',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mappingeventlog',
            name='old_data',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
