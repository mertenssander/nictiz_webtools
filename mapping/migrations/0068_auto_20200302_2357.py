# Generated by Django 2.2.9 on 2020-03-02 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0067_auto_20200302_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappingreleasecandidate',
            name='rules',
            field=models.ManyToManyField(blank=True, default=None, to='mapping.MappingReleaseCandidateRules'),
        ),
        migrations.AlterField(
            model_name='mappingreleasecandidaterules',
            name='accepted',
            field=models.ManyToManyField(default=None, null=True, related_name='accepted_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mappingreleasecandidaterules',
            name='export_rule',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='mapping.MappingRule'),
        ),
        migrations.AlterField(
            model_name='mappingreleasecandidaterules',
            name='export_task',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='mapping.MappingTask'),
        ),
        migrations.AlterField(
            model_name='mappingreleasecandidaterules',
            name='rejected',
            field=models.ManyToManyField(blank=True, default=None, related_name='rejected_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mappingreleasecandidaterules',
            name='source_component',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='source_component', to='mapping.MappingCodesystemComponent'),
        ),
        migrations.AlterField(
            model_name='mappingreleasecandidaterules',
            name='target_component',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='target_component', to='mapping.MappingCodesystemComponent'),
        ),
    ]
