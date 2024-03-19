import allure

from backend.rest.common import constants as common_constants, helpers
from backend.rest.cat_facts_pytest.src.data import constants
from backend.rest.cat_facts_pytest.src.configuration import base_url


@allure.title('Send request with method on facts random uri')
def request(session, method, **kwargs):

    return helpers.session_request(session, method,
                                   f'{base_url}{constants.Uri.FACTS.value}{constants.Uri.RANDOM.value}', **kwargs)


@allure.title('Get random facts')
def get_random_facts(session, params=None):
    r = request(session, common_constants.Method.GET, params=params)
    facts = helpers.valid_response_and_return_json(r, 200)
    return facts
