# Generated by Django 2.2.7 on 2019-11-26 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0053_auto_20191114_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='mappingcodesystem',
            name='codesystem_extra_dict',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
