# Generated by Django 4.0.6 on 2022-08-17 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_band_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='status',
            field=models.CharField(choices=[('N', 'Not Contacted'), ('C', 'Contacted'), ('F', 'Followed Up With'), ('B', 'Successfully Booked'), ('X', 'Not Going To Work')], max_length=30),
        ),
    ]
