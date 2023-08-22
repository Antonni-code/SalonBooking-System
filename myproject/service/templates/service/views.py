from django.shortcuts import render, redirect
from contextlib import redirect_stderr
from http.client import HTTPResponse
from django.http import HttpResponse
from .models import Product

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
  return render(request, 'myapp/homepage.html')

def booking(request):
  return render(request, 'myapp/bookingsalon.html')

def about(request):
  return render(request, 'myapp/About.html')

def services(request):
  return render(request, 'myapp/service.html')

def contact(request):
  return render(request, 'myapp/Contact.html')

def adminpanel1(request):
  return render(request, 'myapp/adminpanel1.html')

def adminpanel2(request):
  return render(request, 'myapp/Adminpanel2.html')

def appointment(request):
  return render(request, 'myapp/appointment.html')

@login_required
def products(request):
  products = Product.objects.all()
  context = {
    'products': products,
  }
  return render(request, 'myapp/adminpanel1.html', context)
  
@login_required
def product_details(request, id):
  product = Product.objects.get(id=id)
  context = {
    'product': product,
  }
  return render(request, 'myapp/details.html', context)

@login_required
def add_product(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    price = request.POST.get('price')
    description = request.POST.get('description')
    product = Product(name=name, price=price, description=description)
    product.save()
  return render(request, 'myapp/addproduct.html')

def update_product(request, id):
  product = Product.objects.get(id=id)
  if request.method == 'POST':
    product.name = request.POST.get('name')
    product.price = request.POST.get('price')
    product.description = request.POST.get('description')
    product.save()
    return redirect('/myapp/products')
  context = {
    'product': product,
  }
  return render(request, 'myapp/updateproduct.html', context)

def delete_product(request, id):
  product = Product.objects.get(id=id)
  context = {
    'product': product,
  }
  if request.method == 'POST':
    product.delete()
    return redirect('/myapp/products')
  return render(request, 'myapp/deleteproduct.html', context)
  
