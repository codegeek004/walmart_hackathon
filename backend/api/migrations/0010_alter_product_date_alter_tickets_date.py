# Generated by Django 5.2.4 on 2025-07-23 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_product_date_alter_tickets_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2025, 7, 23, 6, 23, 33, 624281, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2025, 7, 23, 6, 23, 33, 623376, tzinfo=datetime.timezone.utc)),
        ),
    ]
