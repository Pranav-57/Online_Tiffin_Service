# Generated by Django 3.2.5 on 2021-09-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_alter_order_cart_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart_items',
            field=models.ManyToManyField(to='food.Cart'),
        ),
    ]
