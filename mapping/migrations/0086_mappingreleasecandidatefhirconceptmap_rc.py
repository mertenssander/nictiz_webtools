# Generated by Django 2.2.9 on 2020-03-16 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0085_auto_20200316_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='mappingreleasecandidatefhirconceptmap',
            name='rc',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='mapping.MappingReleaseCandidate'),
        ),
    ]
