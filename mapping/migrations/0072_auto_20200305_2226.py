# Generated by Django 2.2.9 on 2020-03-05 21:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0071_auto_20200304_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='mappingreleasecandidate',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='mappingreleasecandidate',
            name='status',
            field=models.CharField(blank=True, choices=[('0', 'Testing'), ('1', 'Experimental'), ('2', 'Acceptance'), ('3', 'Production')], default=None, max_length=50, null=True),
        ),
    ]
