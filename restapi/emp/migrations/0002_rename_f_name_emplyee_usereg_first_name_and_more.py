# Generated by Django 4.0.2 on 2022-02-21 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emplyee_usereg',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='emplyee_usereg',
            old_name='l_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='emplyee_usereg',
            old_name='ph_no',
            new_name='phone_no',
        ),
    ]
