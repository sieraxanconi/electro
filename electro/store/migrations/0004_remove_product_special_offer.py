# Generated by Django 4.0.6 on 2022-07-15 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_special_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='special_offer',
        ),
    ]
