from unittest.mock import Mock

import pytest

from .item_database import ItemDatabase
from .shopping_cart import ShoppingCart


@pytest.fixture
def cart():
    return ShoppingCart(2)


def test_can_add_item_to_shopping_cart(cart):
    cart.add_item("milk")
    assert cart.cart_size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    cart.add_item("milk")
    assert "milk" in cart.get_cart_items()


def test_when_add_more_than_max_items_should_fail(cart):
    cart.add_item("milk")
    cart.add_item("eggs")
    with pytest.raises(OverflowError):
        cart.add_item("bread")


def test_can_get_total_cart_price(cart):
    cart.add_item("milk")
    cart.add_item("eggs")

    # each added item will be mocked
    item_database = ItemDatabase()
    item_database.get = Mock(side_effect=[1.0, 2.0])

    assert cart.get_cart_total_price(item_database) == 3.0
