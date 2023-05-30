import products


class Store:
    """
        Contains a list of products that exits in the store.
        Expose all the methods that including add product, remove product
        get all products that are active, buy products and return the total price.
    """

    def __init__(self, products_list):
        self.products_list = products_list
        self.shopping_list = []
        self.total_price = 0

    def add_products(self, product):
        """ Adds products to the store."""
        return self.products_list.append(product)

    def remove_product(self, product):
        """ Remove products from the store."""
        return self.products_list.remove(product)

    def get_total_quantity(self):
        """ Returns how many items are in the store in total."""
        total_quantity = 0
        for product in self.products_list:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        """ Returns all products in the store that are active."""
        active_product = []
        for product in self.products_list:
            if product.is_active():
                active_product.append(product)
        return active_product
       
    def order(self, shopping_list):
        """ Makes an order and returns the total price of the order."""
        total_price = 0
        self.shopping_list = shopping_list
        for product, quantity in shopping_list:
            product_price = product.buy(quantity)
            total_price += product_price
        return total_price















