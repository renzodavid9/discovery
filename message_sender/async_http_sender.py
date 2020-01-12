from message_sender.imessage_sender import IMessageSender
import requests
from requests_futures.sessions import FuturesSession

class AsyncHttpSender(IMessageSender):
  
  _ENDPOINT = 'http://postman-echo.com/post'

  def __init__(self, config):
    """Creates a new http sender.
    
    Args:
      config: Endpoint data to make the http request.
    """
    self._endpoint = config.get('http_endpoint', self._ENDPOINT)

  
  def send_message(self, message):
    request_body = {
      'message': message
    }
    response = requests.post(url=self._endpoint, data=request_body)
