import abc

class IMessageSender(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def __init__(self, config: dict):
    """Initializes and configure a new message sender."""
    pass

  @abc.abstractmethod
  def send_message(self, message: str):
    """Sends a message according to the implementation."""
    pass
