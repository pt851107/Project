# Generated by Django 3.2.16 on 2023-02-08 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summercamp', '0004_camp_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='information',
            field=models.TextField(blank=True),
        ),
    ]
