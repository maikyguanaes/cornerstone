from flask import jsonify
from schematics import Model as SchematicModel
from schematics.types import StringType, ListType


class ApiType(SchematicModel):
    version = StringType(required=True)
    data = ListType(StringType(), default=list)

    def to_response(self):
        self.validate()
        return jsonify(self.to_primitive())
