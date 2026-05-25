class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit_money(self, amount):
        if amount <= 0:
            raise ValueError("El monto a depositar debe ser mayor que 0.")

        self.balance += amount

    def withdraw_money(self, amount):
        if amount <= 0:
            raise ValueError("El monto a retirar debe ser mayor que 0.")

        if amount > self.balance:
            raise ValueError("No tienes suficiente dinero en la cuenta.")

        self.balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw_money(self, amount):
        if amount <= 0:
            raise ValueError("El monto a retirar debe ser mayor que 0.")

        if self.balance - amount < self.min_balance:
            raise ValueError("No puedes retirar dinero porque el balance quedaría debajo del mínimo permitido.")

        self.balance -= amount


account1 = BankAccount(1000)
account1.deposit_money(500)
account1.withdraw_money(300)

print("Balance cuenta normal:", account1.balance)


savings1 = SavingsAccount(1000, 200)
savings1.deposit_money(500)
savings1.withdraw_money(1000)

print("Balance cuenta de ahorros:", savings1.balance)


savings1.withdraw_money(400) # Esta línea va a producir error porque dejaría el balance debajo de 200, quebrado!, en la ruina hermano!
