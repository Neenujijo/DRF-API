# Generated by Django 4.0.2 on 2022-02-24 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0003_employees_profile_alter_emplyee_usereg_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees_profile',
            name='Emp_code',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='emplyee_usereg',
            name='phone_no',
            field=models.CharField(max_length=10),
        ),
    ]
