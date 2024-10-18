nome = {1:"Coca",
        2:"Guaraná",
        3:"Macarrão"}

estoque = {"Coca":3,
            "Guaraná":5,
            "Macarrão":2}


class Item:
    def __init__(self, shipping_weight: float, id_item: int, price: float) -> None:
        self.shipping_weight = shipping_weight
        self.nome = nome[id_item]
        self.price = price
        self.stock = estoque[self.nome]

    def get_price_for_quantity(self, quantity: int) -> float:
        return self.price * quantity
    
    def remove_item_stock(self, quantity):
        self.stock -= quantity

    def in_stock(self) -> bool:
        # Implementar lógica de estoque
        return True