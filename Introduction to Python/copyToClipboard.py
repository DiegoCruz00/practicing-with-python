import sys
import subprocess

def copy(s):
    if sys.platform == 'win32' or sys.platform == 'cygwin':
        subprocess.Popen(['clip'], stdin=subprocess.PIPE, encoding="utf-8").communicate(s)
    else:
        raise Exception('Platform not supported')
