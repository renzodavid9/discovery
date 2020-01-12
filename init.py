from input_parser.input_parser_factory import InputParserFactory
from message_sender.message_sender_factory import MessageSenderFactory
#from script_manager.script_manager_factory import 

class InitializerWrapper():
  def __init__(self, messageSenderFactory):
    parser = InputParserFactory.get_parser()
    arguments = parser.get_input_params()
    message_sender = messageSenderFactory.get_message_sender(
        arguments.get('sender_type'),
        arguments)
    message_sender.send_message('Hello HTTP')
    print('End!')
    
if __name__ == '__main__':
  initializer = InitializerWrapper(MessageSenderFactory())