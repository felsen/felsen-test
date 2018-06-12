
import random
from collections import namedtuple
from abc import ABC, abstractmethod


class BingoCage:

    """
    Picking randomly anything from the pack.
    """

    def __init__(self, item):
        self._item = item
        random.shuffle(self._item)

    def pick(self):
        try:
            return self._item.pop()
        except IndexError:
            raise LookupError("Bingo bag is empty.!")

    def __call__(self):
        return self.pick


Customer = namedtuple("Customer", "name fidelity")


class LineItem:

    """
    Product total price calculation.
    """
    
    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


class Order:

    """
    Customer Order details from the CART.
    """
    
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())
        

class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        """ return the discount amount. """


class FidelityPromo(Promotion):

    def discount(self, order):
        """ return 5 % offer """
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):

    def discount(self, order):
        """ return 10% discount """
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() + .1
        return discount


class LargeOrderPromo(Promotion):

    def discount(self, order):
        """ return 7% discount """
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


felix = Customer("Felix Stephen", 0)
felsen = Customer("Stephen Felix", 11000)

cart = [LineItem("pensil", 4, 5),
        LineItem("banana", 2, 7),
        LineItem("apple", 3, 25)]

print(Order(felix, cart, FidelityPromo()))
print(Order(felsen, cart, FidelityPromo()))

banana_cart = [LineItem("TN Banana", 10, 4),
               LineItem("KL Banana", 10, 7)]
print(Order(felix, banana_cart, BulkItemPromo()))
print(Order(felix, banana_cart, LargeOrderPromo()))
