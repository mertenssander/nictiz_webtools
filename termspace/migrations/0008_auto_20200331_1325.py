# Generated by Django 2.2.11 on 2020-03-31 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('termspace', '0007_termspacetasks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TermspaceTasks',
            new_name='TermspaceTask',
        ),
    ]
