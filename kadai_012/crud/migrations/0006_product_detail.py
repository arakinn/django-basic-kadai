# Generated by Django 5.1.3 on 2024-11-08 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
