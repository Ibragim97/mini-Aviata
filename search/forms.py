from django import forms

from django.forms import CharField
import datetime
import re

from datetimewidget.widgets import DateWidget
from django_countries import countries

from .models import Airport

class FlightForm(forms.Form):
    origin_city = forms.CharField()
    dest_city = forms.CharField()
    date = forms.DateField(label="", widget=DateWidget(attrs={'required': True}, 
                                                        usel10n=True, bootstrap_version=3))

class BookingForm(forms.Form):
    CHOICES=[('M','M'),
            ('F','F')]
    sexField = forms.ChoiceField(label="", choices=CHOICES, widget=forms.RadioSelect())
    first_name = forms.CharField(label="First name", \
                                widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    second_name = forms.CharField(label="Second name", 
                                widget=forms.TextInput(attrs={'placeholder': 'Second name'}))
    birthDate = forms.DateField(label="Birth date", input_formats=('%d-%m-%Y',))
    
    citizenship = forms.ChoiceField(choices = list(countries))

    documentNum = forms.CharField(label="Document number")
    validTo = forms.DateField(label="Valid to", input_formats=('%d-%m-%Y',))
    idNum = forms.CharField(label="ID")
    
    phone_country = forms.CharField(label="Phone number")
    phone_number = forms.CharField(label="", min_length=10)
    email = forms.EmailField()

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']

        if not re.match("\([0-9]{3}\)[0-9]{3}-[0-9]{2}-[0-9]{2}", phone):
            raise forms.ValidationError("Incorrect phone number format")

        return phone
