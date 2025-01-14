import pytest
from django.urls import reverse
from rest_framework import status

from dog_app import models
from utils.choices import GengerChoices


pytestmark = pytest.mark.django_db


def test_check_dogs_fields(client, model_factory):
    """
    Test for check fields for dog
    """
    fields = [
        "id",
        "name",
        "age",
        "breed",
        "gender",
        "color",
        "favorite_food",
        "favorite_toy",
        "breeds_age",
    ]
    model_factory(models.Dog)
    response = client.get(reverse("dog-list"))
    assert response.status_code == status.HTTP_200_OK
    assert all(response.data[0][key] for key in fields)


def test_get_avg_age_dogs(client, model_factory):
    """
    Test for check avg age for breed
    """
    breed = model_factory(models.Breed)
    dog_1 = model_factory(models.Dog, breed=breed)
    dog_2 = model_factory(models.Dog, breed=breed)
    response = client.get(reverse("dog-list"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]["breeds_age"] == (dog_1.age + dog_2.age) / 2


def test_get_dog_by_id(client, model_factory):
    """
    Test for get dog by id
    """
    breed = model_factory(models.Breed)
    model_factory(models.Dog, breed=breed)
    model_factory(models.Dog, breed=breed)
    dog = model_factory(models.Dog, breed=breed)
    response = client.get(reverse("dog-detail", kwargs={"pk": dog.id}))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["dogs_count"] == 3


def test_check_fields_dog_by_id(client, model_factory):
    """
    Test for get dog by id and check fields
    """
    fields = [
        "id",
        "name",
        "age",
        "breed",
        "gender",
        "color",
        "favorite_food",
        "favorite_toy",
        "dogs_count",
    ]
    dog = model_factory(models.Dog)
    response = client.get(reverse("dog-detail", kwargs={"pk": dog.id}))
    assert response.status_code == status.HTTP_200_OK
    assert all(response.data[key] for key in fields)


def test_update_dog(client, model_factory):
    """
    Test for update dogs fields
    """
    breed_1 = model_factory(models.Breed)
    breed_2 = model_factory(models.Breed)
    update_date = {
        "name": "Boba",
        "breed": breed_1.id,
    }
    dog = model_factory(models.Dog, breed=breed_2)
    respose = client.patch(
        reverse("dog-detail", kwargs={"pk": dog.id}), update_date
    )
    assert respose.status_code == status.HTTP_200_OK
    assert respose.data["name"] == update_date["name"]
    assert respose.data["breed"] == update_date["breed"]


def test_create_dog(client, model_factory):
    """
    Test for create dog
    """
    breed = model_factory(models.Breed)
    data = {
        "name": "Boba",
        "age": 10,
        "breed": breed.id,
        "gender": GengerChoices.MALE,
        "color": "black",
        "favorite_food": "paper",
        "favorite_toy": "chair",
    }
    response = client.post(reverse("dog-list"), data=data)
    assert response.status_code == status.HTTP_201_CREATED


def test_delete_dog(client, model_factory):
    """
    Test dor delete dog
    """
    dog = model_factory(models.Dog)
    response = client.delete(reverse("dog-detail", kwargs={"pk": dog.id}))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not models.Dog.objects.filter(pk=dog.id).exists()
