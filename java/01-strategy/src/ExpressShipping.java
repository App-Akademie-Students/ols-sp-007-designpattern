public class ExpressShipping implements ShippingStrategy {
    @Override
    public double calculateCost(double weightKg) {
        return 9.90 + 1.00 * weightKg;
    }
}
