class Payment:
    def __init__(self, amount: float) -> None:
        self.amount = amount
        self.status = "pending"

    def process_payment(self) -> str:
        # Simula processamento de pagamento
        self.status = "completed"  # Aqui você poderia adicionar lógica de verificação
        return f"Pagamento de {self.amount} processado com sucesso!"