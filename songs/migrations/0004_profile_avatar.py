# Generated by Django 5.1.4 on 2025-01-18 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_track_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]
