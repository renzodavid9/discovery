from input_parser.iinput_parser import IInputParser
import argparse

class CommandLineParser(IInputParser):
  """Is in charge of read, validate and parse command line arguments.
  
  Attrs:
    _parser: Command line arguments parser.
    _argument: Dictionary with parsed input.
  """

  def __init__(self):
    """Class constructor."""
    self._parser = argparse.ArgumentParser()
    self._arguments = {}
    self._run()


  def _run(self):
    """Parses the command line input."""
    self._add_arguments_to_parser(self._get_arguments_list())
    self._arguments = self._get_arguments_dictionary()


  def _get_arguments_list(self):
    """Returns an array with the configuration for the script's arguments."""
    return [
      {'name': '--script-path', 'required': True, 'dest': 'script_path'},
      {'name': '--run-command', 'dest': 'run_command'},
      {'name': '--sender-type', 'dest': 'sender_type'},
      {'name': '--http-endpoint', 'dest': 'http_endpoint'},
    ]


  def _add_arguments_to_parser(self, arguments):
    """Adds the script arguments to the parser.

    Args:
      arguments: List of script arguments with configuration to add to parser.
    """
    for argument in arguments:
      if self._is_valid_argument(argument):
        self._parser.add_argument(
            argument.get('name'),
            dest=argument.get('dest'),
            required=argument.get('required', False)
        )


  def _is_valid_argument(self, argument):
    """Determines if the given argument has the required configuration keys.

    Args:
      argument: Dicitonary with an argument configuration.
    
    Returns:
      True if the argument has all the required data.
    """
    return bool(argument.get('name')) and bool(argument.get('dest'))


  def _get_arguments_dictionary(self):
    """Returns the command line inputs in a dictionary."""
    arguments_list = vars(self._parser.parse_args()).items()
    return {
      key: value for (key, value) in arguments_list if value
    }


  def get_input_params(self):
    """Returns the list of arguments used to run the script."""
    return self._arguments