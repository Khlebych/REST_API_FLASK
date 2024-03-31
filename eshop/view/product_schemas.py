from marshmallow import Schema, fields


class ProductCreateDtoSchema(Schema):
    name = fields.String(required=True)
    price = fields.Float(required=True)


class ProductSchema(Schema):
    id = fields.String(required=True)
    name = fields.String(required=True)
    price = fields.Float(required=True)


class ProductGetManyParams(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)