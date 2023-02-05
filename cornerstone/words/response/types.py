from flask import jsonify, Response
from schematics import Model as SchematicModel
from schematics.types import DictType, IntType, ListType, StringType


class VowelCountResponseApiType(SchematicModel):
    words = DictType(IntType(), default=dict)

    def to_response(self) -> Response:
        self.validate()
        return jsonify(self.words)


class SortWordsResponseApiType(SchematicModel):
    words = ListType(StringType(), default=list)

    def to_response(self) -> Response:
        self.validate()
        return jsonify(self.words)
