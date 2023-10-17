from django.urls import path
from .views import prediction

app_name = "Predictionmodel"
urlpatterns = [
   
    path("prediction/", prediction, name="prediction"),
]
