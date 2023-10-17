
from django.urls import path
from .views import vehicle_selection, get_vehicles

app_name = 'vehicleform'
urlpatterns = [

    path('valuation/', vehicle_selection, name='valuation_form'),
    path('get_vehicles/<str:brand_name>/', get_vehicles, name='get_vehicles'),


]
