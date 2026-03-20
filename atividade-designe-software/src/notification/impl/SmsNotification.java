package notification.impl;

import notification.MessageInterface;
import notification.NotificationFactory;

public class SmsNotification extends NotificationFactory {
    @Override
    protected MessageInterface createMessage() {
        return new SmsMessageImpl();
    }
}
