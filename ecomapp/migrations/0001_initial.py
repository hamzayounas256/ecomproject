# Generated by Django 4.1.13 on 2025-03-17 19:04

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=50, unique=True, verbose_name='Brand Name')),
                ('brand_index', models.IntegerField(default=0, help_text='Sorting index for brands', validators=[django.core.validators.MinValueValidator(0)])),
                ('brand_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10, verbose_name='Brand Status')),
                ('brand_img', models.ImageField(blank=True, null=True, upload_to='brand_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
        migrations.CreateModel(
            name='Capacity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('capacity_name', models.CharField(max_length=60, unique=True, verbose_name='Capacity Name')),
                ('capacity_index', models.IntegerField(default=0, help_text='Sorting index for brands', validators=[django.core.validators.MinValueValidator(0)])),
                ('capacity_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10, verbose_name='Status')),
                ('capacity_img', models.ImageField(blank=True, null=True, upload_to='capacity_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=60, unique=True, verbose_name='Category Name')),
                ('category_index', models.IntegerField(default=0, help_text='Sorting index for brands', validators=[django.core.validators.MinValueValidator(0)])),
                ('category_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10, verbose_name='Status')),
                ('category_img', models.ImageField(blank=True, null=True, upload_to='category_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=60, unique=True, verbose_name='Product Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Price')),
                ('stock_qnty', models.PositiveIntegerField(default=0, verbose_name='Stock Quantity')),
                ('product_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=8, verbose_name='Status')),
                ('product_img', models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='Product Image')),
                ('discount_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00')), django.core.validators.MaxValueValidator(Decimal('100.00'))], verbose_name='Discount Rate')),
                ('new_arrival', models.BooleanField(default=False, verbose_name='New Arrival')),
                ('most_viewed', models.BooleanField(default=False, verbose_name='Most Viewed')),
                ('top_selling', models.BooleanField(default=False, verbose_name='Top Selling')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.brand', verbose_name='Brand')),
                ('capacity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.capacity', verbose_name='Capacity')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.category', verbose_name='Category')),
            ],
        ),
    ]
