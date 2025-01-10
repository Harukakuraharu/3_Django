from rest_framework import serializers

from dog_app import models


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dog
        fields = "__all__"


class DogGetSerializer(serializers.ModelSerializer):
    breeds_age = serializers.IntegerField()

    class Meta:
        model = models.Dog
        fields = (
            "id",
            "name",
            "age",
            "breed",
            "gender",
            "color",
            "favorite_food",
            "favorite_toy",
            "breeds_age",
        )


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Breed
        fields = "__all__"


class BreedGetSerializer(serializers.ModelSerializer):
    dogs_count = serializers.IntegerField()

    class Meta:
        model = models.Breed
        fields = (
            "id",
            "name",
            "size",
            "friendliness",
            "trainability",
            "shedding_amount",
            "exercise_needs",
            "dogs_count",
        )
