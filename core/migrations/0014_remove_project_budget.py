# Generated by Django 4.1.13 on 2024-01-27 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_projectview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='budget',
        ),
    ]
