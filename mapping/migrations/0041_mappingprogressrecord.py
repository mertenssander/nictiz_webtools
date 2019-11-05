# Generated by Django 2.2.6 on 2019-10-25 18:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0040_mappingproject_status_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='MappingProgressRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('labels', models.TextField()),
                ('values', models.TextField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
