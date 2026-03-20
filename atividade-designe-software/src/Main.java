import notification.MessageData;
import notification.NotificationFactory;
import notification.impl.SmsNotification;

public class Main {
    public static void main(String[] args) {
        NotificationFactory not = new SmsNotification();
        MessageData message = new MessageData();

        message.setMessage("Hello World");
        message.setTelefone("999999999");

        not.sendNotification(message);
    }
}