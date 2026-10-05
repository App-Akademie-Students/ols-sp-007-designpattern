from abc import ABC, abstractmethod


class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight_kg: float) -> float: ...


class StandardShipping(ShippingStrategy):
    def calculate_cost(self, weight_kg: float) -> float:
        return 4.90 + 0.50 * weight_kg


class ExpressShipping(ShippingStrategy):
    def calculate_cost(self, weight_kg: float) -> float:
        return 9.90 + 1.00 * weight_kg


class PickupShipping(ShippingStrategy):
    def calculate_cost(self, weight_kg: float) -> float:
        return 0.00


class Order:
    def __init__(self, weight_kg: float) -> None:
        self.weight_kg = weight_kg
        self.shipping_strategy: ShippingStrategy | None = None

    def set_shipping_strategy(self, shipping_strategy: ShippingStrategy) -> None:
        self.shipping_strategy = shipping_strategy

    def shipping_cost(self) -> float:
        return self.shipping_strategy.calculate_cost(self.weight_kg)


def format_eur(amount: float) -> str:
    return f"{amount:.2f}".replace(".", ",") + " EUR"


def main() -> None:
    order = Order(2.0)

    order.set_shipping_strategy(StandardShipping())
    print(f"Standard: {format_eur(order.shipping_cost())}")

    order.set_shipping_strategy(ExpressShipping())
    print(f"Express:  {format_eur(order.shipping_cost())}")

    order.set_shipping_strategy(PickupShipping())
    print(f"Pickup:   {format_eur(order.shipping_cost())}")


if __name__ == "__main__":
    main()
