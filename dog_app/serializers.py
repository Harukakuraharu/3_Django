from rest_framework import serializers

from dog_app import models


class DogSerializer(serializers.ModelSerializer):
    breeds_age = serializers.IntegerField(read_only=True)
    dogs_count = serializers.IntegerField(read_only=True)

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
            "dogs_count",
        )


class BreedSerializer(serializers.ModelSerializer):
    dogs_count = serializers.IntegerField(read_only=True)

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
