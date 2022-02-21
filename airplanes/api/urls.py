from django.urls import path, include
from .views import AirplaneManagement, AirplaneManagementBulk

urlpatterns = [
    path('add/', AirplaneManagement.as_view(), name="Add Airplane"),
    path('addbulk/', AirplaneManagementBulk.as_view(), name="Add Bulk Airplanes"),
]
