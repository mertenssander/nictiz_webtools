# Generated by Django 2.2.12 on 2020-05-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postcoordination', '0006_auto_20200515_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attributeset',
            name='template',
        ),
        migrations.AddField(
            model_name='attributeset',
            name='template',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='Template', to='postcoordination.template'),
        ),
    ]
