import abc

class IScriptManager(metaclass=abc.ABCMeta):

  _DEFAULT_COMMAND = 'python3'

  def __init__(self, config: dict, message_sender):
    """Initializes and configure a new script manager.

    Args:
      config: Dictionary with info to run the script.
      message_sender: Message sender service.
    """
    self._run_command = ''
    self._script_path = ''
    self._message_sender = message_sender
    self._load_configuration(config)


  def _load_configuration(self, config):
    """Loads into local properties the data to run the script.

    Args:
      config: Dictionary with info to run the script.
    """
    self._run_command = config.get('run_command', self._DEFAULT_COMMAND)
    self._script_path = config.get('script_path')


  @abc.abstractmethod
  def run_script(self):
    """Runs a script according to the implementation."""
    pass
