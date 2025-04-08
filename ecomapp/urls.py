from django.urls import path
# from .views import get_capacity,post_capacity,update_capacity
from ecomapp.products.productcrud import post_product,get_product,get_all_product,update_product,delete_product
from ecomapp.products.brandcrud import get_brand,post_brand,update_brand,delete_brand
from ecomapp.products.categorycrud import get_category,post_category,update_category,delete_category
from ecomapp.products.capacitycrud import get_capacity,post_capacity,update_capacity,delete_capacity
from ecomapp.header.header_create import header_create
from ecomapp.header.header_read import header_read
from ecomapp.detail.detail_create import detail_create
from ecomapp.detail.detail_read import detail_read
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('brands/', get_brand),
    path('brands/create/', post_brand),
    path('brands/update/', update_brand),
    path('brands/delete/', delete_brand),
    
    path('categories/', get_category),
    path('categories/create/', post_category),
    path('categories/update/', update_category),
    path('categories/delete/', delete_category),
    
    path('capacities/', get_capacity),
    path('capacities/create/', post_capacity),
    path('capacities/update/', update_capacity),
    path('capacities/delete/', delete_capacity),
    
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