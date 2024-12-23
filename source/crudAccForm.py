import asyncio
import sqlite3
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from controller.DBF import Database
from controller.commonFunctions import pushNotification
from ui.ui_files import crudAccForm_ui
# from source.homePage import HomePage

class CrudAccForm(QMainWindow):
    def __init__(self,homePage):
        super().__init__()
        self.ui = crudAccForm_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.homePage = homePage
        
   

        self.ui.applyBtn.clicked.connect(self.applyAccBtn)

    def applyAccBtn(self):
        name_profile = self.ui.nameAcc.text()
        username_email_Acc = self.ui.username_email_Acc.text()
        passwordAcc = self.ui.passwordAcc.text()
        proxyAcc = self.ui.proxyAcc.text()
        auth_fa = self.ui.auth2faAcc.text()
        cookie_insta = self.ui.cookiesAcc.toPlainText()
        user_agent = self.ui.useragentAcc.text()
        current_mode = self.homePage.modecccc 
        print(f"==>> current_mode: {current_mode}")
        

        if username_email_Acc == "":
            pushNotification("Vui lòng nhập đầy đủ thông tin")
            return
        
        try:
            asyncio.run(self.insertAccount(name_profile, username_email_Acc, passwordAcc, proxyAcc, auth_fa, cookie_insta, user_agent))  # Chạy hàm chèn dự án bất đồng bộ
            # pushNotification(success_message)  # Tự custom thông báo
            print("Thêm tài khoản thành công")
        except sqlite3.IntegrityError:
            pushNotification(f"Email đã tồn tại")
            return 
    
    async def insertAccount(self, nameAcc, username_email_Acc, passwordAcc, proxyAcc, auth2faAcc, cookie_insta, user_agent):
        db = await Database.get_instance()  # Lấy kết nối duy nhất
        await db.execute_write(f"INSERT INTO accountTable (name_profile, email, password, proxy, auth_fa, cookie_insta , user_agent) VALUES ('{nameAcc}', '{username_email_Acc}', '{passwordAcc}', '{proxyAcc}', '{auth2faAcc}', '{cookie_insta}', '{user_agent}');")
        

