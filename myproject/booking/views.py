#
from django.shortcuts import render, redirect
from booking.models import UserDetails
from django.shortcuts import render
from .forms import UserModelForm


from django.contrib.auth.decorators import login_required

# Create your views here.


# add to your views
# Display the (display0.html) thank you page 

def userDetails(request):

    form = UserModelForm
    args = {}
    if request.method == 'POST':
        form = UserModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            users = UserDetails.objects.all()

            return render(request, 'booking/display0.html', {'users': users})


    else:
        form_class = UserModelForm
    args['form'] = form

    return render(request, 'booking/userdetails.html', args)

@login_required
def bookdetails(request):
    bookdetails = UserDetails.objects.all()
    context = {
        'bookdetails':  bookdetails,
    }
    return render(request, 'service/adminpanel2.html', context)

def delete(request, id):
  book = UserDetails.objects.get(id=id)
  context = {
    'book':  book,
  }
  if request.method == 'POST':
    book.delete()
    return redirect('/booking/bookdetails')
  return render(request, 'booking/delete.html', context)

@login_required
def products(request):
  products = Product.objects.all()
  context = {
    'products': products,
  }
  return render(request, 'service/adminpanel2.html', context)
  


