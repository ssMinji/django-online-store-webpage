# Generated by Django 2.1.4 on 2019-01-06 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0011_auto_20190107_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_small',
            name='aisle_id',
        ),
        migrations.DeleteModel(
            name='Product_small',
        ),
    ]
