# Generated by Django 4.0.6 on 2022-09-26 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_inventoryitem_batchcost_inventoryitem_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='batchCost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='sellingPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20),
        ),
    ]
