# Generated by Django 4.2.13 on 2024-07-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_contactrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
