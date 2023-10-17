
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Vehicle, Brand
from .forms import VehicleForm


from django.http import JsonResponse


from django.http import JsonResponse


def get_vehicles(request, brand_name):

    brand = Brand.objects.get(name=brand_name)
    vehicles = Vehicle.objects.filter(vehicle_brand=brand)

    
    vehicles_list = [
        {'id': vehicle.id, 'vehicle_name': vehicle.vehicle_name} for vehicle in vehicles]

    return JsonResponse(vehicles_list, safe=False)

@login_required
def vehicle_selection(request):
    form = VehicleForm()
    return render(request, 'valu_form.html', {'form': form})
