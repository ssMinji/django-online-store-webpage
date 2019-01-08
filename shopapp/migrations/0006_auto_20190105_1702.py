# Generated by Django 2.1.4 on 2019-01-05 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_auto_20190105_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vip_aisle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aisle', models.CharField(max_length=200, null=True)),
                ('ratio', models.FloatField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='Night',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Prior_reorder',
        ),
        migrations.RemoveField(
            model_name='product_middle',
            name='department_id',
        ),
        migrations.RemoveField(
            model_name='product_small',
            name='aisle_id',
        ),
        migrations.DeleteModel(
            name='Vip_organic',
        ),
        migrations.DeleteModel(
            name='Product_big',
        ),
        migrations.DeleteModel(
            name='Product_middle',
        ),
        migrations.DeleteModel(
            name='Product_small',
        ),
    ]