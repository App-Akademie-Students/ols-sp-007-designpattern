public class StandardShipping implements ShippingStrategy {
    @Override
    public double calculateCost(double weightKg) {
        return 4.90 + 0.50 * weightKg;
    }
}
