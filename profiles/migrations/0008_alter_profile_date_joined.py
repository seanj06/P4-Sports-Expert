# Generated by Django 3.2.18 on 2023-04-02 12:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20230315_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_joined',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
