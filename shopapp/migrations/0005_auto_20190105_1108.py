# Generated by Django 2.1.4 on 2019-01-05 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_auto_20190104_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vip_reorder',
            old_name='eval_set',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='vip_reorder',
            old_name='days_since_prior_order',
            new_name='reordered',
        ),
    ]
