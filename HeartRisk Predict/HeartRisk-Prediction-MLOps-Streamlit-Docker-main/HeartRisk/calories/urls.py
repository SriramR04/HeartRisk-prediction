from django.urls import path
from backendapplication.views import predict_calories

urlpatterns = [
    path('', predict_calories.as_view(), name='predict_calories'),
]
