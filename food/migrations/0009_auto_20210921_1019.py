# Generated by Django 3.2.6 on 2021-09-21 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='menu_details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food.order'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
