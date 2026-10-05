class EmailNotification {
  send(message) {
    console.log(`E-Mail: ${message}`);
  }
}

class SmsNotification {
  send(message) {
    console.log(`SMS:    ${message}`);
  }
}

class PushNotification {
  send(message) {
    console.log(`Push:   ${message}`);
  }
}

class NotificationFactory {
  static create(channel) {
    switch (channel) {
      case "email":
        return new EmailNotification();
      case "sms":
        return new SmsNotification();
      case "push":
        return new PushNotification();
      default:
        throw new Error(`Unbekannter Kanal: ${channel}`);
    }
  }
}

function main() {
  for (const channel of ["email", "sms", "push"]) {
    const notification = NotificationFactory.create(channel);
    notification.send("Ihre Bestellung ist unterwegs.");
  }
}

main();
