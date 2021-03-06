# Generated by Django 2.2.12 on 2020-05-12 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postcoordination', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='attribute_values',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='postcoordination.attributeValue'),
        ),
        migrations.AlterField(
            model_name='template',
            name='attributes',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='postcoordination.attribute'),
        ),
    ]
