from script_manager.iscript_manager import IScriptManager
from subprocess import Popen, PIPE
import errno
import os
import pty


class DefaultScriptManager(IScriptManager):
  
  def __init__(self, config, message_sender):
    """Initializes and configure a default script manager.

    Args:
      config: Dictionary with info to run the script.
    """
    super().__init__(config, message_sender)

  def run_script(self):
    """Runs the script from the configuration data."""
    out_r, out_w = pty.openpty()
    p = Popen([self._run_command, self._script_path], stdout=out_w)
    os.close(out_w) 

    while True:
      try:
          output = os.read(out_r, 1000)
          print('Doing my thing!! ******************************')
          self._message_sender.send_message(output)
      except OSError as e:
          if e.errno != errno.EIO: raise
          output = b""
      if not output: break
