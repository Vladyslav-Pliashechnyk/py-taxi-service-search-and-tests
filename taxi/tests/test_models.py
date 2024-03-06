from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Car, Manufacturer


class ManufacturerModelTest(TestCase):
    def test_manufacturer_str(self) -> None:
        manufacturer = Manufacturer.objects.create(
            name="Audi",
            country="Germany"
        )
        self.assertEqual(
            str(manufacturer),
            f"{manufacturer.name} {manufacturer.country}"
        )


class DriverModelTest(TestCase):
    def setUp(self) -> None:
        self.driver = get_user_model().objects.create_user(
            username="schum_01",
            first_name="Michael",
            last_name="Schumacher",
            password="qwerty",
            license_number="ABC12345",
        )

    def test_driver_str(self) -> None:
        self.assertEqual(
            str(self.driver),
            f"{self.driver.username} "
            f"({self.driver.first_name} {self.driver.last_name})",
        )

    def test_get_absolute_url(self) -> None:
        self.assertEqual(self.driver.get_absolute_url(), "/drivers/1/")

    def test_licence_number_exists(self) -> None:
        self.assertEqual(self.driver.license_number, "ABC12345")


class CarModelTest(TestCase):
    def test_car_str(self) -> None:
        manufacturer = Manufacturer.objects.create(
            name="Audi",
            country="Germany"
        )
        car = Car.objects.create(model="Audi RS6", manufacturer=manufacturer)
        self.assertEqual(str(car), car.model)
