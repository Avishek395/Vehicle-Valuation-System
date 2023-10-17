from django import forms
from .models import Brand, Vehicle
from django.core.validators import MinValueValidator, MaxValueValidator


class VehicleForm(forms.Form):
    vehicle_brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(), empty_label="Select a Brand", to_field_name="name")
    vehicle_name = forms.ModelChoiceField(
        queryset=Vehicle.objects.all(), empty_label="Select a Vehicle", to_field_name="vehicle_name")
    year = forms.IntegerField(
        validators=[MinValueValidator(
            2003, message="Year must be equal to or greater than 2000"),
            MaxValueValidator(
                2023, message="Year must be equal to or less  than 2023")
        ]
    )
    distance_travelled = forms.IntegerField()
    fuel = forms.ChoiceField(
        choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel')])
