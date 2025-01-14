from django.db.models import Avg, Count, OuterRef, Subquery
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from dog_app import models, serializers


@extend_schema(tags=["Dogs"])
class DogViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DogSerializer
    queryset = models.Dog.objects.all()

    def list(self, request, *args, **kwargs):
        breeds_age = (
            models.Breed.objects.filter(id=OuterRef("breed"))
            .annotate(breeds_age=Avg("breed__age"))
            .values("breeds_age")
        )
        queryset = models.Dog.objects.annotate(breeds_age=Subquery(breeds_age))
        serializer = serializers.DogSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        dogs_count = models.Breed.objects.filter(
            pk=instance.breed.id
        ).aggregate(dogs_count=Count("breed__id"))
        instance.dogs_count = dogs_count["dogs_count"]
        serializer = serializers.DogSerializer(instance)
        return Response(serializer.data)


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
        serializer = serializers.BreedSerializer(queryset, many=True)
        return Response(serializer.data)
