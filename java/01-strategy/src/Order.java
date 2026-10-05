public class Order {
    private final double weightKg;
    private ShippingStrategy shippingStrategy;

    public Order(double weightKg) {
        this.weightKg = weightKg;
    }

    public void setShippingStrategy(ShippingStrategy shippingStrategy) {
        this.shippingStrategy = shippingStrategy;
    }

    public double shippingCost() {
        return shippingStrategy.calculateCost(weightKg);
    }
}
