abstract interface class Notification {
  void send(String message);
}

class EmailNotification implements Notification {
  @override
  void send(String message) => print('E-Mail: $message');
}

class SmsNotification implements Notification {
  @override
  void send(String message) => print('SMS:    $message');
}

class PushNotification implements Notification {
  @override
  void send(String message) => print('Push:   $message');
}

class NotificationFactory {
  static Notification create(String channel) {
    return switch (channel) {
      'email' => EmailNotification(),
      'sms' => SmsNotification(),
      'push' => PushNotification(),
      _ => throw ArgumentError('Unbekannter Kanal: $channel'),
    };
  }
}

void main() {
  for (final channel in ['email', 'sms', 'push']) {
    final notification = NotificationFactory.create(channel);
    notification.send('Ihre Bestellung ist unterwegs.');
  }
}
