# Generated by Django 2.2.9 on 2020-03-04 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0070_auto_20200303_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='mappingreleasecandidaterules',
            name='static_source_component_ident',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='mappingreleasecandidaterules',
            name='static_target_component_ident',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
