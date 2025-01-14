from django.db import models


class GengerChoices(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"


class SizeChoices(models.TextChoices):
    TINY = "Tiny"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
