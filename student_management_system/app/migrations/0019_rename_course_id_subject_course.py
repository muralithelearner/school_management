# Generated by Django 4.2 on 2023-05-15 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='course_id',
            new_name='course',
        ),
    ]
