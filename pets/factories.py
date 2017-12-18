from random import randint, choice

import factory

from pets.models import Animal


class AnimalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Animal
    name = factory.Faker('word')
    breed = factory.Faker('word')
    age = randint(1,15)
    sound = choice(['miua', 'guau', 'cuacua'])
