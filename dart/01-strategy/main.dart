abstract interface class ShippingStrategy {
  double calculateCost(double weightKg);
}

class StandardShipping implements ShippingStrategy {
  @override
  double calculateCost(double weightKg) => 4.90 + 0.50 * weightKg;
}

class ExpressShipping implements ShippingStrategy {
  @override
  double calculateCost(double weightKg) => 9.90 + 1.00 * weightKg;
}

class PickupShipping implements ShippingStrategy {
  @override
  double calculateCost(double weightKg) => 0.00;
}

class Order {
  final double weightKg;
  late ShippingStrategy _shippingStrategy;

  Order(this.weightKg);

  void setShippingStrategy(ShippingStrategy shippingStrategy) {
    _shippingStrategy = shippingStrategy;
  }

  double shippingCost() => _shippingStrategy.calculateCost(weightKg);
}

String formatEur(double amount) => '${amount.toStringAsFixed(2).replaceAll('.', ',')} EUR';

void main() {
  final order = Order(2.0);

  order.setShippingStrategy(StandardShipping());
  print('Standard: ${formatEur(order.shippingCost())}');

  order.setShippingStrategy(ExpressShipping());
  print('Express:  ${formatEur(order.shippingCost())}');

  order.setShippingStrategy(PickupShipping());
  print('Pickup:   ${formatEur(order.shippingCost())}');
}
