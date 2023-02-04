# Generated by Django 3.2.16 on 2023-02-04 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_7', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_8', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_9', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_10', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
    ]
