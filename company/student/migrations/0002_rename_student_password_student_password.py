# Generated by Django 4.2.1 on 2023-06-20 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_password',
            new_name='password',
        ),
    ]