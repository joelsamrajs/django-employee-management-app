# Generated by Django 4.0.4 on 2022-04-16 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_profile_salary'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='leave',
            unique_together={('profile', 'leave_date')},
        ),
    ]