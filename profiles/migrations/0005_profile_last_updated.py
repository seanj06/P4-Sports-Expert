# Generated by Django 3.2.18 on 2023-03-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]