from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from deritradeterminal.util.deribit_api import RestClient
from deritradeterminal.managers.ConfigManager import ConfigManager

class MarketSellThread(QThread):

    signeler = pyqtSignal(bool,str,str) 

    def processOrder(self):

        try:
            config = ConfigManager.get_config()

            client = RestClient(config.tradeApis[self.accountid][0], config.tradeApis[self.accountid][1], ConfigManager.get_config().apiUrl)
            client.sell(ConfigManager.get_config().tradeInsturment, float(self.amount), 0, "market")
        
            self.signeler.emit(True, "Market Sell Order Success", "Market Sell On Account: " + str(self.accountid) + " For Amount: " + str(self.amount))

        except Exception as e:
        	
            self.signeler.emit(False, "Market Sell Order Error" , "Failed to market sell on " + str(self.accountid) + " for amount: " + str(self.amount) + "\n" + str(e))

    def __init__(self, accountid, amount):
        QThread.__init__(self)
        self.accountid = accountid
        self.amount = amount

    def run(self):
        self.processOrder()
