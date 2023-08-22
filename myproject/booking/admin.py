from django.contrib import admin
from booking.models import UserDetails
from booking.forms import UserModelForm 


# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    fields = ['Name', 'Service', 'Time', 'Day', 'Email']

admin.site.register(UserDetails, BookingAdmin)