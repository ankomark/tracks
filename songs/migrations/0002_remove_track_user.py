# Generated by Django 5.1.4 on 2025-01-15 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='user',
        ),
    ]
