# Generated by Django 3.2.16 on 2023-02-04 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallerys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='photo_11',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='photo_12',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
