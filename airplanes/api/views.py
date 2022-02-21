from django.http import HttpRequest, HttpResponse

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
        base_consumption_nolog: float = airplane.airplane_id * \
            airplane.fuel_consumption_multiplier
        base_consumption: float = math.log(base_consumption_nolog, 10)
        # Calculating the total consumption by adding the passengers multiplier
        total_consumption: float = base_consumption + \
            (airplane.passengers *
             airplane.passenger_fuel_increase)
        # Calculating the fuel tank capacity
        fuel_tank_capacity: int = airplane.airplane_id * \
            airplane.fuel_tank_capacity_multiplier
        # Calculating max minutes that the airplane can fly
        max_minutes_flyable: float = fuel_tank_capacity / total_consumption

        return Response({
            'Totale Consumption Per Minute': total_consumption,
            'Max minutes this airplane can fly': max_minutes_flyable,
        })
