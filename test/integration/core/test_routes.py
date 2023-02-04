import json

from cornerstone.core.enums.http_status import HttpStatus
from cornerstone.core.responses.types import ApiType


def test_root_url(client):
    # when
    response = client.get('/health-check')

    # then
    assert HttpStatus(response.status_code).is_ok
    assert response.data


def test_root_url_v1(client):
    # when
    response = client.get('v1/')

    # then
    payload = json.loads(response.data)
    api_type = ApiType(payload)

    assert HttpStatus(response.status_code).is_ok
    assert payload == {'version': 'v1', 'data': []}
    assert api_type.version == payload['version']
    assert api_type.data == payload['data']
