# Generated by Django 5.0.3 on 2024-03-21 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.client'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='shop.item'),
        ),
    ]
