# Generated by Django 3.2.16 on 2023-02-07 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summercamp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]