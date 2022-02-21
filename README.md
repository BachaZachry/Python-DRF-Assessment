# Python (DRF) Assessment

## About:

This assessment concerns an airline company, the user can add up to 10 airplanes with further information and will receive a response that includes both its fuel consumption per minute as well as the maximum number of flyable minutes.

## Installation:

```
git clone https://github.com/BachaZachry/Python-DRF-Assessment.git
cd Python-DRF-Assessment
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Usage:

The user is required to send the airplane_id and passengers (number of passengers) and has other optional fields.

```
{
    "airplane_id": Positive number,
    "passengers": Positive number,
}
```

The optional fields are the following:

- fuel_tank_capacity_multiplier : to override the default value of the fuel tank capacity multiplier.
- fuel_consumption_multiplier : to override the default value of the fuel consumption multiplier.
- passenger_fuel_increase : to override the default value of the fuel consumption increase per passenger.
