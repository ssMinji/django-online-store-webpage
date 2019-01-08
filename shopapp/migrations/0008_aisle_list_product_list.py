# Generated by Django 2.1.4 on 2019-01-06 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0007_auto_20190106_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aisle_list',
            fields=[
                ('aisle_id', models.IntegerField(primary_key=True, serialize=False)),
                ('aisle', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_list',
            fields=[
                ('product_id', models.FloatField(default=999999, max_length=200, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('aisle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopapp.Aisle_list')),
            ],
        ),
    ]