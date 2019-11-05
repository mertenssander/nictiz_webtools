# Generated by Django 2.2.6 on 2019-10-22 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0034_auto_20191022_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='mappingproject',
            name='source_codesystem',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='mapping.MappingCodesystem'),
            preserve_default=False,
        ),
    ]
