"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
"""


from typing import Callable, Type


class Order:
    def __init__(self, price: float, discount_strategy: Callable = None) -> None:
        self.price = price
        self.discount_strategy = discount_strategy

    def final_price(self) -> float:
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0

        return self.price - discount


def morning_discount(order: Order) -> float:
    discount = order.price * 0.25
    return discount


def elder_discount(order: Order) -> float:
    discount = order.price * 0.1
    return discount
