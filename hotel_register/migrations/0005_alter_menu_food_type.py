# Generated by Django 3.2.5 on 2021-09-11 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_register', '0004_menu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='food_type',
            field=models.CharField(choices=[('Vegetarian', 'vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian'), ('Dessert', 'Dessert'), ('Breakfast', 'Breakfast'), ('Sweet', 'Sweet')], max_length=20),
        ),
    ]
