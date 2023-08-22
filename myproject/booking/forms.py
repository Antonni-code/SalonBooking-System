from django.forms import ModelForm
from .models import UserDetails
from django import forms
#
from django.forms import ModelForm
from django import forms
from unicodedata import normalize



class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['Name', 'Service', 'Day', 'Time',  'Email']

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Service': forms.Select(attrs={'class': 'form-control'}),
            'Day': forms.Select(attrs={'class': 'form-control'}),
            'Time': forms.Select(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_BookingName(self): 
        Name = self.cleaned_data.get('Name')
        Service = self.cleaned_data.get('Service')

        if (Name == ""):
            raise ValidationError('The Name field cannot be left blank.')
            
        for instance in UserDetails.objects.all():
            if instance.Service == Service:
                if instance.Name == Name:
                        raise ValidationError(Name + ' already has a booking.')
        return Name

    def clean_Date(self):
            Email = self.cleaned_data.get('Email')
            Day = self.cleaned_data.get('Day')
            Time = self.cleaned_data.get('Time')
        
            if (Day == ""):
                raise ValidationError("Please select a day.")

            if (Time == ""):
                raise ValidationError("Please select a timeslot.")
            
            if (Email == ""):
                raise ValidationError("Please enter email.")


            for instance in UserDetails.objects.all():
                if instance.Email == Email:
                    if instance.Day == Day:
                        if instance.Time == Time:
                            raise ValidationError('This info is already booked at that time, please change Day or try another time.')
            return Email
        
        