# Generated by Django 5.0.4 on 2025-03-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0040_paymentrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentrequest',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
