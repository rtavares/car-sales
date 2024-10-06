import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from car.models import Car

pytestmark = pytest.mark.django_db  # This is put here so that we can save to the database otherwise it will fail because tests are not written to the database.


class TestCarModels(APITestCase):
    def setUp(self):
        # Create a User instance
        user = User.objects.create_user("user", "<EMAIL>", "password")
        # Create a car instance
        car_data = {
            "owner": user,
            "model": "Panda 7",
            "brand": "Fiat",
            "year": 1983,
            "color": "Blue",
            "seats": 4,
            "type": "Familiar",
            "price": 1200,
            "publishing_date": "2024-10-05T15:54:41Z",
        }
        car_data["display"] = True
        self.car = Car.objects.create(**car_data)

        car_data["display"] = False
        self.car = Car.objects.create(**car_data)

        # get auth token
        response = self.client.post(
            reverse("login"), {"username": "user", "password": "password"}
        )
        self.token = response.data["token"]

    def test_non_authorized_user_gets_access_denied(self):
        """Do not supply Auth token"""
        response = self.client.get(reverse("car-list"))
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_car_creation(self):
        """Perform an authorized access"""
        response = self.client.get(
            reverse("car-list"), format="json", HTTP_AUTHORIZATION="Token " + self.token
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data != {}
        assert Car.objects.count() == 2  # Include an undisplayed car
        assert len(response.data) == 1  # Only the display==True car should be displayed
        assert (
            response.data[0]["id"] == 1
        )  # The display=True car created is the first one
