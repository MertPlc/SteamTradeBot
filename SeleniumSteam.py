import time
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QTextEdit, QLabel, QAction, QMessageBox, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from Tradebot import SteamTradeBot

class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.baslik = "Trade Bot"
        self.icon = QIcon(r"Icons\trade.png")
        self.sol = 500
        self.ust = 200
        self.width = 320
        self.height = 260
        self.stTrade = None
        self.Goster()
        

    def Goster(self):
        self.setWindowTitle(self.baslik)
        self.setGeometry(self.sol,self.ust,self.width,self.height)
        self.setMinimumSize(320,260)
        self.setMaximumSize(320,260)
        self.setWindowIcon(self.icon)
        self.statusBar().showMessage("Çalışıyor") 
        menu = self.menuBar()
               
        hakkindaMenu = menu.addMenu("Hakkında")
        hakkinda = QAction("Hakkında",self)
        hakkindaMenu.addAction(hakkinda)
        hakkinda.triggered.connect(self.Hakkinda)

        self.username = QLineEdit(self)
        self.userLabel = QLabel(self)
        self.userLabel.setText("Kullanıcı Adı:")
        self.userLabel.move(30,52)
        self.username.setPlaceholderText("Kullanıcı Adı")
        self.username.move(100,60)
        self.username.resize(120,20)
        

        self.sifre = QLineEdit(self)
        self.sifreLabel = QLabel(self)
        self.sifreLabel.setText("Şifre:")
        self.sifreLabel.move(30,83)
        self.sifre.setEchoMode(QLineEdit.Password)
        self.sifre.setPlaceholderText("Şifre")
        self.sifre.move(100,90)
        self.sifre.resize(120,20)

        self.girisDugme = QPushButton("Giriş Yap",self)
        self.girisDugme.move(110,130)
        #self.girisDugme.setIcon(QIcon("Icons\steam.png"))

        self.tradeDugme = QPushButton("Auto Trade",self)
        self.tradeDugme.move(110,170)
        self.tradeDugme.setIcon(QIcon(r"Icons\tradeicon.png"))
        
        
        self.girisDugme.clicked.connect(self.Git)
        self.tradeDugme.clicked.connect(self.AutoTrade)

        self.show()
        
    def Git(self):
        self.stTrade = SteamTradeBot(self.username.text(),self.sifre.text())
        
    def AutoTrade(self):
        self.stTrade.autoTrade()
        
    def Hakkinda(self):
        QMessageBox.information(self,"Hakkında", "Casper")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())
