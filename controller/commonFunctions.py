import json
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import hashlib  



def hash_string(input_string):  
    """Hàm băm chuỗi đầu vào."""  
    # Sử dụng SHA-256 để băm chuỗi  
    hash_object = hashlib.sha256(input_string.encode())  
    return hash_object.hexdigest()  

def unhash_string(hashed_string):  
    """Hàm ngược lại không thể thực hiện được với các hàm băm như SHA-256."""  
    raise NotImplementedError("Hàm băm không thể được đảo ngược.")  



def pushNotification(title):
    if title == '':
        return
    msg = QMessageBox()
    icon = QIcon()
    icon.addPixmap(QPixmap(":/iconshortcut/IconShortcut.png"), QIcon.Mode.Normal, QIcon.State.Off)
    msg.setWindowIcon(icon)
    msg.setWindowTitle('Thông báo!')
    msg.setTextFormat(Qt.TextFormat.RichText)
    msg.setText(title)
    msg.activateWindow()
    msg.exec()
    return

def pushYNQuestion(msg):
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Thông báo")
    msg_box.setText(msg)
    msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

    # Set the icon of the dialog
    msg_box.setWindowIcon(QIcon(":/iconshortcut/IconShortcut.png"))

    button_reply = msg_box.exec()

    if button_reply == QMessageBox.StandardButton.Yes:
        return True
    else:
        return False
    
def checkAndCreateLastLocation():
    last_location_path = './data/last_location/last_location.json'
    last_location_folder  = './data/last_location'
    if not os.path.exists(last_location_folder):
        os.makedirs(last_location_folder)
    
    if not os.path.exists(last_location_path):
        default_data = {
            "username": "",
            "password": "",
        }
        with open(last_location_path, 'w', encoding="utf-8") as f:
            f.write(json.dumps(default_data))