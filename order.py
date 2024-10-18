from order_detail import OrderDetail
from item import Item

class Order:
    def __init__(self, customer, date, status) -> None:
        self.customer = customer
        self.date = date
        self.status = status
        self.order_details = []

    def add_item(self, item: Item, quantity: int, tax_status: str):
        print('Quantidade',quantity, quantity <= 0)
        if quantity <= 0:
            raise Exception("Quantitade inválida!")
        order_detail = OrderDetail(item, quantity, tax_status)
        self.order_details.append(order_detail)
        item.remove_item_stock(quantity)

    def calc_total(self) -> float:
        return sum(detail.calc_total() for detail in self.order_details)