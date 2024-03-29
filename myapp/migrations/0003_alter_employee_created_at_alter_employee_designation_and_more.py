# Generated by Django 5.0.1 on 2024-01-04 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_employee_created_at_employee_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email_address',
            field=models.EmailField(default='example@example.com', max_length=100, unique=True),
        ),
    ]
