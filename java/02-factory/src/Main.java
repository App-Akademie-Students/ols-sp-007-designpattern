public class Main {
    public static void main(String[] args) {
        for (String channel : new String[] {"email", "sms", "push"}) {
            Notification notification = NotificationFactory.create(channel);
            notification.send("Ihre Bestellung ist unterwegs.");
        }
    }
}
