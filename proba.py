from datetime import date
from marshmallow import Schema, fields, validate, ValidationError


# _______________ сериализация _____________________________

class ProductSchema(Schema):
    name = fields.Str()


class OrderSchema(Schema):
    deliver_at = fields.Date()
    products = fields.Nested(ProductSchema(many=True))


book = dict(name = 'Book')
album = dict(products = [book], deliver_at=date(2024, 3, 25))

schema = OrderSchema()
res = schema.dump(album)

print(res)

# _______________ десериализация _____________________________


class UserSchema(Schema):
    name = fields.Str(validate=validate.Length(min=5))
    email = fields.Email(validate=validate.Length(min=5))
    created_at = fields.DateTime()
    age = fields.Int(validate=validate.Range(min=25))


user_data = {
    "created_at":"2025-03-25T17:40:25.896542",
    "email":"ya@ya.ru",
    "name":"Johnny",
    "age":2,
}
try:
    UserSchema().load(user_data)
except ValidationError as err:
    print(err.messages)

# u_schema = UserSchema()
# result = u_schema.load(user_data)
# print(result)