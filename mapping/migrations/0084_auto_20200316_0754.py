# Generated by Django 2.2.9 on 2020-03-16 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0083_mappingreleasecandidatecache'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MappingReleaseCandidateCache',
            new_name='MappingReleaseCandidateFHIRConceptMap',
        ),
    ]
