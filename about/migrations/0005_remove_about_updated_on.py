# Generated by Django 4.2.13 on 2024-08-06 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_delete_testimonial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='updated_on',
        ),
    ]
