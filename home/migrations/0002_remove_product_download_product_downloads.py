# Generated by Django 4.1.7 on 2023-03-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='download',
        ),
        migrations.AddField(
            model_name='product',
            name='downloads',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
