from input_parser.command_line_parser import CommandLineParser

class InputParserFactory():
  """Is in charge to create the proper input parser
  
  TODO: Implement the factory properly following the pattern.
  """
  @staticmethod
  def get_parser():
    """Returns an instance of the proper input parser."""
    return CommandLineParser()