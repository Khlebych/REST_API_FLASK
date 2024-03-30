from dataclasses import dataclass
# from typing import List


@dataclass()
class Product:
    id: str
    name: str
    price: float