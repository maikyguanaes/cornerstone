from flask import jsonify
from schematics import Model as SchematicModel
from schematics.types import DictType, IntType


class VowelCountResponseApiType(SchematicModel):
    words = DictType(IntType(), default=dict)

    def to_response(self):
        self.validate()
        return jsonify(self.words)
