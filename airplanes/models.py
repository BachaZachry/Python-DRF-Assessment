from django.db import models
from django.core.validators import MinValueValidator
from rest_framework.exceptions import ValidationError


class Airplane(models.Model):
    airplane_id = models.PositiveIntegerField(null=False)
    passengers = models.PositiveIntegerField(null=False)
    fuel_tank_capacity_multiplier = models.PositiveIntegerField(default=200)
    fuel_consumption_multiplier = models.FloatField(
        validators=[MinValueValidator(0.0)], default=0.8)
    passenger_fuel_increase = models.FloatField(
        validators=[MinValueValidator(0.0)], default=0.002)

    def save(self, *args, **kwargs):
        if (Airplane.objects.count() >= 10):
            raise ValidationError(
                'You can not add another airplane instance, limit reached.')
        else:
            super(Airplane, self).save(*args, **kwargs)
