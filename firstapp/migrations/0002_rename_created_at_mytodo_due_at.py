# Generated by Django 5.0.6 on 2024-07-28 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mytodo',
            old_name='created_at',
            new_name='due_at',
        ),
    ]
