from message_sender.imessage_sender import IMessageSender

class RabbitMQSender(IMessageSender):
  def __init__(self, config):
    """Creates a new RabbitMQ sender.
    
    Args:
      config: Endpoint data to connect with RabbitMQ queue.
    """
    print('RabbitMQ')


  def send_message(self, message):
    print(messasge)