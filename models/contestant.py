from marshmallow import Schema, fields

class ContestantSchema(Schema):
    contestantName = fields.Str(required=True, unique=True)
    husbandName = fields.Str(required=True)
    vocalRange = fields.Int(required=True)
    location = fields.Int(required=True)