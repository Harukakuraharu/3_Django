from django.urls import include, path
from rest_framework.routers import DefaultRouter

from dog_app import views


router = DefaultRouter()
router.register(r"dog", views.DogViewSet, basename="dog")
router.register(r"breed", views.BreedViewSet, basename="breed")


urlpatterns = [
    path("api/", include(router.urls)),
]
