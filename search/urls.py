from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ajax/get_cities/$', views.get_cities, name='get_cities'),
    url(r'^ajax/check_cities/', views.check_cities, name='check_cities'),
    url(r'^results/', views.search, name='results'),
    url(r'^booking/(?P<flight_id>[0-9]+)/$', views.booking, name='booking'),
]
