from django.core import validators
from django.db import models

from utils.choices import GengerChoices, SizeChoices


class Dog(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    breed = models.ForeignKey(
        "Breed", related_name="breed", on_delete=models.CASCADE
    )
    gender = models.CharField(choices=GengerChoices.choices)
    color = models.CharField(max_length=30)
    favorite_food = models.CharField(max_length=30)
    favorite_toy = models.CharField(max_length=30)

    class Meta:
        ordering = ["id"]


class Breed(models.Model):
    name = models.CharField(max_length=30)
    size = models.CharField(choices=SizeChoices.choices)
    friendliness = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(5),
        ]
    )
    trainability = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(5),
        ]
    )
    shedding_amount = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(5),
        ]
    )
    exercise_needs = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(5),
        ]
    )

    class Meta:
        ordering = ["id"]
