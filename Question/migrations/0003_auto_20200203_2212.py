# Generated by Django 3.0.2 on 2020-02-03 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0002_longanswerquestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='longanswerquestion',
            name='dummy',
        ),
        migrations.AddField(
            model_name='question',
            name='q_type',
            field=models.CharField(choices=[('M', 'MultipleChoice'), ('L', 'LongAnswer'), ('D', 'Default')], default='M', max_length=1),
        ),
    ]