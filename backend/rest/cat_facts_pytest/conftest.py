import allure
import pytest

from backend.rest.common import helpers


@allure.title('Create session fixture')
@pytest.fixture(scope='module')
def create_session():
    return helpers.create_session()


