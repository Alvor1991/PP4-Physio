# appointments/migrations/0002_add_time_field.py

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default='00:00:00'),  
            preserve_default=False,
        ),
    ]
