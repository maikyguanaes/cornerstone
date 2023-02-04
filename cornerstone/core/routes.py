import datetime
from os import environ

from flask import Blueprint

from .responses.types import ApiType
from ..core.enums.http_status import HttpStatus

CURRENT_API_VERSION = environ.get('CURRENT_API_VERSION')

bp = Blueprint('core', __name__)
bp_v1 = Blueprint('core_v1', __name__)


@bp.route('/health-check', methods=['GET'])
def health_check():
    payload = ApiType({'version': CURRENT_API_VERSION, 'data': [str(datetime.datetime.now())]})
    return payload.to_response(), HttpStatus.OK.status_code


@bp_v1.route('/', methods=['GET'])
def index():
    payload = ApiType({'version': CURRENT_API_VERSION})
    return payload.to_response(), HttpStatus.OK.status_code
