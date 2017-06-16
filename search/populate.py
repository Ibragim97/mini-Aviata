from .models import Airport, Flight
import datetime
import random

def populateAirport():
    Airport.create("Atlanta", "Hartsfield Jackson Atlanta International", "ATL").save()
    Airport.create("Beijing", "Beijing Capital International", "PEK").save()
    
    Airport.create("Dubai", "Dubai International", "DXB").save()
    Airport.create("Chicago", "Chicago O Hare International", "ORD").save()
    Airport.create("Tokyo", "Tokyo International", "HND").save()
    Airport.create("London", "London Heathrow", "LHR").save()
    Airport.create("Los Angeles", "Los Angeles International", "LAX").save()
    Airport.create("Honk Kong", "Hong Kong International", "HKG").save()
    Airport.create("Paris", "Charles de Gaulle International", "CDG").save()
    Airport.create("Dallas", "Dallas Fort Worth International", "DFW").save()
    Airport.create("Istanbul", "Ataturk International", "IST").save()
    Airport.create("Frankfurt", "Frankfurt am Main International", "FRA").save()
    Airport.create("Shanghai", "Shanghai Pudong International", "PVG").save()
    Airport.create("Amsterdam", "Amsterdam Schiphol", "AMS").save()
    Airport.create("New Your", "John F Kennedy International", "JFK").save()
    Airport.create("Singaport", "Singapore Changi International", "SIN").save()
    Airport.create("Guangzhou", "Guangzhou Baiyun International", "CAN").save()
    Airport.create("Jakarta", "Soekarno-Hatta International", "CGK").save()
    Airport.create("Almaty", "Almaty", "ALA").save()
    Airport.create("Astana", "Astana", "TSE").save()

def populateFlight():

    airlines = ["Emirates", "Singapore Airlines", "Turkish Airlines", "EVA Air",
                "Lufthansa", "Hainan Airlines", "Asiana", "Bangkok Airways",
                "Air Astana", "KLM"]


    for a in Airport.objects.all():
        if a.airport_code != "ATL":
            for b in Airport.objects.all():
                if a != b:
                    for i in range(1, 31):
                        for j in range(2):
                            time1 = random.randint(0, 23)
                            time2 = random.randint(0, 23)
                            day = i
                            if time1 >= time2: day += 1
                            dept_date = datetime.datetime(2017, 5, i, time1)
                            arr_date = datetime.datetime(2017, 5, day, time2)
                            airline = random.choice(airlines)
                            Flight.create(a, b, airline, dept_date, arr_date).save()


