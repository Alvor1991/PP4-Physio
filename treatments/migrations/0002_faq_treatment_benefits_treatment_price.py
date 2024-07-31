# Generated by Django 4.2.13 on 2024-07-27 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='treatment',
            name='benefits',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]