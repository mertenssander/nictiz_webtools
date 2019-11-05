# Generated by Django 2.2.6 on 2019-10-22 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0033_auto_20191022_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappingtask',
            name='source_codesystem',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='source_codesystem_task', to='mapping.MappingCodesystem'),
        ),
        migrations.AlterField(
            model_name='mappingtask',
            name='status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='mapping.MappingTaskStatus'),
        ),
        migrations.AlterField(
            model_name='mappingtask',
            name='target_codesystem',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='target_codesystem_task', to='mapping.MappingCodesystem'),
        ),
        migrations.AlterField(
            model_name='mappingtask',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
