from rest_framework.test import APITestCase

from django.urls import reverse

from pets.factories import AnimalFactory


class AnimalTestCase(APITestCase):
    def setUp(self):
        self.client.login(username='mayela', password='django2.0')
        self.url = reverse("pets:list_create_pets")

    def test_guagua(self):
        dog = AnimalFactory(sound='guagua')
        self.assertEqual('guagua', dog.sound)

    def test_age_12(self):
        cat = AnimalFactory(age=12)
        self.assertEqual(12, cat.age)

    def test_age_is_a_string(self):
        cat = AnimalFactory(age=13)
        self.assertEqual(int , type(cat.age))
