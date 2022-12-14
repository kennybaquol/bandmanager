# Generated by Django 4.0.6 on 2022-09-26 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_alter_gig_city_alter_gig_date_alter_gig_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('CL', 'Clothing'), ('MU', 'Music'), ('ME', 'Merchandise')], default='CL', max_length=12)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.band')),
            ],
        ),
    ]
