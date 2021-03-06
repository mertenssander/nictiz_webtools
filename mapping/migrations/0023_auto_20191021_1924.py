# Generated by Django 2.2.6 on 2019-10-21 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0022_auto_20191021_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappingcomment',
            name='comment_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mappingrule',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.MappingProject'),
        ),
        migrations.AlterField(
            model_name='mappingrule',
            name='source_component',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_codesystem_rule', to='mapping.MappingCodesystem'),
        ),
        migrations.AlterField(
            model_name='mappingrule',
            name='target_component',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_codesystem_rule', to='mapping.MappingCodesystem'),
        ),
        migrations.AlterField(
            model_name='mappingtask',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.MappingProject'),
        ),
        migrations.AlterField(
            model_name='mappingtask',
            name='source_codesystem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_codesystem_task', to='mapping.MappingCodesystem'),
        ),
        migrations.AlterField(
            model_name='mappingtask',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.MappingTaskStatus'),
        ),
        migrations.AlterField(
            model_name='mappingtask',
            name='target_codesystem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_codesystem_task', to='mapping.MappingCodesystem'),
        ),
        migrations.AlterField(
            model_name='mappingtask',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mappingtaskstatus',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.MappingProject'),
        ),
        migrations.AlterField(
            model_name='mappingtaskstatus',
            name='status_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.MappingTaskStatus'),
        ),
    ]
