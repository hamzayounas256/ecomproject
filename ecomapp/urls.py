from django.urls import path
# from .views import get_capacity,post_capacity,update_capacity
from ecomapp.products.productcrud import post_product,get_product,get_all_product,update_product,delete_product

from ecomapp.brands.brand_create import brand_create
from ecomapp.brands.brand_read import brand_read,brand_read_all
from ecomapp.brands.brand_update import brand_update
from ecomapp.brands.brand_delete import brand_delete

from ecomapp.capacity.capacity_create import capacity_create
from ecomapp.capacity.capacity_read import capacity_read,capacity_read_all
from ecomapp.capacity.capacity_update import capacity_update
from ecomapp.capacity.capacity_delete import capacity_delete


from ecomapp.category.categorycrud import get_category,post_category,update_category,delete_category

from ecomapp.header.header_create import header_create
from ecomapp.header.header_read import header_read
from ecomapp.detail.detail_create import detail_create
from ecomapp.detail.detail_read import detail_read
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('brands/', brand_read),
    path('brands/all', brand_read_all),
    path('brands/create/', brand_create),
    path('brands/update/', brand_update),
    path('brands/delete/', brand_delete),
    
    path('categories/', get_category),
    path('categories/create/', post_category),
    path('categories/update/', update_category),
    path('categories/delete/', delete_category),
    
    path('capacities/', capacity_read),
    path('capacities/all', capacity_read_all),
    path('capacities/create/', capacity_create),
    path('capacities/update/', capacity_update),
    path('capacities/delete/', capacity_delete),
    
    path('products/', get_product),
    path('products/all', get_all_product),
    path('products/create/', post_product),
    path('products/update/',update_product),
    path('products/delete/',delete_product),
    
    path('headers/', header_read),
    path('headers/create/', header_create),
    
    
    path('details/', detail_read),
    path('details/create/', detail_create)
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)