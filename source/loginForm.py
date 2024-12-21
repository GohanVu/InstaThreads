import json
from PyQt6.QtWidgets import *  # Import các lớp cần thiết từ PyQt6
from PyQt6.QtGui import *  # Import các lớp liên quan đến giao diện đồ họa
from PyQt6.QtCore import *  # Import các lớp liên quan đến lõi của PyQt6
from controller.commonFunctions import checkAndCreateLastLocation, pushNotification  # Import hàm thông báo
from source.homePage import HomePage  # Import trang chủ
from ui.ui_files import loginForm_ui  # Import giao diện đăng nhập

# Dữ liệu đăng nhập mặc định
dataLogin = {
    "username": "1",
    "password": "1"
}

class LoginForm(QMainWindow):  # Định nghĩa lớp LoginForm kế thừa từ QMainWindow
    def __init__(self):  # Hàm khởi tạo
        super().__init__()  # Gọi hàm khởi tạo của lớp cha
        self.ui = loginForm_ui.Ui_MainWindow()  # Tạo đối tượng giao diện
        self.ui.setupUi(self)  # Thiết lập giao diện
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)  # Thiết lập cửa sổ không có khung
        self.ui.closeBtn.clicked.connect(self.close)  # Kết nối nút đóng với hàm đóng cửa sổ
        self.ui.minimizeBtn.clicked.connect(self.showMinimized)  # Kết nối nút thu nhỏ với hàm thu nhỏ cửa sổ
        self.ui.closeBtn.setCursor(Qt.CursorShape.PointingHandCursor)  # Thiết lập con trỏ chuột cho nút đóng
        self.ui.minimizeBtn.setCursor(Qt.CursorShape.PointingHandCursor)  # Thiết lập con trỏ chuột cho nút thu nhỏ
        self.ui.loginBtn.setCursor(Qt.CursorShape.PointingHandCursor)  # Thiết lập con trỏ chuột cho nút đăng nhập

        
        self.ui.loginBtn.clicked.connect(self.login)  # Kết nối nút đăng nhập với hàm login   
        checkAndCreateLastLocation()
        self.setupLastLocation()
        
    def setupLastLocation(self):
        with open('./data/last_location/last_location.json', 'r+', encoding="utf-8") as f:
            data=json.load(f)
            self.ui.username.setText(data["username"])
            self.ui.password.setText(data["password"])
            if data["username"] != "" and data["password"] != "":
                self.ui.rememberLoginBtn.setChecked(True)
         
    def login(self):  # Hàm xử lý sự kiện đăng nhập
        username = self.ui.username.text()  # Lấy tên người dùng từ giao diện
        password = self.ui.password.text()  # Lấy mật khẩu từ giao diện
        print(username, password)  # In ra tên người dùng và mật khẩu (chỉ để kiểm tra)

        # Kiểm tra tên người dùng
        if username != dataLogin["username"]:
            pushNotification("Tên đăng nhập hoặc mật khẩu không đúng")  # Thông báo lỗi
            return
        # Kiểm tra mật khẩu
        if password != dataLogin["password"]:
            pushNotification("Tên đăng nhập hoặc mật khẩu không đúng")  # Thông báo lỗi
            return
        

        if not self.ui.rememberLoginBtn.isChecked():
            username = ""
            password = ""
            
        with open('./data/last_location/last_location.json', 'r+', encoding="utf-8") as f:
            data=json.load(f)
            data["username"] = username
            data["password"] = password
            f.seek(0)
            f.write(json.dumps(data))
            f.truncate()
                
        

        self.homePage = HomePage()  # Tạo đối tượng trang chủ
        self.homePage.show()  # Hiển thị trang chủ
        self.close()  # Đóng cửa sổ đăng nhập