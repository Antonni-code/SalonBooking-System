from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as authentication_views

app_name = 'users'

urlpatterns = [
  path('login/', authentication_views.LoginView.as_view(template_name='users/admin.html'), name='login'),
  path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]