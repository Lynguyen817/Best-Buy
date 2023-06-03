from products import Product, NonStockedProducts, LimitedProducts
from store import Store


def start(store_obj):
    """ Shows the menu with options to the users.
        Returns results for each option. """
    for _ in range(0, 100):
        print("""
        Store Menu
        __________
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit
        """)
        user_choice = int(input("Please choose a number:"))
        if user_choice == 1:
            list_all_product(store_obj)
        if user_choice == 2:
            total_products = store_obj.get_total_quantity()
            print(f"Total of {total_products} items in store")
        if user_choice == 3:
            make_order(store_obj)
        if user_choice == 4:
            exit()


def list_all_product(store_obj):
    """ Lists all products in the store. """
    print("________")
    number = 0
    for product_obj in store_obj.get_all_products():
        number += 1
        print(f"{number}.{product_obj.show()}")
    print("________")


def make_order(store_obj):
    """
        Makes an order when the user inputs the product number
        and the amount of that product.
        Returns the total payment after the user completes the purchase.
    """
    print("When you want to finish order, enter empty text.")
    shopping_list = []
    while True:
        list_all_product(store_obj)
        product_number = input("Which product # do you want?")
        product_amount = input("What amount do you want?")
        if product_number == "" and product_amount == "":
            print("********")
            print(f"Order made! Total payment: ${total_payment}")
            break
        if int(product_number) > len(store_obj.get_all_products()):
            print("Error adding product.")
        else:
            all_products = store_obj.get_all_products()
            total_payment = 0
            if int(product_number) == 1:
                product_name = all_products[0]
                shopping_list.append([product_name, int(product_amount)])
            if int(product_number) == 2:
                product_name = all_products[1]
                shopping_list.append([product_name, int(product_amount)])
            if int(product_number) == 3:
                product_name = all_products[2]
                shopping_list.append([product_name, int(product_amount)])
            if int(product_number) == 4:
                product_name = all_products[3]
                NonStockedProducts.show(product_name)
                shopping_list.append([product_name, int(product_amount)])
            if int(product_number) == 5:
                product_name = all_products[4]
                LimitedProducts.show(product_name)
                shopping_list.append([product_name, int(product_amount)])
            print("Product added to list!\n")
            total_payment += store_obj.order(shopping_list)


def main():
    """
        Creates a default list of products in store.Creates an object of Store class,
        then calls the start function to show menu to the users.
    """
    products_list = [Product("MacBook Air M2", price=1450, quantity=100),
                     Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                     Product("Google Pixel 7", price=500, quantity=250),
                     NonStockedProducts("Windows License", price=125),
                     LimitedProducts("Shipping", price=10, quantity=250, maximum=1)
                    ]
    store_obj = Store(products_list)
    start(store_obj)


if __name__ == "__main__":
    main()
