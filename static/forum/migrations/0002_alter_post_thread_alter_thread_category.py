# Generated by Django 4.2.1 on 2023-06-02 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='forum.thread'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='forum.category'),
        ),
    ]
