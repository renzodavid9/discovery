from input_parser.input_parser_factory import InputParserFactory

class InitializerWrapper():
  def __init__(self):
    parser = InputParserFactory.get_parser()
    arguments = parser.get_input_params()
    print(arguments)

if __name__ == '__main__':
  initializer = InitializerWrapper()