# Generated by Django 4.2.1 on 2023-06-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milestones', '0006_loggedmilestone'),
    ]

    operations = [
        migrations.AddField(
            model_name='loggedmilestone',
            name='date_observed',
            field=models.DateField(blank=True, null=True),
        ),
    ]
