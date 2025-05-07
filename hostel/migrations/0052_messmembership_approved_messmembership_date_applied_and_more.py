from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0051_alter_messmenu_meal_time'),  # Replace with your previous migration
    ]

    operations = [
        migrations.AddField(
            model_name='messmembership',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='messmembership',
            name='date_applied',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
        ),
    ]
