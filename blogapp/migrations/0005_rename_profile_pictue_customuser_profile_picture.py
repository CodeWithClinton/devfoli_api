# Generated by Django 5.1.2 on 2024-11-04 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_customuser_job_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='profile_pictue',
            new_name='profile_picture',
        ),
    ]
