package notification.impl;

import notification.MessageInterface;
import notification.NotificationFactory;

public class EmailNotification extends NotificationFactory {
    @Override
    protected MessageInterface createMessage() {
        return new EmailMessageImpl();
    }
}
