import json
import os
import sqlite3
from PyQt6.QtWidgets import *  
from PyQt6.QtGui import *  
from PyQt6.QtCore import * 
import asyncio  
from controller.DBF import Database, fetch_all, fetch_one  
from controller.commonFunctions import pushNotification, pushYNQuestion  
from source.crudAccForm import CrudAccForm
from source.tableProfiles import TableProfiles
from ui.ui_files import homepage_ui  
from controller.constantTemplate import CONTENT_ATTRIBUTE_LIST, COLUMN_DISPLAY_HEADER, INSTAGRAM_MODE, THREADS_MODE, column_projectTable_index  
from source.switch_button import SwitchButton

class HomePage(QMainWindow):  
    def __init__(self): 
        super().__init__()  # Gọi hàm khởi tạo của lớp cha
        self.ui = homepage_ui.Ui_MainWindow()  # Tạo đối tượng giao diện người dùng
        self.ui.setupUi(self)  # Thiết lập giao diện người dùng
        self.tableProfiles = None
        asyncio.run(self.setupDatabase())  # Thiết lập cơ sở dữ liệu 
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)  # Thiết lập cửa sổ không có khung
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # Thiết lập nền trong suốt
        self.setupBtn()  # Thiết lập các nút dự án (Trên cùng homepage)
        self.setupSidebar()  # Thiết lập setup thanh bên
        self.setupMainContent()
        
        # Các nút sự kiện với dự án (trên cùng homepage)
        self.ui.addProjBtn.clicked.connect(self.addProject)  
        self.ui.deleteProjBtn.clicked.connect(self.deleteProject)
        self.ui.editProjBtn.clicked.connect(self.editProject)

        # Các nút sự kiện với tài khoản (giữa homepage)
        self.ui.addAccBtn.clicked.connect(self.addAcc)

        # Nút switch nền tảng (instagram/threads)
        self.switch = SwitchButton(self)
        self.switch.setObjectName('switchBtn')
        self.switch.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.switchLayoutBtn.addWidget(self.switch)

    # Hàm setup cơ sở dữ liệu----------------------------------
    async def setupDatabase(self): 
        self.db = await Database.get_instance('./data/coreData.db')  # Lấy kết nối cơ sở dữ liệu duy nhất
        db = await Database.get_instance()  # Lấy kết nối duy nhất

    # Tạo bảng projectTable nếu chưa tồn tại
        create_table_project = """
        CREATE TABLE IF NOT EXISTS projectTable (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL UNIQUE,
            project_browser TEXT DEFAULT 'gologin'
        );
        """
        await db.execute_write(create_table_project)  

    # Kiểm tra và thêm bản ghi mặc định nếu bảng trống
        check_and_insert_default_query = """
        INSERT INTO projectTable (project_name, project_browser)
        SELECT 'mặc định', 'gologin'
        WHERE NOT EXISTS (SELECT 1 FROM projectTable);
        """
        await db.execute_write(check_and_insert_default_query)  # Thực thi câu lệnh kiểm tra và thêm bản ghi mặc định
        
    # Tạo bảng accountTable nếu chưa tồn tại
        create_table_account = """
        CREATE TABLE IF NOT EXISTS accountTable (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name_account TEXT NULL,
            username_email_account TEXT NOT NULL UNIQUE,
            password_account TEXT NOT NULL,
            proxy_account TEXT,
            auth2fa_account TEXT,
            cookies_account TEXT
        );
        """
        await db.execute_write(create_table_account)

    # Tạo bảng contentHeadlines nếu chưa tồn tại
        create_table_content_headlines = """
        CREATE TABLE IF NOT EXISTS contentHeadlines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name_column TEXT NOT NULL UNIQUE,
            positon_column INTEGER NOT NULL DEFAULT 0
        );
        """
        await db.execute_write(create_table_content_headlines) 

    # Thêm các cột trong tablewidget (contentAttribute)
        for name_column in CONTENT_ATTRIBUTE_LIST:
            try:
                await self.insertContentAttribute(name_column) #Thêm cột
            except sqlite3.IntegrityError: #Nếu có lỗi
                pass #Bỏ qua lỗi
            
        await self.loadProject()  # Tải danh sách dự án
    
    # Hàm setup chủ đề (Instagram hoặc Threads)----------------------------------
    def setUpTheme(self, mode = INSTAGRAM_MODE):
        self.mode = mode
           
        if mode == INSTAGRAM_MODE:
            self.ui.body.setStyleSheet("""
                QWidget#body {  
                background: url(:/background/InstaBackground.jpg);  
                background-repeat: no-repeat; /* Đảm bảo hình không lặp lại */  
                background-position: left; /* Căn giữa hình nền */  
                background-size: cover; /* Resize hình nền để bao phủ toàn bộ widget */  
                border-top-left-radius: 0px; /* Không bo góc trên bên trái */
                border-top-right-radius: 0px; /* Không bo góc trên bên phải */
                border-bottom-left-radius: 10px; /* Bo góc dưới bên trái */
                border-bottom-right-radius: 10px; /* Bo góc dưới bên phải */
            }
            """)
        
        if mode == THREADS_MODE:
            self.ui.body.setStyleSheet("""
                QWidget#body {  
                background: url(:/background/threadsBackground.jpg);  
                background-repeat: no-repeat; /* Đảm bảo hình không lặp lại */  
                background-position: left; /* Căn giữa hình nền */  
                background-size: cover; /* Resize hình nền để bao phủ toàn bộ widget */  
                border-top-left-radius: 0px; /* Không bo góc trên bên trái */
                border-top-right-radius: 0px; /* Không bo góc trên bên phải */
                border-bottom-left-radius: 10px; /* Bo góc dưới bên trái */
                border-bottom-right-radius: 10px; /* Bo góc dưới bên phải */
            }
            """)

    # Hàm setup các nút liên quan đến dự án project (Trên cùng homepage)----------------------------------
    def setupBtn(self):  
        self.ui.addProjBtn.setCursor(Qt.CursorShape.PointingHandCursor)  # Thiết lập con trỏ chuột cho nút thêm dự án
        self.ui.editProjBtn.setCursor(Qt.CursorShape.PointingHandCursor)  # Thiết lập con trỏ chuột cho nút chỉnh sửa dự án
        self.ui.deleteProjBtn.setCursor(Qt.CursorShape.PointingHandCursor)  # Thiết lập con trỏ chuột cho nút xóa dự án
        self.ui.resetProjBtn.setCursor(Qt.CursorShape.PointingHandCursor)  # Thiết lập con trỏ chuột cho nút đặt lại dự án
        self.ui.minimizeBtnProj.setCursor(Qt.CursorShape.PointingHandCursor)  # Thiết lập con trỏ chuột cho nút thu nhỏ
        self.ui.scaleBtnProj.setCursor(Qt.CursorShape.PointingHandCursor)  # Thiết lập con trỏ chuột cho nút phóng to
        self.ui.closeBtnProj.setCursor(Qt.CursorShape.PointingHandCursor)  # Thiết lập con trỏ chuột cho nút đóng

    # Hàm setup thanh bên sidebar----------------------------------
    def setupSidebar(self): 
        self.ui.smallSidebar.hide()  # Ẩn thanh bên nhỏ
        self.isShowSmallSidebar = False  # Đặt trạng thái thanh bên nhỏ là ẩn
        self.ui.toggleSidebarBtn.clicked.connect(self.toggleSidebar)  # Kết nối nút chuyển đổi thanh bên với hàm toggleSidebar
        self.ui.homepageSidebar.setCursor(Qt.CursorShape.PointingHandCursor)  # Thiết lập con trỏ chuột cho thanh bên trang chủ
        self.ui.uploadSidebar.setCursor(Qt.CursorShape.PointingHandCursor)  
        self.ui.smallHomepageSidebar.setCursor(Qt.CursorShape.PointingHandCursor)  
        self.ui.smallUploadSidebar.setCursor(Qt.CursorShape.PointingHandCursor) 
        
        self.ui.homepageSidebar.clicked.connect(self.showHomepage)  # Kết nối thanh bên trang chủ với hàm showHomepage
        self.ui.uploadSidebar.clicked.connect(self.showUpload)  
        self.ui.smallHomepageSidebar.clicked.connect(self.showHomepage)  
        self.ui.smallUploadSidebar.clicked.connect(self.showUpload)  

    # Hàm setup switch thanh bên to nhỏ (sidebar)----------------------------------
    def toggleSidebar(self):  
        if self.isShowSmallSidebar:  # Kiểm tra nếu thanh bên nhỏ đang hiển thị
            self.ui.smallSidebar.hide()  
            self.ui.sidebar.show()  
            self.isShowSmallSidebar = False 
        else:
            self.ui.smallSidebar.show()  # Hiển thị thanh bên nhỏ
            self.ui.sidebar.hide()  
            self.isShowSmallSidebar = True  

    # Hàm hiển thị trang chủ (trang chủ sidebar)----------------------------------
    def showHomepage(self):  
        self.ui.stackedWidget.setCurrentIndex(0)  # Đặt chỉ mục hiện tại của stacked widget là 0 (trang chủ)

    # Hàm hiển thị trang tải lên (tải lên sidebar)----------------------------------
    def showUpload(self):  
        self.ui.stackedWidget.setCurrentIndex(1)  # Đặt chỉ mục hiện tại của stacked widget là 1 (tải lên)

    # Hàm setup giao diện chính giữa (tài khoản)----------------------------------
    def setupMainContent(self):
        # Thiết lập nội dung trên cùng (filter, search, add, delete, edit)
        def setupTopContent():
            # Combobox cho filter khi tìm kiếm(filter, search)
            for value in COLUMN_DISPLAY_HEADER.values():
                self.ui.categorySearch.addItem(value)
        # Thiết lập nội dung dưới cùng (tableProfiles)
        def setupBottomContent():
            self.tableProfiles = TableProfiles(self)
            self.ui.homepageDisplayLayout.addWidget(self.tableProfiles)

        setupTopContent()
        setupBottomContent()



    # Hàm thêm tài khoản----------------------------------
    def addAcc(self):
        self.crudAccForm = CrudAccForm()
        self.crudAccForm.show()


    # Hàm thêm dự án----------------------------------
    def addProject(self):  
        dialog = QDialog(self)  # Tạo hộp thoại mới
        dialog.setWindowIcon(QIcon(":/iconshortcut/IconShortcut.png"))  # Thiết lập biểu tượng cho hộp thoại
        dialog.setWindowTitle("Tạo dự án mới")  # Thiết lập tiêu đề cho hộp thoại
        dialog.setWindowModality(Qt.WindowModality.ApplicationModal)  # Thiết lập chế độ modal cho hộp thoại
        dialog.setFixedSize(300, 150)  # Thiết lập kích thước cố định cho hộp thoại

        layout = QVBoxLayout()  # Tạo layout dọc cho hộp thoại

        label = QLabel("Nhập tên dự án:")  # Tạo nhãn để hướng dẫn người dùng nhập tên dự án
        layout.addWidget(label)  # Thêm nhãn vào layout

        project_name_input = QLineEdit()  # Tạo ô nhập liệu cho tên dự án
        layout.addWidget(project_name_input)  # Thêm ô nhập liệu vào layout

        button_layout = QHBoxLayout()  # Tạo layout ngang cho các nút

        create_button = QPushButton("Tạo")  # Tạo nút "Tạo"
        create_button.setCursor(Qt.CursorShape.PointingHandCursor)  # Thiết lập con trỏ chuột cho nút
        create_button.clicked.connect(lambda: self.checkExitsProject(
            dialog, 
            project_name_input.text(), 
            f"Tạo dự án {project_name_input.text()} thành công"
        ))  # Kết nối nút với hàm tạo dự án
        button_layout.addWidget(create_button)  # Thêm nút vào layout

        cancel_button = QPushButton("Hủy")  # Tạo nút "Hủy"
        cancel_button.setCursor(Qt.CursorShape.PointingHandCursor) 
        cancel_button.clicked.connect(dialog.reject)  # Kết nối nút với hàm từ chối hộp thoại
        button_layout.addWidget(cancel_button)  # Thêm nút vào layout

        layout.addLayout(button_layout)  # Thêm layout nút vào layout chính
        dialog.setLayout(layout)  # Thiết lập layout cho hộp thoại
        dialog.exec()  # Hiển thị hộp thoại

    # Hàm chỉnh sửa dự án----------------------------------
    def editProject(self):
        project_name = self.ui.projectCombobox.currentText()
        if project_name == "mặc định":
            pushNotification("Không thể chỉnh sửa dự án mặc định")
            return
        
        dialog = QDialog(self)
        dialog.setWindowIcon(QIcon(":/iconshortcut/IconShortcut.png"))
        dialog.setWindowTitle("Chỉnh sửa dự án")
        dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        dialog.setFixedSize(300, 150)   
        
        button_layout = QVBoxLayout()
        label = QLabel("Nhập tên dự án:")
        button_layout.addWidget(label)
        project_name_input = QLineEdit()
        project_name_input.setText(project_name) 
        button_layout.addWidget(project_name_input)
        edit_button = QPushButton("Sửa")  # Tạo nút "Sửa"
        edit_button.setCursor(Qt.CursorShape.PointingHandCursor)  # Thiết lập con trỏ chuột cho nút
        edit_button.clicked.connect(lambda: self.checkExitsProject(
            dialog, 
            project_name_input.text(), 
            f"Sửa tên dự án thành công! Tên mới: {project_name_input.text()}"
        ))  # Kết nối nút với hàm tạo dự án
        button_layout.addWidget(edit_button)
        
        cancel_button = QPushButton("Hủy")  # Tạo nút "Hủy"
        cancel_button.setCursor(Qt.CursorShape.PointingHandCursor) 
        cancel_button.clicked.connect(dialog.reject)  # Kết nối nút với hàm từ chối hộp thoại
        button_layout.addWidget(cancel_button)
        
        dialog.setLayout(button_layout)
        dialog.exec()

    # Hàm xóa dự án----------------------------------
    def deleteProject(self):  
        async def deleteProjectAsync():  # Hàm bất đồng bộ để xóa dự án
            project_id = self.getProjectId()  # Lấy ID dự án
            print(f"==>> project_id: {project_id}")  # In ID dự án ra console
            await self.db.execute_write(f"DELETE FROM projectTable WHERE id = {project_id};")  # Xóa dự án khỏi cơ sở dữ liệu
            await self.loadProject()  # Tải lại danh sách dự án
            
        project_name = self.ui.projectCombobox.currentText()  # Lấy tên dự án hiện tại
        if project_name == "mặc định":  # Kiểm tra nếu dự án là "mặc định"
            pushNotification("Không thể xóa dự án mặc định") 
            return
        if pushYNQuestion(f"Bạn có chắc chắn muốn xóa dự án {project_name} không?"):  
            if pushYNQuestion(f"Việc này sẽ xóa toàn bộ tài khoản thuộc dự án {project_name} này?"): 
                if pushYNQuestion("Bạn đã suy nghĩ kỹ và muốn xóa, tiếp tục ? "):  
                    asyncio.run(deleteProjectAsync())  # Chạy hàm xóa dự án bất đồng bộ

    # Hàm kiểm tra tên dự án----------------------------------
    def checkExitsProject(self, dialog, project_name, success_message):  
        if len(project_name) < 3:  
            pushNotification("Tên dự án quá ngắn. Tên dự án phải có độ dài từ 3 đến 50 ký tự.") 
            return
        if len(project_name) > 50:  
            pushNotification("Tên dự án quá dài. Tên dự án phải có độ dài từ 3 đến 50 ký tự.")  
            return
        if '\n' in project_name:  
            pushNotification("Tên dự án không được chứa ký tự xuống dòng.")  
            return
        if not all(char.isalnum() or char.isspace() for char in project_name): 
            pushNotification("Tên dự án không được chứa ký tự đặc biệt.")  
            return
        
        async def insertProject():  # Hàm bất đồng bộ để chèn dự án vào cơ sở dữ liệu
            await self.db.execute_write(f"INSERT INTO projectTable (project_name) VALUES ('{project_name}');")  
            await self.loadProject()  # Tải lại danh sách dự án
        
        try:
            asyncio.run(insertProject())  # Chạy hàm chèn dự án bất đồng bộ
            pushNotification(success_message)  # Tự custom thông báo
        except sqlite3.IntegrityError:
            pushNotification(f"Tên dự án đã tồn tại")
            return 
        dialog.accept()  # Đóng hộp thoại
    # Hàm lấy ID dự án----------------------------------
    def getProjectId(self):  
        return self.ui.projectCombobox.currentData()  # Trả về dữ liệu hiện tại của combobox

    # Hàm tải danh sách dự án----------------------------------
    async def loadProject(self):  
        self.ui.projectCombobox.clear()  # Xóa tất cả các mục trong combobox
        project_records = await fetch_all("SELECT * FROM projectTable;")  # Lấy tất cả các bản ghi từ bảng projectTable
        
        for project in project_records:  # Duyệt qua từng bản ghi dự án
            project_id = project[column_projectTable_index["id"]]  # Lấy ID dự án
            project_name = project[column_projectTable_index["project_name"]]  # Lấy tên dự án
            self.ui.projectCombobox.addItem(project_name, project_id)  # Thêm tên dự án và ID vào combobox


    # Hàm thêm các cột trong tablewidget (contentAttribute)----------------------------------
    async def insertContentAttribute(self, name_column):
        # Fetch the current maximum value of positon_column
        max_position_query = "SELECT MAX(positon_column) FROM contentAttribute;"
        max_position_result = await fetch_one(max_position_query)
        
        # Ensure max_position_result is not None and extract the value
        max_position = max_position_result[0] if max_position_result and max_position_result[0] is not None else -1
        
        # Calculate the new position
        new_position = max_position + 1  # Start from 0 if no rows exist

        # Insert the new row with the calculated position
        insert_query = f"""
        INSERT INTO contentAttribute (name_column, positon_column)
        VALUES ('{name_column}', {new_position});
        """
        await self.db.execute_write(insert_query) 




    # Việc di chuyển cửa sổ----------------------------------
    def mousePressEvent(self, event): #Hàm  khi người dùng nhấn chuột
        if event.button() == Qt.MouseButton.LeftButton: #Kiểm tra nếu nhấn chuột trái
            self.moveFlag = True #Đặt trạng thái di chuyển là true
            self.movePosition = event.globalPosition() #Lưu vị trí chuột
            event.accept() #Chấp nhận sự kiện

    def mouseMoveEvent(self, event): #Hàm khi người dùng di chuyển chuột
        if Qt.MouseButton.LeftButton and self.moveFlag: #Kiểm tra nếu nhấn chuột trái và trạng thái di chuyển là true
            delta = event.globalPosition() - self.movePosition #Tính toán sự thay đổi vị trí
            new_pos = self.pos() + delta.toPoint() #Tính toán vị trí mới
            self.move(new_pos)  # Cập nhật vị trí của cửa sổ
            self.movePosition = event.globalPosition()  # Cập nhật vị trí gốc
            event.accept()

    def mouseReleaseEvent(self, QMouseEvent): #Hàm khi người dùng nhả chuột
        self.moveFlag = False #Đặt trạng thái di chuyển là false