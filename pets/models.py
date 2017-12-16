from django.db import models


class Animal(models.Model):
    name = models.CharField('Pet name', max_length=50)
    breed = models.CharField('Breed',max_length=30)
    age = models.IntegerField('Age', default=0)
    sound = models.CharField('Breed',max_length=10)

    def __str__(self):
        return f"The {self.name} says {self.sound}"
