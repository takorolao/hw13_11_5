# Generated by Django 4.2.1 on 2023-11-13 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger_app', '0003_burger_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='burger',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='burgers/'),
        ),
    ]
