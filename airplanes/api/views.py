from django.http import HttpRequest, HttpResponse
from airplanes.api.utils import calculate_max_flyable_minutes, calculate_total_fuel_consumption

from airplanes.models import Airplane
from .serializers import AirplaneSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
import math
from typing import TypeVar

AirplaneType = TypeVar('AirplaneType', bound=Airplane)


class AirplaneManagement(generics.GenericAPIView):
    serializer_class = AirplaneSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Airplane.objects.all()

    def post(self, request: HttpRequest) -> HttpResponse:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        airplane: AirplaneType = serializer.save()
        # Calculating the consumption per minute
        total_consumption = calculate_total_fuel_consumption(
            airplane.airplane_id, airplane.fuel_consumption_multiplier, airplane.passengers, airplane.passenger_fuel_increase)
        # Calculating max minutes that the airplane can fly
        max_minutes_flyable = calculate_max_flyable_minutes(
            airplane.airplane_id, airplane.fuel_tank_capacity_multiplier, total_consumption)

        return Response({
            'Totale Consumption Per Minute': total_consumption,
            'Max minutes this airplane can fly': max_minutes_flyable,
        })
