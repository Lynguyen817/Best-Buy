import pytest
import products


def test_creating_product(product):
    """ Test that creating a normal product works."""
    assert product.is_active()


def test_invalid_detail(product):
    """ Test that creating a product with invalid details
    (empty name, negative price) invokes an exception."""
    pass


def deactivate_product(product):
    """ Test that when a product reaches 0 quantity, it becomes inactive."""
    pass


def buy_modified_quantity(product):
    """ Test that product purchase modifies the quantity and returns the right output."""
    pass


def buy_large_amount(product):
    """ Test that buying a larger quantity than exists invokes exception."""
    pass