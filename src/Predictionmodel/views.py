import pickle
import pandas as pd
from django.shortcuts import render
from vehicleform.forms import VehicleForm
import random


with open("prediction_model.pkl", "rb") as f:
    model = pickle.load(f)


import pandas as pd

from vehicleform.models import Vehicle
from django.http import JsonResponse
from django.shortcuts import render

import pandas as pd
from django.shortcuts import render

from vehicleform.forms import VehicleForm


def prediction(request):
    context = {}

    if request.method == "POST":
        form = VehicleForm(request.POST)

        if form.is_valid():

            brand = form.cleaned_data['vehicle_brand']
            vehicle = form.cleaned_data['vehicle_name']
            year = form.cleaned_data['year']
            distance_travelled = form.cleaned_data['distance_travelled']
            fuel = form.cleaned_data['fuel']

            data = pd.DataFrame({
                "name": [str(vehicle)],
                "company": [str(brand)],
                "year": [year],
                "kms_driven": [distance_travelled],
                "fuel_type": [fuel],
            })

            prediction = model.predict(data)[0]
            price = prediction if prediction > 0 else 0
            price *= 3.2
            print(price)
            finalPrice = price
            if finalPrice == 0:
                print("No price")
                context["price"] = " The data can't be found "
                context["form"] = form

                return render(request, 'valu_form.html', context)

            context["form"] = form
            context["price"] = finalPrice

            return render(request, 'valu_form.html', context)

    else:
        form = VehicleForm()

    context["form"] = form
    return render(request, 'valu_form.html', context)
