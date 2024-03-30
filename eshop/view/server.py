from flask import Flask, request
from marshmallow import ValidationError

from eshop.businsess_logic.order_usecases import order_create, order_get_many, order_get_by_id
from eshop.businsess_logic.product_usecases import product_create, product_get_by_id
from eshop.view.order_schemas import OrderCreateDtoSchema, OrderSchema, OrderGetManyParams
from eshop.data_access.product_repo import get_many
from eshop.view.product_schemas import ProductCreateDtoSchema, ProductSchema

app = Flask(__name__)


@app.post("/api/v1/product")        # создание продукта
def product_create_endpoint():
    try:
        product_create_dto = ProductCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        product = product_create(product_create_dto)

    except Exception as e:
        return {
            "error": str(e)
        }

    return ProductSchema().dump(product)


@app.get("/api/v1/product")     # получение страницы продуктов
def get_all_product():
    return get_many()


@app.get("/api/v1/product/<_id>")    # получение продукта по его ID
def product_get_by_id_endpoint(_id):
    product = product_get_by_id(_id)

    if product is None:
        return {
            "error": 'Not found'
        }, 404

    return ProductSchema().dump(product)


@app.post("/api/v1/order")
def order_create_endpoint():
    try:
        order_create_dto = OrderCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        order = order_create(
            product_ids=order_create_dto['product_ids']
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    return OrderSchema().dump(order)


@app.get("/api/v1/order")
def order_get_many_endpoint():
    try:
        order_get_many_params = OrderGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    order = order_get_many(
        page=order_get_many_params['page'],
        limit=order_get_many_params['limit'],
    )

    return OrderSchema(many=True).dump(order)


@app.get("/api/v1/order/<_id>")
def order_get_by_id_endpoint(_id):
    order = order_get_by_id(_id)

    if order is None:
        return {
            "error": 'Not found'
        }, 404

    return OrderSchema().dump(order)


def run_server():
    app.run()
