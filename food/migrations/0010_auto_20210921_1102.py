# Generated by Django 3.2.6 on 2021-09-21 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_auto_20210921_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_to',
        ),
        migrations.AddField(
            model_name='order',
            name='order_till',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_from',
            field=models.DateField(blank=True, null=True),
        ),
    ]
