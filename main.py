from customer import Customer
from order import Order
from item import Item
from payment import Payment

# Caso de Uso 1: Criar um Pedido
def criar_pedido():
    customer = Customer("João", "Rua A, 123")
    order = Order(customer, "2024-10-17", "pending")

    # Adicionando itens ao pedido
    item1 = Item(2.5, 3, 100.0)
    order.add_item(item1, 2, "taxable")

    item2 = Item(1.5, 2, 50.0)
    order.add_item(item2, 1, "non-taxable")

    total = order.calc_total()
    print(f"Total do pedido: {total:.2f}")

# Caso de Uso 2: Processar Pagamento
def processar_pagamento(total: float):
    payment = Payment(total)
    resultado = payment.process_payment()
    print(resultado)

if __name__ == "__main__":
    criar_pedido()
    total = 270  # Aqui você poderia obter o total do pedido real
    processar_pagamento(total)
