# Generated by Django 4.2.3 on 2023-07-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_otpcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpcode',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
