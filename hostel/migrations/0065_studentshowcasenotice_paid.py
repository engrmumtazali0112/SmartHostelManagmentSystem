# Generated by Django 5.0.4 on 2025-04-09 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0064_alter_messpayment_payment_method_messpaymentrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentshowcasenotice',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
