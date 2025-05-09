# Generated by Django 5.0.4 on 2025-04-17 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0067_stripepayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(choices=[('One Seater', 'One Seater'), ('Two Seater', 'Two Seater'), ('Three Seater', 'Three Seater'), ('Four Seater', 'Four Seater'), ('Five Seater', 'Five Seater'), ('Six Seater', 'Six Seater'), ('Seven Seater', 'Seven Seater'), ('Eight Seater', 'Eight Seater'), ('Nine Seater', 'Nine Seater'), ('Ten Seater', 'Ten Seater')], max_length=50, unique=True)),
                ('capacity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.RenameField(
            model_name='hostel',
            old_name='Single_Seater_Rooms',
            new_name='Eight_Seater_Rooms',
        ),
        migrations.AddField(
            model_name='hostel',
            name='Five_Seater_Rooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hostel',
            name='Four_Seater_Rooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hostel',
            name='Nine_Seater_Rooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hostel',
            name='One_Seater_Rooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hostel',
            name='Seven_Seater_Rooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hostel',
            name='Ten_Seater_Rooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='room_type_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='hostel.roomtype'),
        ),
    ]
