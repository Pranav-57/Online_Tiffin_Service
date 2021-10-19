# Generated by Django 3.2.5 on 2021-08-26 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_register', '0003_hotel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('more_image', models.ImageField(upload_to='menu')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_register.menu')),
            ],
        ),
    ]
