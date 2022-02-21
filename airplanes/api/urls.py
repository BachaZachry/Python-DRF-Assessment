from django.urls import path, include
from .views import AirplaneManagement

urlpatterns = [
    path('add/', AirplaneManagement.as_view(), name="Add airplane")
]
