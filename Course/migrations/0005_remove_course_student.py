# Generated by Django 2.0.7 on 2020-01-09 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0004_course_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='Student',
        ),
    ]
