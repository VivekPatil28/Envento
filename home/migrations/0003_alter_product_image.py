# Generated by Django 4.1.7 on 2023-03-29 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_product_download_product_downloads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
