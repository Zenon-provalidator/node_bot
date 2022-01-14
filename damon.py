import daemon
from daemon.pidfile import PIDLockFile
import logging
from logging import handlers

#test
import threading
import time

_logger = logging.getLogger("mylogger")
_logger.setLevel(logging.INFO)

file_handler = handlers.RotatingFileHandler(
    "log/daemon.log",
    maxBytes= (1024 * 1024 * 512), # 512GB
    backupCount=3
)
_logger.addHandler(file_handler)

# ... 중략 ..

context = daemonDaemonContext(pidfile=pidLockfile)
logfile_fileno = file_handler.stream.fileno()
context.files_preserve = [logfile_fileno]
with context:
   main_program()
   
   
def main_program():    
    threading.Timer(2.5, print('test')).start()