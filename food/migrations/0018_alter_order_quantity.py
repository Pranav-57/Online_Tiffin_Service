# Generated by Django 3.2.5 on 2021-09-21 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0017_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.CharField(blank=True, default='', max_length=1000000, null=True),
        ),
    ]
