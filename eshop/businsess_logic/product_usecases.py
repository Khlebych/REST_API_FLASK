import uuid
from typing import Optional, List

# from eshop.businsess_logic import product
from eshop.data_access.product_repo import product_List, save, get_by_id

from eshop.businsess_logic.product import Product
from eshop.view.product_schemas import ProductCreateDtoSchema


def product_create(product: ProductCreateDtoSchema) -> Product:
    print(product)
    new_product = Product(
        id=str(uuid.uuid4()),
        name=product['name'],
        price=product['price'],
    )

    for i in range(len(product_List)):
        existing_product = product_List[i]
        if existing_product.id == new_product.id:
            product_List[i] = new_product
            break
    else:
        product_List.append(new_product)

    save(new_product)
    return new_product


def product_get_by_id(id: str) -> Optional[Product]:
    return get_by_id(id)


def product_get_many(page: int, limit: int) -> List[Product]:
    raise Exception('Not implemented yet')