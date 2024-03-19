import allure
from backend.rest.common import helpers
from backend.rest.cat_facts_pytest.src.requests.facts import get_random_facts

suite = 'FACT'


@allure.suite(suite)
@allure.title('Get random fact')
def test_get_random_fact(create_session):
    get_random_facts(create_session)


@allure.suite(suite)
@allure.title('Get two random facts')
def test_get_more_random_facts(create_session):
    params = {'animal_type': 'cat', 'amount': 3}
    r = get_random_facts(create_session, params=params)
    assert len(r) == 3
    for ind in range(3):
        assert helpers.get_value_from_json_data(r, ind, 'type') == 'cat'
