# Generated by Django 2.2.7 on 2019-11-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0052_auto_20191113_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappingeclquery',
            name='query_type',
            field=models.CharField(blank=True, choices=[('1', 'Children'), ('2', 'Descendants and self'), ('3', 'Custom')], default=None, max_length=50, null=True),
        ),
    ]
