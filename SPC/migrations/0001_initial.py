# Generated by Django 3.0 on 2019-12-08 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Course', '0001_initial'),
        ('Student', '0001_initial'),
        ('Professor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.Course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Professor.Professor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Student')),
            ],
        ),
    ]
