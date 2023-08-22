from django.contrib import admin
from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
  path('products/', views.products, name='products'),
  path('products/<int:id>', views.product_details, name='product_details'),
  path('products/add', views.add_product, name='add_product'),
  path('products/update/<int:id>', views.update_product, name='update_product'),
  path('products/delete/<int:id>', views.delete_product, name='delete_product'),
  path('booking/', views.booking, name='booking'),
  path('about/', views.about, name='about'),
  path('services/', views.services, name='services'),
  path('contact/', views.contact, name='contact'),
  path('adminpanel1/', views.adminpanel1, name='adminpanel1'),
  path('adminpanel2/', views.adminpanel2, name='adminpanel2'),
  path('appointment/', views.appointment, name='appointment'),
  path('', views.index, name='service'),
]