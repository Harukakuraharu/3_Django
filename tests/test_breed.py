import pytest
from django.urls import reverse
from rest_framework import status

from dog_app import models
from utils.choices import SizeChoices


pytestmark = pytest.mark.django_db


def test_get_check_breed_fields(client, model_factory):
    """
    Test for check fields for breeds
    """
    fields = [
        "id",
        "name",
        "size",
        "friendliness",
        "trainability",
        "shedding_amount",
        "exercise_needs",
        "dogs_count",
    ]
    breed = model_factory(models.Breed)
    model_factory(models.Dog, breed=breed)
    response = client.get(reverse("breed-list"))
    assert response.status_code == status.HTTP_200_OK
    assert all(response.data[0][key] for key in fields)


def test_get_count_dogs(client, model_factory):
    """
    Test for check count dogs fore breed
    """
    breed = model_factory(models.Breed)
    model_factory(models.Dog, breed=breed)
    model_factory(models.Dog, breed=breed)
    response = client.get(reverse("breed-list"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]["dogs_count"] == 2


def test_get_breed_by_id(client, model_factory):
    """
    Test for get breed by id
    """
    breed = model_factory(models.Breed)
    model_factory(models.Dog, breed=breed)
    response = client.get(reverse("breed-detail", kwargs={"pk": breed.id}))
    assert response.status_code == status.HTTP_200_OK


def test_update_breed(client, model_factory):
    """
    Test for update breed fields
    """
    breed = model_factory(models.Breed)

    update_date = {
        "name": "Labr",
    }
    respose = client.patch(
        reverse("breed-detail", kwargs={"pk": breed.id}), update_date
    )
    assert respose.status_code == status.HTTP_200_OK
    assert respose.data["name"] == update_date["name"]


def test_create_dog(client):
    """
    Test for create dog
    """
    data = {
        "name": "Labr",
        "size": SizeChoices.LARGE,
        "friendliness": 5,
        "trainability": 5,
        "shedding_amount": 5,
        "exercise_needs": 5,
    }
    response = client.post(reverse("breed-list"), data=data)
    assert response.status_code == status.HTTP_201_CREATED


def test_delete_breed(client, model_factory):
    """
    Test dor delete breed
    """
    breed = model_factory(models.Breed)
    response = client.delete(reverse("breed-detail", kwargs={"pk": breed.id}))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not models.Breed.objects.filter(pk=breed.id).exists()
