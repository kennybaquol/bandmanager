# Generated by Django 4.0.6 on 2022-09-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_gig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='foh',
            field=models.CharField(blank=True, max_length=150, verbose_name='Sound Person'),
        ),
        migrations.AlterField(
            model_name='gig',
            name='fohConfirmed',
            field=models.BooleanField(verbose_name='Is the sound person confirmed?'),
        ),
        migrations.AlterField(
            model_name='gig',
            name='setTime',
            field=models.CharField(max_length=150, verbose_name='Set Time'),
        ),
    ]