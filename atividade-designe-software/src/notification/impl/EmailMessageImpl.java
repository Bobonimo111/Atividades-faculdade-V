package notification.impl;

import notification.MessageData;
import notification.MessageInterface;

public class EmailMessageImpl implements MessageInterface {

    private MessageData messageData;

    @Override
    public void setMessageData(MessageData messageData) {
        this.messageData = messageData;
    }

    @Override
    public void sendNotification() {
        if(this.messageData.getEmail() == null) {
            System.out.println("messageData.email não pode ser nulo.");
            return;
        }
        System.out.println("Conectando ao servidor de Emails");
        System.out.println("Enviando email|!!" + messageData.getEmail());
    }
}
