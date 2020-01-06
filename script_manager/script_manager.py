from subprocess import Popen, PIPE
import errno
import os
import pty

COMMAND = 'python3'
SCRIPT_PATH = 'C:\Desarrollo\PythonExercises\py_script_manager\script.py'
SCRIPT_PATH = '/var/development/script_manager/script.py'

def run():
  out_r, out_w = pty.openpty()
  p = Popen([COMMAND, SCRIPT_PATH], stdout=out_w)
  os.close(out_w) 

  while True:
    try:
        output = os.read(out_r, 1000)
        print(output)
        print('Doing my thing!! ******************************')
    except OSError as e:
        if e.errno != errno.EIO: raise
        output = b""
    if not output: break

if __name__ == "__main__":
  run()