# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from datetime import datetime, timedelta

from .models import ReservationInfo

def send_smag(error):
    pass

def checkReservationInfo():

    date_2_days_ago = datetime.now() - timedelta(days=2)
    tickets = ReservationInfo.objects.filter(is_paid=1, 
                                            status="BOOKED", 
                                            tickets_num=0,
                                            created__gte=date_2_days_ago)

    for reservation_info in tickets:
        msg = {
                'event': 'avia_ticket_error',
                'error': exception.get_message(),
                'data': {
                    'title': settings.TICKETING_ERROR_TXT.format(rcode=reservation_info.provider_code),
                    'reservation_code_id': reservation_info.id,
                    'is_paid': reservation_info.is_paid,
                    'payment_method': reservation_info.payment_method,
                    'payment_id': reservation_info.payment_id,
                    'provider_code': reservation_info.provider_code,
                    'created': timezone.now(),
                },
        }
        send_smag(msg)


