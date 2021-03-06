# Generated by Django 3.0.2 on 2020-05-29 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0003_auto_20200529_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.CharField(max_length=100)),
                ('product_sku', models.IntegerField(default=1)),
                ('product_price', models.IntegerField(default=0)),
                ('out_of_stock', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=100)),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.Supplier')),
            ],
        ),
    ]
