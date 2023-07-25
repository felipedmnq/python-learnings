class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.items: list[str] = []
        self.max_size = max_size

    def add_item(self, item: str):
        if self.cart_size() == self.max_size:
            raise OverflowError("Cart is full, cannot add more items.")
        self.items.append(item)

    def cart_size(self) -> int:
        return len(self.items)

    def get_cart_items(self) -> list[str]:
        return self.items

    def get_cart_total_price(self, price_map: dict[str, float]) -> float:
        pass
