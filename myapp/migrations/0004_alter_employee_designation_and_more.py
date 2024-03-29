# Generated by Django 5.0.1 on 2024-01-04 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_employee_created_at_alter_employee_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email_address',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
