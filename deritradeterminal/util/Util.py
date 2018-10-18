import os
import sys
import logging
import logging.handlers
from datetime import datetime

from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Util:

    banner = '''
______          _ _____ _          _ _ 
|  _  \\        (_)  ___| |        | | |
| | | |___ _ __ _\\ `--.| |__   ___| | |
| | | / _ \\ '__| |`--. \\ '_ \\ / _ \\ | |
| |/ /  __/ |  | /\\__/ / | | |  __/ | |
|___/ \\___|_|  |_\\____/|_| |_|\\___|_|_|

'''

    firstRun = True

    logger = None

    @staticmethod
    def set_up_logging():
      file_path = sys.modules[__name__].__file__
      project_path = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
      log_location = project_path + '/logs/'
      if not os.path.exists(log_location):
          os.makedirs(log_location)

      current_time = datetime.now()
      current_date = current_time.strftime("%Y-%m-%d")
      file_name = current_date + '.log'
      file_location = log_location + file_name
      with open(file_location, 'a+'):
          pass

      logger = logging.getLogger(__name__)
      format = '[%(asctime)s] [%(levelname)s] %(message)s'
      logging.basicConfig(format=format, level=logging.INFO)
      return logger

    @staticmethod
    def get_logger():
      if Util.firstRun:
        Util.firstRun = False
        Util.logger = Util.set_up_logging()
        return Util.logger
      else:
        return Util.logger

    @staticmethod
    def clear_screen():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def safe_str_split_on_space(tosplit):
      if not tosplit:
        return []
      else:
        return tosplit.split(' ')
    
    @staticmethod
    def show_info_dialog(parent, title, text):
      
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Information)

       msg.setText(text)
       msg.setWindowTitle(title)
       p = parent.frameGeometry().center() - QtCore.QRect(QtCore.QPoint(), msg.sizeHint()).center()
       msg.move(p)
       msg.exec_()

    @staticmethod
    def show_error_dialog(parent, title, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        msg.setText(text)
        msg.setWindowTitle(title)
        p = parent.frameGeometry().center() - QtCore.QRect(QtCore.QPoint(), msg.sizeHint()).center()
        msg.move(p)
        msg.exec_()

    @staticmethod
    def percentageOf(part, whole):
        return 100 * float(part)/float(whole)


