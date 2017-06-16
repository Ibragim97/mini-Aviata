# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
    

from datetime import datetime

from .models import Airport, Flight, Passenger
from .forms import FlightForm, BookingForm



def index(request):
    form = FlightForm(initial={'date': timezone.now()})

    return render(request, 'search/index.html', {'form': form})

def get_cities(request):
    data = {
        'cities': [x.airport_city for x in Airport.objects.all()]
    }
    return JsonResponse(data)

def check_cities(request):
    data = request.GET
    
    try:
        Airport.objects.get(airport_city=data['origin'])
        try:
            Airport.objects.get(airport_city=data['dest'])  
            response = {'valid': True}
        except Airport.DoesNotExist: 
            response = {'notValid': "There is no flights to this city"}
    except Airport.DoesNotExist:
        response = {'notValid': "There is no flights from this city"}
    
    return JsonResponse(response)


def search(request):
    data = request.POST

    try:
        date = datetime.strptime(data["date"], "%Y-%m-%d")
        origin_city = Airport.objects.get(airport_city=data["origin_city"])
        dest_city = Airport.objects.get(airport_city=data["dest_city"])
    except:
        error = "Error getting the airports"
        content = {
            'error': error
        }
    else:
        content = {
            'from': origin_city.airport_city,
            'to': dest_city.airport_city,
            'when': (date.date()),   
            'filter': Flight.objects.filter(
                origin_city__airport_code=origin_city.airport_code,
                dest_city__airport_code=dest_city.airport_code,
                dept_datetime__date=date
            ),  
        }
        
    return render(request, 'search/results.html', content)

def registerUser(data, flight_id):
    passenger = Passenger(sexField=data['sexField'],
                        first_name=data['first_name'],
                        second_name=data['second_name'],
                        birthDate=datetime.strptime(data["birthDate"], "%d-%m-%Y"),        
                        citizenship=data['citizenship'],
                        documentNum=data['documentNum'],
                        validTo=datetime.strptime(data["validTo"], "%d-%m-%Y"),            
                        idNum=data['idNum'],
                        phone_country=data['phone_country'],
                        phone_number=data['phone_number'],
                        email=data['email'])
    try:
        Passenger.objects.get(email=passenger.email)
        message = "Passenger already exists."
    except:
        message = "New passenger created."
            
    try:
        f = Flight.objects.get(pk=flight_id)
        passenger.save()
        passenger.flights.add(f)
    except:
        message = "Error... Flight does not exist."
    
    return message


def booking(request, flight_id):

    if request.POST:
        form = BookingForm(request.POST)
        if form.is_valid(): 
            message = registerUser(request.POST, flight_id)
            error = None 
            if "Error" in message:
                error = message
            content = {
                'message': message,
                'error': error,
            }
            return render(request, 'search/return_page.html', content)
    else:
        form = BookingForm(initial={'citizenship': "KZ"})

    content = {
        'form': form,
    }
    
    return render(request, 'search/booking.html', content)
