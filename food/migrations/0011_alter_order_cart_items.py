# Generated by Django 3.2.5 on 2021-09-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_register', '0005_alter_menu_food_type'),
        ('food', '0010_auto_20210921_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart_items',
            field=models.ManyToManyField(to='hotel_register.Menu'),
        ),
    ]
