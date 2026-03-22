package notification;

public abstract class NotificationFactory {
    public void sendNotification(MessageData messageData) {

        if(messageData == null) {
            System.out.println("Valor invalido");
            return;
        }
        if(messageData.getMessage() == null) {
            System.out.println("messageData.message não pode ser nulo.");
            return;
        }

        MessageInterface notification = this.createMessage();
        notification.setMessageData(messageData);
        notification.sendNotification();
    }

    protected abstract MessageInterface createMessage();

}
