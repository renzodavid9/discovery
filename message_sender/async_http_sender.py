from message_sender.imessage_sender import IMessageSender
import requests
from requests_futures.sessions import FuturesSession


class AsyncHttpSender(IMessageSender):
  
  _DEFAULT_ENDPOINT = 'http://postman-echo.com/post'

  def __init__(self, config):
    """Creates a new http sender.
    
    Args:
      config: Endpoint data to make the http request.
    """
    self._endpoint = config.get('http_endpoint', self._DEFAULT_ENDPOINT)
    self._session = FuturesSession()

  
  def _get_message_to_send(self, message):
    """Creates the body message to send over HTTP.

    Args:
      message: Main message to send.
    
    Returns:
      A message dictionary to be send over HTTP.
    """
    return {
      'message': message,
    }


  def send_message(self, message):
    """Sends an async HTTP post messag to the _endpoint.

    Args:
      message: Main message to send.
    """
    request_body = self._get_message_to_send(message)
    self._session.get(url=self._endpoint, data=request_body)
    print('Sending...' + str(message))
