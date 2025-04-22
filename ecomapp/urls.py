from django.urls import path

from ecomapp.auth.login import login
from ecomapp.auth.logout import logout
from ecomapp.auth.auth_update import auth_update
from ecomapp.auth.register import register, verify_otp,resend_otp

from ecomapp.products.product_create import product_create
from ecomapp.products.product_read import product_read, product_read_all
from ecomapp.products.product_update import product_update
from ecomapp.products.product_delete import product_delete

from ecomapp.brands.brand_create import brand_create
from ecomapp.brands.brand_read import brand_read,brand_read_all
from ecomapp.brands.brand_update import brand_update
from ecomapp.brands.brand_delete import brand_delete

from ecomapp.capacity.capacity_create import capacity_create
from ecomapp.capacity.capacity_read import capacity_read,capacity_read_all
from ecomapp.capacity.capacity_update import capacity_update
from ecomapp.capacity.capacity_delete import capacity_delete

from ecomapp.category.category_create import category_create
from ecomapp.category.category_read import category_read,category_read_all
from ecomapp.category.category_update import category_update
from ecomapp.category.category_delete import category_delete

from ecomapp.header.header_create import header_create
from ecomapp.header.header_read import header_read

from ecomapp.detail.detail_create import detail_create
from ecomapp.detail.detail_read import detail_read
from ecomapp.detail.detail_delete import detail_delete

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('login/', login),
    path('logout/', logout),
    path('update/', auth_update),
    path('register/', register),
    path('verify/', verify_otp),
    path('resend/', resend_otp),
    
    path('brands/', brand_read),
    path('brands/all', brand_read_all),
    path('brands/create/', brand_create),
    path('brands/update/', brand_update),
    path('brands/delete/', brand_delete),
    
    path('categories/', category_read),
    path('categories/all', category_read_all),
    path('categories/create/', category_create),
    path('categories/update/', category_update),
    path('categories/delete/', category_delete),
    
    path('capacities/', capacity_read),
    path('capacities/all', capacity_read_all),
    path('capacities/create/', capacity_create),
    path('capacities/update/', capacity_update),
    path('capacities/delete/', capacity_delete),
    
    path('products/', product_read),
    path('products/all', product_read_all),
    path('products/create/', product_create),
    path('products/update/',product_update),
    path('products/delete/',product_delete),
    
    path('headers/', header_read),
    path('headers/create/', header_create),
    
    
    path('details/', detail_read),
    path('details/create/', detail_create),
    path('details/delete/', detail_delete),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)