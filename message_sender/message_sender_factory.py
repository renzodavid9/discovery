from message_sender.async_http_sender import AsyncHttpSender
from message_sender.rabbitmq_sender import RabbitMQSender

class MessageSenderFactory():
  """Is in charge to create the proper message sender.
  
  Attr:
    _message_senders: Dictionary with every sender available.
    _default_sender: Default sender in case any rule matches.

  TODO: Implement the factory properly following the pattern.
  """
  def __init__(self):
    """Creates a new message sender factory.
    
    Configures the rules for each case to return the proper message sender.
    """
    self._message_senders = self._get_message_senders_rules()
    self._default_sender = AsyncHttpSender

  def _get_message_senders_rules(self):
    """Creates a dictionary with the rules to use to instantiate a sender.

    Returns:
      A dictionary with the rules.
    """
    return {
      'http-async': AsyncHttpSender,
      'rabbitmq': RabbitMQSender,
    }

  def get_message_sender(self, rule, config):
    """Returns an instance of the proper message sender.
    
    Attrs:
      rule: Rule to match the proper message sender.
    """
    return self._message_senders.get(rule, self._default_sender)(config)