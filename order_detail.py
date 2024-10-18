from item import Item 

class OrderDetail:
    def __init__(self, item: Item, quantity: int, tax_status: str) -> None:
        self.item = item
        self.quantity = quantity
        self.tax_status = tax_status
    
    def calc_subtotal(self) -> float:
        return self.item.get_price_for_quantity(self.quantity)

    def calc_tax(self) -> float:
        # Lógica simples de cálculo de imposto
        if self.tax_status == "taxable":
            return self.calc_subtotal() * 0.1  # Exemplo: 10% de imposto
        return 0.0

    def calc_total(self) -> float:
        return self.calc_subtotal() + self.calc_tax()