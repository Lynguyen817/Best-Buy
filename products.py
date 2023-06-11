from abc import ABC, abstractmethod


class Product:
    """
        Encapsulates the product information, including its name and price,
        and keeps track of the total quantity of items of that product
        if it's available in the store.
    """
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self):
        """ Getter function for quantity. Return the quantity."""
        return float(self.quantity)

    def set_quantity(self, quantity):
        """ Setter function for quantity.
            If quantity reaches 0, deactivates the product."""
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def get_promotion(self):
        """ Getter function for promotion. Return promotion."""
        return self.promotion

    def set_promotion(self, promotion):
        """ Setter function for promotion."""
        self.promotion = promotion

    def is_active(self):
        """ Getter function for active.
            Return True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """ Activates the product."""
        self.active = True

    def deactivate(self, amount):
        """ Deactivates the product if the quantity reaches 0"""
        self.quantity -= amount
        if self.quantity <= 0:
            self.active = False

    def show(self):
        """ Shows list of products in the store."""
        if self.promotion:
            return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Promotion: {self.promotion.name}"
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Promotion: None"

    def buy(self, quantity):
        """ Returns a total price of the purchase."""
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        if quantity <= 0:
            print(f"Error: Quantity must be greater than 0.")
        if self.quantity < quantity:
            print(f"Error: Not enough quantity.")
        total_price = self.price * quantity
        self.quantity -= quantity
        return total_price


class NonStockedProducts(Product):
    """ Some products in the store are not physical.
        The quantity is set to zero and always stay that way. """
    def __init__(self, name, price):
        super().__init__(name, price, 0)
        self.quantity = 0

    def show(self):
        """ Shows non-physical products"""
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited, Promotion: {self.promotion.name}"

    def buy(self, quantity):
        """ Return the price of each order."""
        total_price = self.price * quantity
        self.quantity -= quantity
        return total_price


class LimitedProducts(Product):
    """ Some products can only be purchased X times in an order.
     If an order is attempted with quantity larger than the maximum one,
     it will be refused with an exception."""
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        """ Limits times of purchasing a limited product. """
        if quantity > self.maximum:
            print(f"Error:{self.name} can only be purchased {self.maximum} time(s) in an order.")
        total_price = self.price * quantity
        self.quantity -= quantity
        return total_price

    def show(self):
        """ Shows limited products. """
        return f"{self.name}, Price: ${self.price}, Limited to {self.maximum} per order!, Promotion: {self.promotion}"


class Promotions(ABC):
    """ Adds promotions to a product instance."""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotions):
    """ Apply half price for a second product."""
    def apply_promotion(self, product, quantity):
        regular_price = product.price * quantity
        discount_price = regular_price * 3/4
        product.quantity -= quantity
        return discount_price


class ThirdOneFree(Promotions):
    """ Apply the third one free."""
    def apply_promotion(self, product, quantity):
        regular_price = product.price * quantity
        discount_price = regular_price - (regular_price/3)
        product.quantity -= quantity
        return discount_price


class PercentDiscount(Promotions):
    """ Apply discount percent off."""
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        regular_price = product.price * quantity
        discount_price = regular_price * (1 - (self.percent/100))
        product.quantity -= quantity
        return discount_price






