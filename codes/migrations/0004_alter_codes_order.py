# Generated by Django 4.2.4 on 2023-12-06 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_phone'),
        ('codes', '0003_remove_codes_orderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codes',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='orders.order'),
        ),
    ]
