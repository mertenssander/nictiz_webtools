# Generated by Django 2.2.9 on 2020-03-05 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0073_mappingreleasecandidate_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappingreleasecandidate',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]