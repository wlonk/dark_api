import pytest
from django.contrib.auth import get_user_model
from ..models import (
    Sheet,
    Suit,
)


@pytest.fixture(scope='module')
def user():
    User = get_user_model()
    return User.objects.create()


@pytest.mark.django_db
def test_create_sheet_for_user(user):
    Sheet.objects.create_sheet_for_user(user)
    assert Suit.objects.count() == 4
