# Generated by Django 2.2.6 on 2019-10-21 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0023_auto_20191021_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappingcomment',
            name='comment_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.MappingTask'),
        ),
    ]
