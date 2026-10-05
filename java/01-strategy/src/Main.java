public class Main {
    public static void main(String[] args) {
        Order order = new Order(2.0);

        order.setShippingStrategy(new StandardShipping());
        System.out.printf("Standard: %.2f EUR%n", order.shippingCost());

        order.setShippingStrategy(new ExpressShipping());
        System.out.printf("Express:  %.2f EUR%n", order.shippingCost());

        order.setShippingStrategy(new PickupShipping());
        System.out.printf("Pickup:   %.2f EUR%n", order.shippingCost());
    }
}
