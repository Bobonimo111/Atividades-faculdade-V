package notification;

public abstract class NotificationFactory {
    public void sendNotification(MessageData messageData) {
        MessageInterface notification = this.createMessage();
        notification.setMessageData(messageData);
        notification.sendNotification();
    }

    protected abstract MessageInterface createMessage();

}
