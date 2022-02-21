from airplanes.models import Airplane
from rest_framework import serializers


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ['airplane_id', 'passengers', 'fuel_tank_capacity_multiplier',
                  'fuel_consumption_multiplier', 'passenger_fuel_increase']
