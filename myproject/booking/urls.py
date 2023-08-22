from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
 path('display/', views.userDetails, name='userDetails'),   
 path('booking/bookdetails/', views.bookdetails, name='bookdetails'),
 path('book/<int:id>', views.delete, name='delete'),
 path('products/', views.products, name='products'),
]
