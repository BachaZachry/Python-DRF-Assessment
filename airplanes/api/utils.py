import math


def calculate_total_fuel_consumption(airplane_id: int, fuel_consumption_multiplier: float, passengers: int, passenger_fuel_increase: float) -> float:
    # Calculating the consumption per minute
    base_consumption_nolog: float = airplane_id * \
        fuel_consumption_multiplier
    base_consumption: float = math.log(base_consumption_nolog, 10)
    # Calculating the total consumption by adding the passengers multiplier
    total_consumption: float = base_consumption + \
        (passengers *
         passenger_fuel_increase)

    return total_consumption


def calculate_max_flyable_minutes(airplane_id: int, fuel_tank_capacity_multiplier: int, total_consumption: float) -> float:
    fuel_tank_capacity: int = airplane_id * \
        fuel_tank_capacity_multiplier
    # Calculating max minutes that the airplane can fly
    max_minutes_flyable: float = fuel_tank_capacity / total_consumption

    return max_minutes_flyable
