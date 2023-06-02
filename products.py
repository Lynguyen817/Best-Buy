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

    def get_quantity(self):
        """ Getter function for quantity. Return the quantity."""
        return float(self.quantity)

    def set_quantity(self, quantity):
        """ Setter function for quantity.
            If quantity reaches 0, deactivates the product."""
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

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
        """ Show list of products in the store."""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """ Return a total price of the purchase."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        if self.quantity < quantity:
            raise ValueError("Not enough quantity.")
        total_price = self.price * quantity
        self.quantity -= quantity
        return total_price
