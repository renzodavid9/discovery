from input_parser.input_parser import InputParser

class InputParserFactory():
  @staticmethod
  def get_parser():
    return InputParser()