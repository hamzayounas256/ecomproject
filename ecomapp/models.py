from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

class Brand(models.Model):
    class BrandStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        
    id = models.AutoField(primary_key=True)
    
    brand_name = models.CharField(max_length=50, unique=True, verbose_name="Brand Name")
    
    brand_index = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0)], 
        help_text="Sorting index for brands"
    )
    
    brand_status = models.CharField(
        max_length=10, 
        choices=BrandStatus.choices,
        default=BrandStatus.ACTIVE, 
        verbose_name="Brand Status"
    )
    
    brand_img = models.ImageField(upload_to="brand_images/", null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"{self.brand_name} ({self.brand_status})"
    
    
class Category(models.Model):
    class CategoryStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    id = models.AutoField(primary_key=True)
    
    category_name = models.CharField(max_length=60, unique=True, verbose_name="Category Name")
    
    category_index = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0)], 
        help_text="Sorting index for brands"
    )
    
    category_status = models.CharField(
        max_length=10, 
        choices=CategoryStatus.choices,
        default=CategoryStatus.ACTIVE, 
        verbose_name="Status"
    )
    
    category_img = models.ImageField(upload_to="category_images/", null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"{self.category_name} ({self.category_status})"


class Capacity(models.Model):
    class CapacityStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    id = models.AutoField(primary_key=True)
    
    capacity_name = models.CharField(max_length=60, unique=True, verbose_name="Capacity Name")
    
    capacity_index = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0)], 
        help_text="Sorting index for brands"
    )
    
    capacity_status = models.CharField(
        max_length=10, 
        choices=CapacityStatus.choices,
        default=CapacityStatus.ACTIVE, 
        verbose_name="Status"
    )
    
    capacity_img = models.ImageField(upload_to="capacity_images/", null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"{self.capacity_name} ({self.capacity_status})"
    
    
class Products(models.Model):
    class ProductStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    id = models.AutoField(primary_key=True)
    
    product_name = models.CharField(
        max_length=60,
        unique=True,
        verbose_name="Product Name"
    )
    
    description = models.TextField(verbose_name="Description")
    
    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name="Price"
    )
    
    stock_qnty = models.PositiveIntegerField(
        default=0,
        verbose_name="Stock Quantity"
    )
    
    product_status = models.CharField(
        max_length=8,
        choices=ProductStatus.choices,
        default=ProductStatus.ACTIVE,
        verbose_name="Status"
    )
    
    product_img = models.ImageField(
        upload_to='product_images/',
        null=True, 
        blank=True,
        verbose_name="Product Image"
    )
    
    discount_rate = models.DecimalField(
        max_digits=5, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('100.00'))],
        null=True, blank=True, verbose_name="Discount Rate"
    )
    
    new_arrival = models.BooleanField(default=False, verbose_name="New Arrival")
    
    most_viewed = models.BooleanField(default=False, verbose_name="Most Viewed")
    
    top_selling = models.BooleanField(default=False, verbose_name="Top Selling")
    
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.CASCADE,
        verbose_name="Brand"
    )
    
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name="Category"
    )
    
    capacity = models.ForeignKey(
        'Capacity',
        on_delete=models.CASCADE,
        verbose_name="Capacity"
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.product_name
    