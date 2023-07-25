import pytest

from .shopping_cart import ShoppingCart


def test_can_add_item_to_shopping_cart():
    cart = ShoppingCart(2)
    cart.add_item("milk")
    assert cart.cart_size() == 1


def test_when_item_added_then_cart_contains_item():
    cart = ShoppingCart(2)
    cart.add_item("milk")
    assert "milk" in cart.get_cart_items()


def test_when_add_more_than_max_items_should_fail():
    cart = ShoppingCart(max_size=2)
    cart.add_item("milk")
    cart.add_item("eggs")
    with pytest.raises(OverflowError):
        cart.add_item("bread")


def test_can_get_total_cart_price():
    print("test can get total cart price")
    pass
