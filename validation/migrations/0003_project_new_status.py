# Generated by Django 2.2.12 on 2020-08-12 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0002_auto_20200812_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='new_status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='status_new_tasks', to='validation.Status'),
        ),
    ]
