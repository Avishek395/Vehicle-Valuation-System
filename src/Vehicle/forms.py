# from django import forms
# from .models import Vehicle
# from datetime import datetime


# class VehicleValuationForm(forms.ModelForm):
#     START_YEAR = 1995
#     END_YEAR = datetime.now().year
#     YEAR_CHOICES = [(year, year)  for year in range(START_YEAR, END_YEAR + 1)]

#     Year = forms.ChoiceField(choices=YEAR_CHOICES)

#     class Meta:
#         model = Vehicle
#         fields = ('vehicle_brand', 'vehicle_name',
#                   'Year', 'Fuel', 'Distance_Travelled')

#         labels = {
#             'vehicle_brand': 'Vehicle Brand',
#             'vehicle_name': 'Vehicle Name',
#             'Year': 'Year',
#             'Fuel': 'Fuel',
#             'Distance_Travelled': 'Distance Travelled',
#         }
#         widgets = {
#             'vehicle_brand': forms.Select(attrs={'class': 'form-control'}),
#             'vehicle_name': forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
#             'Year': forms.Select(attrs={'class': 'form-control'}),
#             'Fuel': forms.Select(attrs={'class': 'form-control'}),
#             'Distance_Travelled': forms.NumberInput(attrs={'class': 'form-control'}),
#         }
