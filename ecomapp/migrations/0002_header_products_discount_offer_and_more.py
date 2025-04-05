# Generated by Django 4.1.13 on 2025-04-05 06:42

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('order_no', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(auto_now_add=True, verbose_name='Order Date')),
                ('order_time', models.TimeField(auto_now_add=True, verbose_name='Order Time')),
                ('cust_name', models.CharField(max_length=60, verbose_name='Customer Name')),
                ('cust_address', models.CharField(max_length=100, verbose_name='Customer Address')),
                ('cust_phone_no', models.CharField(max_length=13, verbose_name='Phone Number')),
                ('cust_email', models.EmailField(max_length=50, verbose_name='Email')),
                ('cust_nic', models.CharField(max_length=15, verbose_name='NIC')),
                ('total_qnty', models.PositiveIntegerField(default=0, verbose_name='Total Quantity')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Total Amount')),
                ('total_sale_amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Total Sale Amount')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='discount_offer',
            field=models.BooleanField(default=False, verbose_name='Discount Offer'),
        ),
        migrations.AlterField(
            model_name='products',
            name='discount_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Discount Rate'),
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=60, verbose_name='Product Name')),
                ('product_rate', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Product Rate')),
                ('product_qnty', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Quantity')),
                ('product_amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Amount')),
                ('product_sale_rate', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Sale Rate')),
                ('product_sale_amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Sale Amount')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('order_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.header', verbose_name='Order No')),
                ('product_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.products', verbose_name='Product')),
            ],
        ),
    ]
