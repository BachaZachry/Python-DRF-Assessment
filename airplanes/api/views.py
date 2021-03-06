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


class AirplaneManagementBulk(generics.ListCreateAPIView):
    serializer_class = AirplaneSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Airplane.objects.all()

    def create(self, request: HttpRequest) -> HttpResponse:
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        try:
            entry_number: int = 0
            info = dict()
            self.perform_create(serializer)
            # Go through each entry and save it's information in info
            for data in serializer.data:
                entry_number += 1
                # Calculating the consumption per minute
                total_consumption = calculate_total_fuel_consumption(
                    data['airplane_id'], data['fuel_consumption_multiplier'], data['passengers'], data['passenger_fuel_increase'])
                # Calculating max minutes that the airplane can fly
                max_minutes_flyable = calculate_max_flyable_minutes(
                    data['airplane_id'], data['fuel_tank_capacity_multiplier'], total_consumption)
                info["Entry " + str(entry_number)] = {'Totale Consumption Per Minute': total_consumption,
                                                      'Max minutes this airplane can fly': max_minutes_flyable}
            # Returns the information for each entry
            return Response(info)
        except Exception:
            return Response({'message': 'Max Entries Reached'}, status=400)
