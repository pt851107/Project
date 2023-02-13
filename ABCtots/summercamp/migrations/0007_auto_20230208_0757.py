# Generated by Django 3.2.16 on 2023-02-08 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summercamp', '0006_camp_activities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camp',
            name='image',
        ),
        migrations.AddField(
            model_name='camp',
            name='date',
            field=models.DateField(auto_now_add=True, default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camp',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='camp',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='camp',
            name='photo_main',
            field=models.ImageField(default=4, upload_to='photos/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
