from input_parser.iinput_parser import IInputParser
import argparse

class InputParser(IInputParser):
  """In charge of read, validate and parse input arguments.
  
  Attrs:
    _parser: Argument parsed to read command line data.
  """

  def __init__(self):
    self._parser = argparse.ArgumentParser()
    self._arguments = {}
    self._run()

  def _run(self):
    """Initializes the input parser."""
    self._add_parser_arguments(self._get_arguments_list())
    self._arguments = self._parser.parse_args()
    extra_arguments = self._calculate_extra_arguments()

  def _get_arguments_list(self):
    """Returns an array with the configuration for the scripts arguments."""
    return [
      {'name': 'script-path', 'required': True, 'dest': 'script_path'},
      {'name': 'run-command', 'dest': 'run_command'},
    ]

  def _add_parser_arguments(self, arguments):
    """Adds the script arguments to the parser.

    Args:
      arguments: List of script arguments with configuration to add to parser.
    """
    for argument in arguments:
      if self._is_valid_argument(argument):
        self._parser.add_argument(
            '--{name}'.format(name=argument.get('name')),
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

  def _calculate_extra_arguments(self):
    return True

  def get_input_params(self):
    return {}