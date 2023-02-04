import datetime
import json

from freezegun import freeze_time

from cornerstone.core.enums.http_status import HttpStatus
from cornerstone.core.response.types import ApiType
from cornerstone.core.routes import CURRENT_API_VERSION


def test_root_url(client):
    # when
    response = client.get('/')

    # then
    payload = json.loads(response.data)
    api_type = ApiType(payload)

    assert HttpStatus(response.status_code).is_ok
    assert response.data
    assert payload == {'version': CURRENT_API_VERSION, 'data': []}
    assert api_type.version == payload['version']
    assert api_type.data == payload['data']


@freeze_time("2018-10-02")
def test_health_check(client):
    # when
    response = client.get('/health-check')

    # then
    payload = json.loads(response.data)
    api_type = ApiType(payload)

    assert HttpStatus(response.status_code).is_ok
    assert response.data
    assert payload == {'version': CURRENT_API_VERSION, 'data': [str(datetime.datetime.now())]}
    assert api_type.version == payload['version']
    assert api_type.data == payload['data']


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
