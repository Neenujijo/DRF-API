# Generated by Django 4.0.2 on 2022-02-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0006_delete_employees_profile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_designation', models.CharField(max_length=100)),
                ('Emp_code', models.CharField(max_length=300)),
                ('Emp_department', models.CharField(max_length=50)),
                ('Emp_skills', models.CharField(max_length=300)),
            ],
        ),
    ]
