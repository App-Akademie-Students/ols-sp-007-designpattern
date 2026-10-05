// JavaScript kennt kein Interface: Eine Strategie ist jedes Objekt mit einer Methode calculateCost(weightKg)
class StandardShipping {
  calculateCost(weightKg) {
    return 4.9 + 0.5 * weightKg;
  }
}

class ExpressShipping {
  calculateCost(weightKg) {
    return 9.9 + 1.0 * weightKg;
  }
}

class PickupShipping {
  calculateCost(weightKg) {
    return 0.0;
  }
}

class Order {
  constructor(weightKg) {
    this.weightKg = weightKg;
    this.shippingStrategy = null;
  }

  setShippingStrategy(shippingStrategy) {
    this.shippingStrategy = shippingStrategy;
  }

  shippingCost() {
    return this.shippingStrategy.calculateCost(this.weightKg);
  }
}

function formatEur(amount) {
  return amount.toFixed(2).replace(".", ",") + " EUR";
}

function main() {
  const order = new Order(2.0);

  order.setShippingStrategy(new StandardShipping());
  console.log(`Standard: ${formatEur(order.shippingCost())}`);

  order.setShippingStrategy(new ExpressShipping());
  console.log(`Express:  ${formatEur(order.shippingCost())}`);

  order.setShippingStrategy(new PickupShipping());
  console.log(`Pickup:   ${formatEur(order.shippingCost())}`);
}

main();
