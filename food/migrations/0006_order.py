# Generated by Django 3.2.6 on 2021-09-20 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel_register', '0005_alter_menu_food_type'),
        ('food', '0005_alter_application_form_delivery_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_from', models.DateField()),
                ('order_to', models.DateField()),
                ('delivery_time', models.TimeField()),
                ('menu_items', models.ManyToManyField(to='hotel_register.Menu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
