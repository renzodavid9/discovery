from input_parser.input_parser_factory import InputParserFactory

class Main():
  def __init__(self):
    InputParserFactory.get_parser()

if __name__ == '__main__':
  main = Main()