from marshmallow import Schema, fields


class ScoreResponseSchema(Schema):
    result = fields.Integer()
