from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from controller.commonFunctions import pushNotification
from ui.ui_files import crudAccForm_ui

class CrudAccForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = crudAccForm_ui.Ui_MainWindow()
        self.ui.setupUi(self)

   
        self.ui.applyBtn.clicked.connect(self.applyAccBtn)

    def applyAccBtn(self):
        nameAcc = self.ui.nameAcc.text()
        username_email_Acc = self.ui.username_email_Acc.text()
        passwordAcc = self.ui.passwordAcc.text()
        proxyAcc = self.ui.proxyAcc.text()
        auth2faAcc = self.ui.auth2faAcc.text()
        cookiesAcc = self.ui.cookiesAcc.toPlainText()

        if username_email_Acc == "" or passwordAcc == "" :
            pushNotification("Vui lòng nhập đầy đủ thông tin")
            return
        
        
        
