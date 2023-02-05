
from flask import Blueprint, request

from .request.types import VowelCountRequestApiType
from .response.types import VowelCountResponseApiType
from ..core.enums.http_status import HttpStatus

bp = Blueprint('words', __name__)


@bp.route('/vowel_count', methods=['POST'])
def vowel_count():
    payload = request.json

    result = VowelCountRequestApiType(payload).run()

    response = VowelCountResponseApiType({'words': result})

    return response.to_response(), HttpStatus.OK.status_code
