# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone



# Create your models here.

class Airport(models.Model):
	airport_city = models.CharField(default="city", max_length=200)
	airport_name = models.CharField(max_length=200)
	airport_code = models.CharField(max_length=200)

	@classmethod
	def create(cls, airport_city, airport_name, airport_code):
		return cls(airport_city=airport_city, airport_name=airport_name, airport_code=airport_code)

	def __str__(self):
		return "%s     (%s)" % (self.airport_city, self.airport_code)

class Flight(models.Model):
    origin_city = models.ForeignKey(Airport, related_name="origin_city", on_delete=models.CASCADE)
    dest_city = models.ForeignKey(Airport, related_name="dest_city", on_delete=models.CASCADE)
    airline_name = models.CharField(max_length=200)
    dept_datetime = models.DateTimeField('depature datetime')
    arr_datetime = models.DateTimeField('arrival datetime') 

    @classmethod
    def create(cls, origin_city, dest_city, airline, dept_date, arr_date):
        return cls(origin_city=origin_city, dest_city=dest_city, airline_name=airline,
                    dept_datetime=dept_date, arr_datetime=arr_date)

    def __str__(self):
        return "From: %s To: %s Airline: %s Dept: %s Arr: %s" % \
                                                        (self.origin_city.airport_city,
                                                        self.dest_city.airport_city, 
                                                        self.airline_name,
                                                        str(self.dept_datetime),
                                                        str(self.arr_datetime))

class Passenger(models.Model):
    sexField = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    second_name = models.CharField(max_length=200, null=True)
    birthDate = models.DateField(null=True)
    citizenship = models.CharField(max_length=200, null=True)
    documentNum = models.CharField(max_length=200, null=True)
    validTo = models.DateField(null=True)
    idNum = models.CharField(max_length=200, null=True)
    phone_country = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    email = models.EmailField(primary_key=True)
    flights = models.ManyToManyField(Flight)

    def __str__(self):
        return "First_name: %s Email:%s" % (self.first_name, self.email)


class ReservationInfo(models.Model):
    PAYMENT = [
        (0, ""),
        (1, "Да"),
    ]

    is_paid = models.IntegerField(default=0, verbose_name=u'Оплата', choices=PAYMENT)
    tickets_num = models.PositiveSmallIntegerField(default=0, verbose_name=u'Билеты')
    tickets_txt = models.CharField(max_length=255, default='', verbose_name=u'Номера билетов', blank=True)
    status = models.CharField(max_length=15, verbose_name=u'Статус', default='BOOKED', blank=True)
    payment_method = models.CharField(max_length=50, verbose_name=u'Метод оплаты', default='', blank=True, null=True)
    payment_id = models.CharField(max_length=50, default='', blank=True, verbose_name=u'ID оплаты')
    provider_code = models.CharField(max_length=20, verbose_name=u'Код брони', default='', db_index=True)
    created = models.DateTimeField(
            default=timezone.now,
            verbose_name=u'Дата создания',
            db_index=True
        )