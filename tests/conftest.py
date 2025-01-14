# pylint: disable=redefined-outer-name
import pytest
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def client():
    """
    Returns api client to perform requests
    """
    return APIClient()


@pytest.fixture
def model_factory():
    """
    Creates object with provided model
    """

    def factory(model_class, *args, **kwargs):
        return baker.make(model_class, *args, **kwargs)

    return factory
