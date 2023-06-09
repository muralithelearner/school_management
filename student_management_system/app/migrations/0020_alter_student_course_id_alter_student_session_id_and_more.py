# Generated by Django 4.2 on 2023-05-16 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_course_id_subject_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.courses'),
        ),
        migrations.AlterField(
            model_name='student',
            name='session_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.session_year'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.courses'),
        ),
    ]
