from django.urls import path, include
from rest_framework.routers import SimpleRouter

from aircraft.api import viewsets, views

router = SimpleRouter()
router.register(r'aircrafts', viewsets.AircraftViewset, basename='aircraft')


urlpatterns = [
    path('data/', views.DataView.as_view(), name='Load data from CSV'),
] + router.get_urls()
