# Generated by Django 4.2.3 on 2023-08-01 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_customer_contact_info_submission_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_contact_info',
            name='submission_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
