from django.db.models import Count, OuterRef, Subquery
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from dog_app import models, serializers


@extend_schema(tags=["Dogs"])
class DogViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DogSerializer
    queryset = models.Dog.objects.all()


@extend_schema(tags=["Breed"])
class BreedViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BreedSerializer
    queryset = models.Breed.objects.all()

    def list(self, request, *args, **kwargs):
        dogs_count = (
            models.Dog.objects.filter(breed=OuterRef("pk"))
            .values("breed")
            .annotate(dogs_count=Count("id"))
            .values("dogs_count")
        )
        queryset = models.Breed.objects.annotate(
            dogs_count=Subquery(dogs_count)
        )
        serializer_dog = serializers.BreedGetSerializer(queryset, many=True)
        return Response(serializer_dog.data)
