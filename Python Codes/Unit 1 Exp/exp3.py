# Write a program to implement a Configurable Payment Processing System Using the Strategy Pattern

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardStrategy(PaymentStrategy):
    def process_payment(self, amount):
        print(f"credit card payment of ₹{amount}")
        # algo for payment

class DebitCardStrategy(PaymentStrategy):
    def process_payment(self, amount):
        print(f"debit card payment of ₹{amount}")
        # algo for payment

class UPIStrategy(PaymentStrategy):
    def process_payment(self, amount):
        print(f"UPI payment of ₹{amount}")
        # algo for payment

class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.process_payment(amount)

# def main():
#     payment_method = "credit_card"
#
#     if payment_method == "credit_card":
#         strategy = CreditCardStrategy()
#     elif payment_method == "debit_card":
#         strategy = DebitCardStrategy()
#     elif payment_method == "paypal":
#         strategy = UPIStrategy()
#
#     context = PaymentContext(strategy)
#     context.pay(100)

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")

    cc = CreditCardStrategy()
    dc = DebitCardStrategy()
    upi = UPIStrategy()

    ch = int(input("@ Payment Method\n1. Credit Card\n2. Debit Card\n3. UPI\n> "))
    if ch == 1:
        strategy = CreditCardStrategy()
    elif ch == 2:
        strategy = DebitCardStrategy()
    elif ch == 3:
        strategy = UPIStrategy()

    context = PaymentContext(strategy)
    context.pay(420)