# Generated by Django 2.1.4 on 2019-01-03 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['department']},
        ),
    ]
