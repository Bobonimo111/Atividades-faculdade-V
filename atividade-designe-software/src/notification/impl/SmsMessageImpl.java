package notification.impl;

import notification.MessageData;
import notification.MessageInterface;

public class SmsMessageImpl implements MessageInterface {
    private MessageData messageData;

    @Override
    public void setMessageData(MessageData messageData) {
        this.messageData = messageData;
    }

    @Override
    public void sendNotification() {
        if(messageData == null) {
            System.out.println("Valor invalido");
            return;
        }
        if(messageData.getTelefone() == null) {
            System.out.println("messageData.Telefone não pode ser nulo.");
            return;
        }
        if(messageData.getMessage() == null) {
            System.out.println("messageData.message não pode ser nulo.");
            return;
        }

        System.out.println("Sending notification...");
    }
}
