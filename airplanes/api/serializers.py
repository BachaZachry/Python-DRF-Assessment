from airplanes.models import Airplane
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class BulkSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        count = Airplane.objects.count() + len(validated_data)

        if (count >= 10):
            raise ValidationError("Max Entries Reached")
        else:
            data = [Airplane(**item) for item in validated_data]
            return Airplane.objects.bulk_create(data)


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ['airplane_id', 'passengers', 'fuel_tank_capacity_multiplier',
                  'fuel_consumption_multiplier', 'passenger_fuel_increase']
        list_serializer_class = BulkSerializer
