from django.urls import path
# from .views import get_capacity,post_capacity,update_capacity
from ecomapp.products.productcrud import post_product,get_product,update_product,delete_product
from ecomapp.products.brandcrud import get_brand,post_brand,update_brand,delete_brand
from ecomapp.products.categorycrud import get_category,post_category,update_category,delete_category
from ecomapp.products.capacitycrud import get_capacity,post_capacity,update_capacity,delete_capacity
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
    path('products/create/', post_product),
    path('products/update/',update_product),
    path('products/delete/',delete_product),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)