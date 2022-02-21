import pytest
import pytest_django
from rest_framework.test import APIClient
from airplanes.models import Airplane


class TestAirplane:
    def setup(self):
        self.client = APIClient()

    @pytest.mark.django_db()
    @pytest.mark.parametrize('airplane_id,passengers,status,consumption,max_minutes', [
        [2, 1000, 200, 2.2, 181]
    ])
    def test_add_airplane(self, airplane_id, passengers, status, consumption, max_minutes):
        req = self.client.post(
            '/airplane/add/', {'airplane_id': airplane_id, 'passengers': passengers})
        print(req.data)
        assert req.status_code == status
        assert req.data['Totale Consumption Per Minute'] >= consumption
        assert req.data['Max minutes this airplane can fly'] >= max_minutes

    @pytest.mark.django_db()
    @pytest.mark.parametrize('airplane_id,passengers,status', [
        [2, 1000, 400],
    ])
    def test_max_airplanes(self, airplane_id, passengers, status):
        for i in range(10):
            self.client.post(
                '/airplane/add/', {'airplane_id': airplane_id, 'passengers': passengers})

        req = self.client.post(
            '/airplane/add/', {'airplane_id': airplane_id, 'passengers': passengers})

        assert req.status_code == status

    @pytest.mark.django_db()
    @pytest.mark.parametrize('airplane_id,passengers,status', [
        [2, 1000, 200],
    ])
    def test_bulk_entry(self, airplane_id, passengers, status):
        req = self.client.post(
            '/airplane/addbulk/', [{'airplane_id': airplane_id, 'passengers': passengers}, {'airplane_id': airplane_id, 'passengers': passengers}], format='json')

        assert req.status_code == status
        assert Airplane.objects.count() == 2

    @pytest.mark.parametrize('airplane_id,passengers,status', [
        [2, 1000, 400],
    ])
    def test_bulk_entry_limit_reached(self, airplane_id, passengers, status):
        req = self.client.post(
            '/airplane/addbulk/', [
                {'airplane_id': airplane_id, 'passengers': passengers},
                {'airplane_id': airplane_id, 'passengers': passengers},
                {'airplane_id': airplane_id, 'passengers': passengers},
                {'airplane_id': airplane_id, 'passengers': passengers},
                {'airplane_id': airplane_id, 'passengers': passengers},
                {'airplane_id': airplane_id, 'passengers': passengers},
                {'airplane_id': airplane_id, 'passengers': passengers},
                {'airplane_id': airplane_id, 'passengers': passengers},
                {'airplane_id': airplane_id, 'passengers': passengers},
                {'airplane_id': airplane_id, 'passengers': passengers},
                {'airplane_id': airplane_id, 'passengers': passengers},
                {'airplane_id': airplane_id, 'passengers': passengers},
            ], format='json')

        assert req.status_code == status
