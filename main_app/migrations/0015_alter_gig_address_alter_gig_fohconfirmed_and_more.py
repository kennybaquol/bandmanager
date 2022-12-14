# Generated by Django 4.0.6 on 2022-09-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_alter_gig_city_alter_gig_fohconfirmed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='gig',
            name='fohConfirmed',
            field=models.CharField(blank=True, max_length=50, verbose_name='Is the sound person confirmed?'),
        ),
        migrations.AlterField(
            model_name='gig',
            name='setTime',
            field=models.CharField(blank=True, max_length=50, verbose_name='Set Time'),
        ),
    ]
