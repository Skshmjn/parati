# Generated by Django 3.1.4 on 2020-12-20 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtask',
            old_name='task',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task',
            new_name='title',
        ),
    ]
