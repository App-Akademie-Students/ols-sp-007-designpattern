from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None: ...


class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"E-Mail: {message}")


class SmsNotification(Notification):
    def send(self, message: str) -> None:
        print(f"SMS:    {message}")


class PushNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Push:   {message}")


class NotificationFactory:
    @staticmethod
    def create(channel: str) -> Notification:
        match channel:
            case "email":
                return EmailNotification()
            case "sms":
                return SmsNotification()
            case "push":
                return PushNotification()
            case _:
                raise ValueError(f"Unbekannter Kanal: {channel}")


def main() -> None:
    for channel in ["email", "sms", "push"]:
        notification = NotificationFactory.create(channel)
        notification.send("Ihre Bestellung ist unterwegs.")


if __name__ == "__main__":
    main()
