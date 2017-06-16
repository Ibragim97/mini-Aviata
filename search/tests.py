# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import ReservationInfo
from .utils import checkReservationInfo

# Create your tests here.

class ReservationInfoTest(TestCase):
    
    def test(self):
        from datetime import datetime, timedelta

        ReservationInfo(created=datetime.now()-timedelta(days=1)).save()
        ReservationInfo(created=datetime.now()-timedelta(days=2)).save()
        ReservationInfo(created=datetime.now()-timedelta(days=3)).save()
        ReservationInfo(created=datetime.now()-timedelta(days=4)).save()

        date_2_days_ago = datetime.now() - timedelta(days=2)
        tickets = ReservationInfo.objects.filter(tickets_num=0,
                                                created__gte=date_2_days_ago)

        self.assertIs(tickets.count(), 1)

