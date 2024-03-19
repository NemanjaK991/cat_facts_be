import allure
import requests
from json import JSONDecodeError


@allure.title('Create session')
def create_session():
    session = requests.Session()
    headers = {'Accept': 'application/json, text/javascript, */*;'}
    session.headers.update(headers)
    return session


@allure.title('Send session request with method, url and optional kwargs')
def session_request(session, method, url, **kwargs):
    try:
        return session.request(str(method.value), url, **kwargs)
    except Exception as e:
        print(str(e))


@allure.title('Validate response with status code')
def valid_response(response, status_code):
    assert response, f'Response: {response}'
    assert response.status_code == status_code, f'Response code: {response.status_code}'


@allure.title('Get json from response')
def get_json_from_response(response):
    try:
        return response.json()
    except JSONDecodeError as e:
        print('Response could not be serialized ' + str(e))


@allure.title('Validate response with status code and return json')
def valid_response_and_return_json(response, status_code):
    valid_response(response, status_code)
    return get_json_from_response(response)


@allure.title('Access a value from the json response object')
def get_value_from_json_data(json_data, *args):
    actual_value = json_data
    for key in args:
        try:
            actual_value = actual_value[int(key)]
        except ValueError:
            actual_value = actual_value[key]
    return actual_value



