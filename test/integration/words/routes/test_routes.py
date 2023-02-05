import json
from os.path import join

import pytest

from cornerstone import PROJECT_ROOT_PATH
from cornerstone.core.enums.http_status import HttpStatus


@pytest.fixture
def file_path():
    return join(PROJECT_ROOT_PATH, "test/fixtures/json/words/request/words.json")


@pytest.fixture
def payload_as_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
    file.close()

    return data


@pytest.fixture
def payload_as_text(file_path):
    with open(file_path) as file:
        data = file.read()
    file.close()

    return data


def test_vowel_count_with_content_type_text(client, payload_as_text):

    # when
    response = client.post("vowel_count", data=payload_as_text, content_type='text/plain')
    response_data = response.json

    # then
    assert HttpStatus(response.status_code).is_bad_request
    assert response_data is None


def test_vowel_count_url(client, payload_as_json):

    # when
    response = client.post("vowel_count", json=payload_as_json)
    response_data = response.json

    # then
    assert HttpStatus(response.status_code).is_ok
    assert response_data == {"batman": 2, "robin": 2, "coringa": 3}


@pytest.mark.parametrize('file_path', [
    join(PROJECT_ROOT_PATH, "test/fixtures/json/words/request/incorrect_words.json")
])
def test_vowel_count_incorrect_payload(client, payload_as_json, file_path):
    # when
    response = client.post("vowel_count", json=payload_as_json)
    response_data = response.json

    # then
    assert HttpStatus(response.status_code).is_bad_request
    assert response_data == {}


def test_vowel_count_url_method_not_allowed(client, payload_as_json):

    # when
    response = client.get("vowel_count", json=payload_as_json)
    response_data = response.json

    # then
    assert HttpStatus(response.status_code).is_method_not_allowed
    assert response_data is None
