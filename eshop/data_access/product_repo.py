from typing import List, Optional

from eshop.businsess_logic.product import Product

product_List: List[Product] = [
    Product(
        id='1',
        name='Телевизор',
        price=15,
    ),
    Product(
        id='2',
        name='Кофемашина',
        price=10,
    ),
    Product(
        id='3',
        name='Ноутбук',
        price=12,
    )
]


def save(product: Product):
    for i in range(len(product_List)):
        existed_product = product_List[i]
        if existed_product.id == product.id:
            product_List[i] = product
            break
    else:
        product_List.append(product)


def delete_by_id(_id: str):
    global product_List
    product_List = [p for p in product_List if p.id != id]


def get_by_id(_id: str) -> Optional[Product]:
    return next((p for p in product_List if p.id == id), None)


def get_many(page: int = 0, limit: int = 10):
    start = page * limit
    end = start + limit
    return product_List[start:end]
