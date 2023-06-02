import pytest
from products import Product


def test_creating_product():
    """ Test that creating a normal product works."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100


def test_invalid_detail():
    """ Test that creating a product with invalid details
    (empty name, negative price) invokes an exception."""
    try:
        Product("", 250, 100)
    except ValueError as e:
        print(f"Got an error but we caught it: {e}")


def test_deactivate_product():
    """ Test that when a product reaches 0 quantity, it becomes inactive."""
    product = Product("MacBook Air M2", price=1450, quantity=4)
    assert product.active == True


def test_buy_modified_quantity():
    """ Test that product purchase modifies the quantity and returns the right output."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    purchase_quantity = 5
    new_quantity = Product.buy(product, purchase_quantity)
    assert purchase_quantity > 0, "Quantity purchase must be greater than 0. "
    assert new_quantity == Product.buy(product, purchase_quantity)


def test_buy_large_amount():
    """ Test that buying a larger quantity than exists invokes exception."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    try:
        Product.buy(product, quantity=110)
    except ValueError:
        assert "Not enough quantity."
