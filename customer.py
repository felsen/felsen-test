from collections import namedtuple


Customer = namedtuple("Customer", ["name", "fidelity"])


class LineItem:

    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.quantity * self.price

    
class Order:

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
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order: total:{:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())

    
def fidelity_promo(order):
    return order.total() * .05 if order.customer.fidelity >= 10000 else 0


def bulkitem_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def largeorder_promo(order):
    distinct_item = {item.product for item in order.cart}
    if len(distinct_item) >= 10:
        return order.total() * .07
    return 0


felix = Customer("Felix Stephen", 0)
felsen = Customer("Stephen Felix", 11000)
cart = [LineItem("pensil", 4, 5),
        LineItem("banana", 2, 7),
        LineItem("apple", 3, 25)]
print(Order(felix, cart, fidelity_promo))
print(Order(felsen, cart, fidelity_promo))
banana_cart = [LineItem("TN Banana", 10, 4),
               LineItem("KL Banana", 10, 7)]
print(Order(felix, banana_cart, bulkitem_promo))
print(Order(felix, banana_cart, largeorder_promo))
