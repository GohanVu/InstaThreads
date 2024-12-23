import asyncio
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from controller.DBF import Database, fetch_all
from controller.commonFunctions import hash_string

class TableProfiles(QTableWidget):
    def __init__(self, homePage):
        super().__init__()
        self.homePage = homePage
        self.setShowGrid(False) #Ẩn lưới của bảng
        self.setAlternatingRowColors(True) #Đặt màu xen kẽ các hàng

        # Lấy nội dung của các cột từ cơ sở dữ liệu
        header_labels = asyncio.run(self.fetch_content_headlines())
        # self.setHorizontalHeaderLabels(header_labels)
        self.hashed_position = {} #Tạo một từ điển để lưu trữ vị trí của các cột đã băm
        name_column = [] #Tạo một mảng để lưu trữ tên của các cột
        for header in header_labels:
            column_name = header[1]
            hashed_column_name = hash_string(column_name)
            column_position = header[2]
            self.hashed_position[hashed_column_name] = column_position
            name_column.append(column_name)


        self.setColumnCount(len(header_labels))
        self.setHorizontalHeaderLabels(name_column) 
        self.setStyleSheet("""
            
            QTableWidget{
                color:white;
                border:none;
                font: 500 9pt "Be Vietnam Pro";
                           
            }
            
            QTableView
            {
                color: #1f3044;
                gridline-color: red;
                border-left: 0;
                border-right: 0;

            }
            QTableView::item
            { 
                background-color: #f1f1f1;
          
            }
                           
            QTableView::item:alternate {
                background-color: white;
            
            }
            QTableWidget::item:selected {
                background-color: lightblue;
            }

            QScrollBar:horizontal  
            {
                height: 12px;
                background:#1f3044;
            }
        
        """)
        self.horizontalHeader().setStyleSheet("""
            QHeaderView{
                background: #1f3044;
               
            }
            QHeaderView::section {
                background-color: #1f3044;
                color: white;          
                font: 600 9pt "Be Vietnam Pro";
                border: none;
                border-left: none;
                border-right: none;
            }
            
        """)
        self.verticalScrollBar().setStyleSheet("QScrollBar:vertical { width: 10px;}")
        self.verticalHeader().setVisible(False)
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

       
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.itemSelectionChanged.connect(self.on_select_row)
        self.setup_column_width()

    def setup_column_width(self):
        self.setColumnWidth(self.hashed_position[hash_string('STT')], 25)
        self.setColumnWidth(self.hashed_position[hash_string('Tên Tài Khoản')], 150)
        self.setColumnWidth(self.hashed_position[hash_string('Ảnh')], 35)
        self.setColumnWidth(self.hashed_position[hash_string('ID Tài Khoản')], 150)
        self.setColumnWidth(self.hashed_position[hash_string('Email')], 200)
        self.setColumnWidth(self.hashed_position[hash_string('Cookie')], 200)
        self.setColumnWidth(self.hashed_position[hash_string('Last Active')], 100)
        self.setColumnWidth(self.hashed_position[hash_string('Ghi Chú')], 100)
        self.setColumnWidth(self.hashed_position[hash_string('Tổng like')], 50)
        self.setColumnWidth(self.hashed_position[hash_string('Tổng share')], 50)
        self.setColumnWidth(self.hashed_position[hash_string('Tổng video')], 50)




        self.hideColumn(self.hashed_position[hash_string('Tổng like')])
        self.hideColumn(self.hashed_position[hash_string('Tổng share')])
        self.hideColumn(self.hashed_position[hash_string('Tổng video')])
       
       
        
    def on_select_row(self):
        self.unique_arr = []
        selected_rows = [index.row() for index in self.selectedIndexes()]
        # self.unique_arr = [index.row() for index in self.selectedIndexes()]
        # print(f"==>> self.unique_arr: {self.unique_arr}")
        self.unique_arr = list(set(selected_rows))       

    async def fetch_content_headlines(self):
        query = "SELECT * FROM contentHeadlines;"
        db = await Database.get_instance()  # Get the singleton database instance
        async with db.connection.execute(query) as cursor:
            return await cursor.fetchall()
        
class ProfilesTableWidget(QTableWidget):
    
    def __init__(self,mainWd ):#HomeWindowUI
        super().__init__()
        
        self.setWindowIcon(QIcon(":/logo/icon-sw.png"))
        self.mainWd = mainWd
        self.setShowGrid(False)
        self.setAlternatingRowColors(True)
        self.setStyleSheet("""
            
            QTableWidget{
                color:white;
                border:none;
                font: 500 9pt "Be Vietnam Pro";
                           
            }
            
            QTableView
            {
                color: #1f3044;
                gridline-color: red;
                border-left: 0;
                border-right: 0;

            }
            QTableView::item
            { 
                background-color: #f1f1f1;
          
            }
                           
            QTableView::item:alternate {
                background-color: white;
            
            }
            QTableWidget::item:selected {
                background-color: lightblue;
            }

            QScrollBar:horizontal  
            {
                height: 12px;
                background:#1f3044;
            }
        """)
        self.setColumnCount(18)
        self.setHorizontalHeaderLabels(
            [
            '#',
            'Tên hồ sơ',
            'ID Kênh',
            '', 
            '',
            'Proxy',
            'Tổng view',
            'Tổng follower',
            'Tổng like',
            'Tổng share',
            'Tổng video',
            'Email',
            'Dự án',
            'Thư mục upload',
            'Note',
            'Cookie',
            'Last upload time',
            'ID Uploader'
        ])
        # Align the headers to the left
        for col in range(self.columnCount()):
            header_item = self.horizontalHeaderItem(col)
            header_item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Replace the text in the 3rd and 4th columns with icons
        icon3 = QIcon(":/icons/switchinsta.png")  # Replace with your own icon path
        icon4 = QIcon(":/icons/switchthreads.png")  # Replace with your own icon path
        
        # header_item_3 = QTableWidgetItem()
        # header_item_3.setIcon(icon3)
        # header_item_3.setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        # self.setHorizontalHeaderItem(3, header_item_3)
        
        # header_item_4 = QTableWidgetItem()
        # header_item_4.setIcon(icon4)
        # header_item_4.setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        # self.setHorizontalHeaderItem(4, header_item_4)

        header = CustomHeader(Qt.Orientation.Horizontal, self)
        self.setHorizontalHeader(header)
        header.setIcon(3, icon3)
        header.setIcon(4, icon4)
        
        self.setColumnWidth(0,25)
        self.setColumnWidth(1,171)
        
        self.setColumnWidth(2,190)
        self.setColumnWidth(3,10)
        self.setColumnWidth(4,10)
        self.setColumnWidth(5,125)
        
        self.hideColumn(8)
        self.hideColumn(9)
        self.hideColumn(10)
        self.hideColumn(17)
        self.hideColumn(12)
        self.setColumnWidth(13,180)
        # self.setColumnWidth(14,280)
 
        # self.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)
        self.horizontalHeader().setStyleSheet("""
            QHeaderView{
                background: #1f3044;
               
            }
            QHeaderView::section {
                background-color: #1f3044;
                color: white;          
                font: 600 9pt "Be Vietnam Pro";
                border: none;
                border-left: none;
                border-right: none;
            }
            
        """)
        self.verticalScrollBar().setStyleSheet("QScrollBar:vertical { width: 10px;}")
        self.verticalHeader().setVisible(False)
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        # self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
       
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.itemSelectionChanged.connect(self.on_select_row)
        # self.itemDoubleClicked.connect(self.on_click_item)

        self.unique_arr = []
        self.openSession = {}
        self.viewStatisticSessions = {}
        self.accountHelpers = {}
        self.accountHelpersItemTable = {}
        self.loginThreadsLD = {}
        self.loginThreadsCookies = {}
        self.loginThreadsBrowser = {}
        self.raiseThreadsBrowser = {}
        self.raiseProjects = {}
        self.changeInfoThreads = {}
        self.threadCookie = {}
        self.rasingThreads = {}
        self.openLdThread = {}
        self.changingThreadsBrowser = {}
        self.screenWindow = None
        self.isLoggin = False
        self.isRaisin = False
        self.logginScreen = None
        self.raiseThread = None
        self.changingScreen = None
        self.isResizingHeader = False
        self.isResizingVertical = False
        # self.event_filter = RowHeightChangeEventFilter()
        # self.event_filter.rowHeightChanged.connect(self.on_size_changed)
        # self.rowHeightChanged
        # self.viewport().installEventFilter(self.event_filter)
        # self.verticalHeader().sectionResized.connect(
        #     self.row_resized)
        # self.horizontalHeader().sectionResized.connect(
        #     self.row_resized_header) 

    def row_resized_header(self, index, old_size, new_size):
        # print(f"==>> index: {index}")
        # print(f"==>> old_size: {old_size}")
        # print(f"==>> new_size: {new_size}")
        if self.isResizingVertical:
            return

        self.isResizingHeader = True
        for i in range(self.verticalHeader().count()):
            rowheight = self.rowHeight(i)
            # self.row_resized(index=i,new_size= new_size)
            rowheight = rowheight+(new_size-old_size)
            
            self.setRowHeight(i, rowheight)

            # avt:QWidget = self.cellWidget(i,0)
            # label = avt.findChild(QLabel)
            # label.setFixedSize(old_size,old_size)
        self.isResizingHeader = False

    def row_resized(self, index, old_size, new_size):
        # print(f"==>> index: {index}")
        # print(f"==>> old_size: {old_size}")
        # print(f"==>> new_size: {new_size}")
        if self.isResizingHeader:
            return
        self.isResizingVertical = True
        for i in range(self.verticalHeader().count()):
            
            # avt.setFixedSize(old_size,old_size)
            self.setRowHeight(i, new_size)
            # thread = threading.Thread(target=self.setRowHeight,args=(i, new_size,))
            # thread.start()
            # avt:QWidget = self.cellWidget(index,0)
            # label = avt.findChild(QLabel)
            # print(f"==>> label: {label.objectName()}")
        self.isResizingVertical = False
    
    def on_size_changed(self, row, column):
        print(f"Cell at row {row} and column {column} size changed")

    def on_click_item(self,item):
        self.mainWd.openEditProfileWindow(item.row())

    def on_select_row(self):
        self.unique_arr = []
        selected_rows = [index.row() for index in self.selectedIndexes()]
        # self.unique_arr = [index.row() for index in self.selectedIndexes()]
        # print(f"==>> self.unique_arr: {self.unique_arr}")
        self.unique_arr = list(set(selected_rows))

    def generate_random_string(self,length):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def updateIDFromTiktokServer(self):
      
        thisTable = self
        class getUniqueIDThread(QThread):
            update_id_signal = pyqtSignal(int,str)
            update_avt_signal = pyqtSignal(int,str)
            def __init__(self) -> None:
                super().__init__()

            def run(self):
                conn = sqlite3.connect('./data/profilesDATA.db')
                cursor = conn.cursor()
                for i, indexTarget in enumerate(thisTable.unique_arr):
                    uore = thisTable.item(indexTarget, EMAIL_INDEX).text()
                    print(f"==>> uore: {uore}")
                    cursor.execute("SELECT * FROM profilesTableInstagram WHERE uore = ?", (uore,))
                    record = cursor.fetchone()
                    self.cookie = record[20]
                    proxy = record[15]
                    try:
                        proxy = proxy.split(':')
                        proxies = {
                        'http': f'http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}',
                        'https': f'http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}'
                        }
                    except:
                        proxies = None
                  
                    headers = {
                        'authority': 'www.tiktok.com',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'vi',
                        'cache-control': 'max-age=0',
                        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
                        'cookie': self.cookie,
                    }
                    url = random.choice(['https://www.tiktok.com/','https://www.tiktok.com/live'])
                    rs = requests.get(url,headers=headers,proxies=proxies)
                    match = re.search(r'"uniqueId":"(.*?)","createTime"', rs.text)
                    if match:
                        uniqueId = match.group(1)
                        sql_query = '''UPDATE profilesTableInstagram 
                            SET username_on_tiktok = ? WHERE uore = ?'''
                        cursor.execute(sql_query, (uniqueId, uore))
                        conn.commit()
                        self.update_id_signal.emit(indexTarget,uniqueId)
                        
                    matchFull = re.compile(
                        r"<script id=\"__UNIVERSAL_DATA_FOR_REHYDRATION__\" type=\"application/json\">(.*?)</script>"
                    ).search(str(rs.text))
                    # with open('CHECKPR.txt','w',encoding='utf-8') as f:
                    #     f.write(rs.text)

                    data = json.loads(matchFull.group(1))
                    try:
                        avturl = data["__DEFAULT_SCOPE__"]['webapp.user-detail']['userInfo']['user']['avatarThumb']
                    except:
                        avturl = data["__DEFAULT_SCOPE__"]['webapp.app-context']['user']['avatarUri'][0]
                    # response = requests.get(avturl)
                    randchar = thisTable.generate_random_string(18)
                    randchar = randchar+'.jpg'
                    full = os.path.join(os.path.abspath(r'.\data\avtCache'),randchar)
                    self.download_image(avturl,os.path.abspath(r'.\data\avtCache'),randchar)
                    sql_query = '''UPDATE profilesTableInstagram 
                        SET avt_path = ? WHERE uore = ?'''
                    cursor.execute(sql_query, (full, uore))
                    self.update_avt_signal.emit(indexTarget,full)
                    conn.commit()
                
                conn.close()

            def download_image(self,url, save_path, file_name):
                # Gửi yêu cầu GET đến URL để tải ảnh
                # headersTiktok = {
                #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
                # }
                response = requests.get(url,allow_redirects=True, stream=True)
                
                
                # Kiểm tra nếu yêu cầu thành công
                if response.status_code == 200:
                    # Tạo đường dẫn đầy đủ cho tệp tin
                    full_path = os.path.join(save_path, file_name)
                    
                    # Mở tệp tin để ghi dữ liệu
                    with open(full_path, 'wb') as file:
                        # Ghi dữ liệu từng khối vào tệp tin
                        for chunk in response.iter_content(1024):
                            file.write(chunk)
                    print(f"Image downloaded and saved to {full_path}")
                else:
                    print(f"Failed to download image. Status code: {response.status_code}")

        self.gettingThread = getUniqueIDThread()
        self.gettingThread.update_id_signal.connect(self.updateIDToTable)
        self.gettingThread.update_avt_signal.connect(self.updateAvtToTable)
        self.gettingThread.start()
        while not self.gettingThread.isFinished():
            QApplication.processEvents()
        print('Hoàn tất!')

    def updateAvtToTable(self,indexTarget,path):
        avt:QWidget = self.cellWidget(indexTarget,AVATAR_INDEX)
        label = avt.findChild(QLabel)
        pixmap = QPixmap(path)
        pixmap = self.createCircularPixmap(pixmap)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
   

    def createCircularPixmap(self, pixmap):
        size = min(pixmap.width(), pixmap.height())
        rounded = QPixmap(size, size)
        rounded.fill(Qt.GlobalColor.transparent)

        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(QBrush(pixmap))
        painter.setPen(QPen())
        
        # Cắt pixmap theo hình tròn
        path = QPainterPath()
        path.addEllipse(0, 0, size, size)
        painter.setClipPath(path)
        
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

        return rounded

    def updateIDToTable(self,indexTarget,uniqueId):
        self.setItem(indexTarget,IDTIKTOK_INDEX,QTableWidgetItemCenter(uniqueId))

    def pushAccountToBottom(self):
        rowsArr = self.unique_arr
        self.moveRows(rowsArr)

    
    def moveRows(self, row_indices):
        """Move specified rows to the end of the table."""

        rows_to_move = [self.getRowData(row) for row in row_indices]
        
        rows_to_move_db = []
        
        for index in self.unique_arr:
            uore = self.item(index,EMAIL_INDEX).text()
            self.mainWd.cursor.execute("SELECT * FROM profilesTableInstagram WHERE uore = ?", (uore,))
            record = self.mainWd.cursor.fetchone()
            rows_to_move_db.append(record)
            self.mainWd.cursor.execute(f"DELETE FROM profilesTableInstagram WHERE uore = ?", (uore,))
    
        self.mainWd.cursor.execute(f"PRAGMA table_info(profilesTable)")
        columns_info = self.mainWd.cursor.fetchall()
        column_names = [info[1] for info in columns_info][1:]
        for row in rows_to_move_db:
            row = row[1:]
            placeholders = ', '.join('?' * len(row))
            self.mainWd.cursor.execute(f"INSERT INTO profilesTable ({', '.join(column_names)}) VALUES ({placeholders})", row)
        
        self.mainWd.conn.commit()


        for row in sorted(row_indices, reverse=True):
            self.removeRow(row)

        # Inserting rows at the end
        end_index = self.rowCount()
        for i, row_data in enumerate(rows_to_move):
            self.insertRow(end_index + i)
            for column, item in enumerate(row_data):
                self.setItem(end_index + i, column, QTableWidgetItemCenter(item))
        
    def getRowData(self, row):
        """Get data from a specific row."""
        
        row_data = []
        for column in range(self.columnCount()):
            item = self.item(row, column)
            row_data.append(item.text() if item else "")
        return row_data

    def startCheckingVmld(self):
        path = os.path.abspath(r'.\vmld')
        if not os.path.exists(path):
            ret = pushYNQuestion('Chúng tôi phát hiện bạn chưa cài đặt giả lập!<br>Bạn có muốn tải xuống giả lập không?')
            if not ret:
                return False
            webbrowser.open('https://www.youtube.com/watch?v=Of2m3TT6dl4')
            return False
        return True

    
    
    def mouseDoubleClickEvent(self, event):
        item = self.itemAt(event.pos())
        if item:
            dialog = EditDialog(item.text(), self)
            dialog.exec()

    def contextMenuEvent(self, event):
        menu = QMenu()

        # khai báo sub menu copy
        submenuCopyOptions = QMenu("Copy thông tin", self)
        icon = QIcon(":/menu_context/papers.png")
        submenuCopyOptions.setIcon(icon)

        copyProfileName = submenuCopyOptions.addAction('Copy Tên hồ sơ')
        icon = QIcon(":/menu_context/profile-name-user.png")
        copyProfileName.setIcon(icon)

        copyUsername = submenuCopyOptions.addAction('Copy ID')
        icon = QIcon(":/menu_context/user.png")
        copyUsername.setIcon(icon)

        copyProxy = submenuCopyOptions.addAction('Copy Proxy')
        icon = QIcon(":/menu_context/proxy.png")
        copyProxy.setIcon(icon)

        copyEmail = submenuCopyOptions.addAction('Copy Email')
        icon = QIcon(":/menu_context/email.png")
        copyEmail.setIcon(icon)

        copyCookies = submenuCopyOptions.addAction('Copy Cookies')
        icon = QIcon(":/menu_context/cookies.png")
        copyCookies.setIcon(icon)

        copyStatistic = submenuCopyOptions.addAction('Copy thống kê(view|follow|like)')
        icon = QIcon(":/menu_context/analytics.png")
        copyStatistic.setIcon(icon)
        copyStatistic.setVisible(False)
        # khai báo sub menu copy

        # khai báo sub menu trình duyệt
        submenuBrowserOptions = QMenu("Tính năng trình duyệt", self)
        icon = QIcon(":/menu_context/chrome-black.png")
        submenuBrowserOptions.setIcon(icon)

        

        loginAction = submenuBrowserOptions.addAction('Đăng nhập tài khoản này')
        icon = QIcon(":/menu_context/login.png")
        loginAction.setIcon(icon)

        openBrowserForNt = submenuBrowserOptions.addAction('Mở trình duyệt tài khoản này')
        icon = QIcon(":/menu_context/earth.png")
        openBrowserForNt.setIcon(icon)


       
        reFingerprint= submenuBrowserOptions.addAction('Re-Fingerprint trình duyệt(Undetected)')
        icon = QIcon(":/menu_context/fingerprint.png")
        reFingerprint.setIcon(icon)

        addCookies = submenuBrowserOptions.addAction('Set cookies')
        icon = QIcon(":/menu_context/cookies.png")
        addCookies.setIcon(icon)
 


        # khai báo sub menu trình duyệt




        index = self.indexAt(event.pos())

        if not index.isValid():
            noAction = menu.addAction('Không có dòng nào được chọn')
            noAction.setText('Không có dòng nào được chọn')
            noAction.setEnabled(False)
            res = menu.exec(QCursor.pos())
            return
            
        if len(self.unique_arr) == 1:
            index = self.unique_arr[0]
            uore = self.item(index, EMAIL_INDEX).text()
            uploader_id = self.item(index, UPLOADER_ID).text()
          
            
            # Menu cho việc chọn 1 dòng
          

            editAction = menu.addAction('Sửa account này')
            icon = QIcon(":/menu_context/edit-profile.png")
            editAction.setIcon(icon)

     

            menu.addMenu(submenuBrowserOptions)
 
            
       
            moveToProject = menu.addAction('Chuyển sang dự án khác')
            icon = QIcon(":/menu_context/move-right.png")
            moveToProject.setIcon(icon)
                
            

            pushDownAccount = menu.addAction('Đưa vị trị các tài khoản này xuống dưới cùng')
            icon = QIcon(":/menu_context/push_down.png")
            pushDownAccount.setIcon(icon)
            pushDownAccount.setVisible(False)
       
            
            # nếu đăng nhập rồi thì tắt tuỳ chọn đăng nhập và tôi đã đăng nhập
            # if self.item(index, 2).text() == 'Đã đăng nhập':
            #     loginActionEmulator.setEnabled(False)
                # iHaveLoggedEmulator.setEnabled(False)

            # nếu có id tiktok rồi thì bật tuỳ chọn thống kê, và thay đổi username
  

            menu.addMenu(submenuCopyOptions)

            deleteAction = menu.addAction('Xóa account này')
            icon = QIcon(":/menu_context/bin.png")
            deleteAction.setIcon(icon)


            # khởi tạo và chờ đợi giá trị
            res = menu.exec(QCursor.pos())

          




            if res == editAction:
                self.mainWd.openEditProfileWindow(index,uore)
            
            elif res == moveToProject:
                self.moveToProject(uore)

            
            elif res == openBrowserForNt:
                self.openAndViewThisAccount(index,uore,uploader_id)
            
            elif res == loginAction:
                self.goLoginThisAccount(index,uore,uploader_id)

            elif res == deleteAction:
                ret = pushYNQuestion('Bạn có chắc chắn muốn xoá tài khoản này không?')
                if ret:
                    self.deleteThisAccount()

            elif res == reFingerprint:
                self.thewg = RefingerprintWidget()
                self.thewg.show()
                self.thewg.btn_cancel.clicked.connect(self.thewg.close)
                self.thewg.btn_ok.clicked.connect(lambda: self.bulkRefingerprint(
                    self.thewg.checkbox_win.isChecked(),
                    self.thewg.checkbox_mac.isChecked(),
                    self.thewg.checkbox_android.isChecked()
    
                    ))
                # self.reFingerprintThisAccount(uore)

            elif res == addCookies:
                self.loginByCookieWindow = QMainWindow()
                self.loginByCookieWindow.ui = ui_loginByCookiesWindow.Ui_MainWindow()
                self.loginByCookieWindow.ui.setupUi(self.loginByCookieWindow)
                self.loginByCookieWindow.ui.startStuff.clicked.connect(lambda: self.setCookieToUore(index,self.loginByCookieWindow.ui.cookiesPlainText.toPlainText(),uore,self.loginByCookieWindow))
                self.loginByCookieWindow.show()

                
                
            

            
            
            elif res == pushDownAccount:
                self.pushAccountToBottom()

       

            elif res == copyProfileName:
                try:
                    text = self.item(index, PROFILENAME_INDEX).text()
                except:
                    text = ''
                QApplication.clipboard().setText(text)

            elif res == copyUsername:
                try:
                    text = self.item(index, IDTIKTOK_INDEX).text()
                except:
                    text = ''
                QApplication.clipboard().setText(text)
            
            elif res == copyEmail:
                try:
                    text = self.item(index, EMAIL_INDEX).text()
                except:
                    text = ''
                QApplication.clipboard().setText(text)

            elif res == copyCookies:
                try:
                    cookie = self.item(index, COOKIE_INDEX).text()
                except:
                    cookie = ''
                QApplication.clipboard().setText(cookie)
            
            elif res == copyProxy:
                
                try:
                    text = self.item(index, PROXY_INDEX).text()
                except:
                    text = ''
                
                QApplication.clipboard().setText(text)
            elif res == copyStatistic:
                views = self.item(index, TOTALVIEWS_INDEX).text()
                follows = self.item(index, TOTALFOLLOWERS_INDEX).text()
                likes = self.item(index, TOTALLIKES_INDEX).text()
                text =  f'{views}|{follows}|{likes}'
                QApplication.clipboard().setText(text)

            

            # elif res == raiseProfileEmulator:
            #     if not os.path.isfile('./data/rasingAccountConfig.json'):
            #         ret = ret = pushYNQuestion(f'{self.mainWd.fullName} ơi! Chúng tôi phát hiện bạn chưa cài đặt nuôi tài khoản!<br>Bạn có muốn cài đặt ngay chứ?')
            #         if ret:
            #             self.mainWd.openSettingsQueueWindow()
            #             return
            #         else:
            #             return
            #     else:
            #         with open('./data/rasingAccountConfig.json', 'r+', encoding="utf-8") as f:
            #             json_data = json.load(f) 
            #             fastRaise = json_data['fastRaise']
            #             if not fastRaise:
            #                 pushNotification('Bạn chưa đồng ý cho nuôi nick trong cài đặt! Vui lòng mở cài đặt nuôi và kiểm tra lại!')
            #                 return
            #     self.raiseThisAccountByLD(index,uore)

        elif len(self.unique_arr) > 1:
            
            # khai báo sub menu trình duyệt
            submenuBrowserOptions = QMenu("Tính năng trình duyệt", self)
            icon = QIcon(":/menu_context/earth.png")
            submenuBrowserOptions.setIcon(icon)

            raiseProfileAdv = submenuBrowserOptions.addAction('Bảng chức năng trình duyệt')
            icon = QIcon(":/menu_context/job-enrichment.png")
            raiseProfileAdv.setIcon(icon)
            raiseProfileAdv.setVisible(False)
        

            
            reFingerprint= submenuBrowserOptions.addAction('Re-Fingerprint trình duyệt(Undetected)')
            icon = QIcon(":/menu_context/fingerprint.png")
            reFingerprint.setIcon(icon)

            addCookies= submenuBrowserOptions.addAction('Set cookies cho các tài khoản này')
            icon = QIcon(":/menu_context/cookies.png")
            addCookies.setIcon(icon)
            # khai báo sub menu trình duyệt

            # khai báo sub menu trình duyệt
            # submenuEmulatorOptions = QMenu("Tính năng giả lập", self)
            # icon = QIcon(":/menu_context/emulator.png")
            # submenuEmulatorOptions.setIcon(icon)

            # loginActionEmulator = submenuEmulatorOptions.addAction('Chạy đăng nhập cho các account đã chọn')
            # icon = QIcon(":/menu_context/login.png")
            # loginActionEmulator.setIcon(icon)

            # raiseProfileEmulator = submenuEmulatorOptions.addAction('Nuôi tài khoản (fast) cho các account đã chọn')
            # icon = QIcon(":/menu_context/social-media.png")
            # raiseProfileEmulator.setIcon(icon)
            # # khai báo sub menu trình duyệt
            menu.addMenu(submenuBrowserOptions)

          

            

            if not self.mainWd.isShownAllProfiles:
                moveToProject = menu.addAction('Chuyển các account đã chọn sang dự án khác')
                icon = QIcon(":/menu_context/move-right.png")
                moveToProject.setIcon(icon)
            else:
                moveToProject = None

            spreadProxyUa = menu.addAction('Phân bổ Proxy/UA cho account đã chọn')
            icon = QIcon(":/menu_context/multiple.png")
            spreadProxyUa.setIcon(icon)

            
            exportAccounts = menu.addAction('Xuất thông tin các account đã chọn')
            icon = QIcon(":/menu_context/download.png")
            exportAccounts.setIcon(icon)
            exportAccounts.setVisible(False)

            pushDownAccount = menu.addAction('Đưa vị trị các tài khoản này xuống dưới cùng')
            icon = QIcon(":/menu_context/push_down.png")
            pushDownAccount.setIcon(icon)
            
            menu.addMenu(submenuCopyOptions)
            
            # menu.addMenu(submenuEmulatorOptions)

           

            deleteAction = menu.addAction('Xóa các account đã chọn')
            icon = QIcon(":/menu_context/bin.png")
            deleteAction.setIcon(icon)

            res = menu.exec(QCursor.pos())
    
            
            

            if res == moveToProject:
                arr = []
                for indexTarget in self.unique_arr:
                    arr.append(self.item(indexTarget,EMAIL_INDEX).text())
                self.moveToProject(None,arr)

            

            

            elif res == spreadProxyUa:
                self.openSettingProxyUABeforeChange()
            
    
            
            elif res == exportAccounts:
                self.openExportOptions()

            elif res == pushDownAccount:
                self.pushAccountToBottom()

            

            
                
            elif res == raiseProfileAdv:
                self.openRaiseAdvWindow(self.unique_arr)  

            

            elif res == reFingerprint:
                self.thewg = RefingerprintWidget()
                self.thewg.show()
                self.thewg.btn_cancel.clicked.connect(self.thewg.close)
                self.thewg.btn_ok.clicked.connect(lambda: self.bulkRefingerprint(
                    self.thewg.checkbox_win.isChecked(),
                    self.thewg.checkbox_mac.isChecked(),
                    self.thewg.checkbox_android.isChecked()
                    
                    ))
            
            elif res == addCookies:
                def changedText(ui):
                    text = ui.cookiesPlainText.toPlainText()
                    text = text.split('\n')
                    final1 = []
                    for cookie in text:
                        if cookie and cookie != '':
                            final1.append(cookie)
                    ui.countCookie.setText(str(len(final1)))

                self.loginByCookieWindow = QMainWindow()
                self.loginByCookieWindow.ui = ui_loginMultipleByCookiesWindow.Ui_MainWindow()
                self.loginByCookieWindow.ui.setupUi(self.loginByCookieWindow)
                self.loginByCookieWindow.ui.cookiesPlainText.textChanged.connect(lambda:changedText(self.loginByCookieWindow.ui))
                self.loginByCookieWindow.ui.total.setText(str(len(self.unique_arr)))
                
                
                text = ''
                
                def loginThis():
                    ui = self.loginByCookieWindow.ui
                    cookies = ui.cookiesPlainText.toPlainText()
                    cookies = cookies.split('\n')
                    final = []
                    
                    for cookie in cookies:
                        if cookie and cookie != '':
                            final.append(cookie)
              

                    for ii,indexTarget in enumerate(self.unique_arr):
                        try:
                            cookie = final[ii]
                        except:
                            continue
                        uore = self.item(indexTarget, EMAIL_INDEX).text()
                        
                        self.setCookieToUore(indexTarget,cookie,uore)
                    
                    self.loginByCookieWindow.close()
                  

                    
                for indexTarget in self.unique_arr:
                    profileName = self.item(indexTarget, PROFILENAME_INDEX).text()
                    uore = self.item(indexTarget, EMAIL_INDEX).text()
                  
                    item = profileName
                    text = text+item+','
                text = text[:-1]
                self.loginByCookieWindow.ui.whichIndex.setText(text)
                self.loginByCookieWindow.ui.startStuff.clicked.connect(lambda: loginThis())
                self.loginByCookieWindow.show()
                
                


           
            
            elif res == copyProfileName:
                alltext = ''
                for row in (self.unique_arr):
                    try:
                        text = self.item(row,PROFILENAME_INDEX).text()
                    except:
                        text = ''
                    alltext = alltext + text + '\n'
                QApplication.clipboard().setText(alltext)

            elif res == copyUsername:
                alltext = ''
                for row in (self.unique_arr):
                    try:
                        text = self.item(row,IDTIKTOK_INDEX).text()
                    except:
                        text = ''
                    alltext = alltext + text + '\n'
                QApplication.clipboard().setText(alltext)
            
            elif res == copyEmail:
                alltext = ''
                for row in (self.unique_arr):
                    try:
                        text = self.item(row,EMAIL_INDEX).text()
                    except:
                        text = ''
                    alltext = alltext + text + '\n'
                QApplication.clipboard().setText(alltext)

            elif res == copyCookies:
                alltext = ''
                for row in (self.unique_arr):
                    try:
                        uore = self.item(row,EMAIL_INDEX).text()
                        self.mainWd.cursor.execute("SELECT * FROM profilesTableInstagram WHERE uore = ?", (uore,))
                        record = self.mainWd.cursor.fetchone()
                        text = record[20]
                    except:
                        text = ''
                    alltext = alltext + text + '\n'
                
                QApplication.clipboard().setText(alltext)

            elif res == copyProxy:
                alltext = ''
                for row in (self.unique_arr):
                    try:
                        text = self.item(row,PROXY_INDEX).text()
                    except:
                        text = ''
                    alltext = alltext + text + '\n'
                QApplication.clipboard().setText(alltext)

            elif res == copyStatistic:
                alltext = ''
                for row in self.unique_arr:
                    try:
                        views = self.item(row, TOTALVIEWS_INDEX).text()
                        if views == '':
                            views = 0
                    except:
                        views = 0
                    try:
                        follows = self.item(row, TOTALFOLLOWERS_INDEX).text()
                        if follows == '':
                            follows = 0
                    except:
                        follows = 0
                    try:
                        likes = self.item(row, TOTALLIKES_INDEX).text()
                        if likes == '':
                            likes = 0
                    except:
                        likes = 0
                    
                    text =  f'{views}|{follows}|{likes}'
                    alltext = alltext + text + '\n'
                QApplication.clipboard().setText(alltext)

            elif res == deleteAction:
                ret = pushYNQuestion('Bạn có chắc chắn muốn xoá các tài khoản này không?')
                if ret:
                    self.deleteThisAccount()
                
            # elif res == loginActionEmulator:
            #     if self.logginScreen is not None and self.logginScreen.isRunning():
            #         self.logginScreen.terminate()
            #         return
            #     self.screenWindow = ScreenBrowsers(self)
            #     self.screenWindow.show()
            #     QCoreApplication.processEvents()
            #     thisTable = self

            #     class startThread(QThread):
            #         err_signal = pyqtSignal(str)
            #         def __init__(self) -> None:
            #             super().__init__()

            #         def run(self):
            #             for indexTarget in thisTable.unique_arr:
            #                 profileName = thisTable.item(indexTarget, 0).text()
            #                 uore = thisTable.item(indexTarget, 11).text()
            #                 login_thread = LoginThisAccountInScreensByLD(indexTarget,uore,profileName)
            #                 login_thread.stateAccount.connect(thisTable.changeStateAccountFuncLD)
            #                 login_thread.pushIntoScreen.connect(thisTable.screenWindow.addNewLDToGridScreen)
            #                 login_thread.update_slashState_signal.connect(thisTable.screenWindow.updateSlashStateWorker)
            #                 login_thread.pushErrors.connect(self.pushNoti)
            #                 thisTable.loginThreadsBrowser[indexTarget] = login_thread
            #                 login_thread.start()
            #                 time.sleep(3)
                        
            #         def pushNoti(self,text):
            #             self.err_signal.emit(text)
                

            #     self.logginScreen = startThread()
            #     self.logginScreen.err_signal.connect(pushNotification)
            #     self.logginScreen.start()

            # elif res == raiseProfileEmulator:

            #     if self.raiseThread is not None and self.raiseThread.isRunning():
            #         pushNotification('Bạn cần kiên nhẫn cho đến khi lượt nuôi này hoàn tất hoặc bạn có thể tắt cửa sổ này và làm lại!')
            #         return
            #     with open('./data/rasingAccountConfig.json', 'r+', encoding="utf-8") as f:
            #         json_data = json.load(f) 
            #         fastRaise = json_data['fastRaise']
            #         if not fastRaise:
            #             pushNotification('Bạn cần phải cho phép nuôi trong cài đặt thì mới nuôi được! Vui lòng kiểm tra lại!')
            #             return

            #     self.screenWindow = ScreenBrowsers(self)
            #     self.screenWindow.show()
            #     QCoreApplication.processEvents()
            #     thisTable = self
            #     for indexTarget in thisTable.unique_arr:
            #         profileName = thisTable.item(indexTarget, 0).text()
            #         uore = thisTable.item(indexTarget, 11).text()
            #         raise_thread = RaiseThisAccountInScreensByLD(indexTarget,uore,profileName)
            #         raise_thread.pushIntoScreen.connect(thisTable.screenWindow.addNewLDToGridScreen)
            #         raise_thread.update_slashState_signal.connect(thisTable.screenWindow.updateSlashStateWorker)
            #         self.raiseThreadsBrowser[indexTarget] = raise_thread
            #     class startThread(QThread):
            #         def run(self):
            #             for indexTarget in thisTable.unique_arr:
            #                 # profileName = thisTable.item(indexTarget, 0).text()
            #                 # uore = thisTable.item(indexTarget, 11).text()
            #                 # raise_thread = RaiseThisAccountInScreensByLD(indexTarget,uore,profileName)
            #                 # raise_thread.pushIntoScreen.connect(thisTable.screenWindow.addNewLDToGridScreen)
            #                 # raise_thread.update_slashState_signal.connect(thisTable.screenWindow.updateSlashStateWorker)
            #                 # # raise_thread.pushErrors.connect(self.pushNoti)
            #                 raise_thread:RaiseThisAccountInScreensByLD = thisTable.raiseThreadsBrowser[indexTarget]
            #                 raise_thread.start()
            #                 time.sleep(2)
                    
            #         def stopAll(self):
            #             for indexTarget in thisTable.unique_arr:
            #                 # profileName = thisTable.item(indexTarget, 0).text()
            #                 # uore = thisTable.item(indexTarget, 11).text()
            #                 # raise_thread = RaiseThisAccountInScreensByLD(indexTarget,uore,profileName)
            #                 # raise_thread.pushIntoScreen.connect(thisTable.screenWindow.addNewLDToGridScreen)
            #                 # raise_thread.update_slashState_signal.connect(thisTable.screenWindow.updateSlashStateWorker)
            #                 # # raise_thread.pushErrors.connect(self.pushNoti)
            #                 raise_thread:RaiseThisAccountInScreensByLD = thisTable.raiseThreadsBrowser[indexTarget]
            #                 raise_thread._forceStop = True
            #                 # time.sleep(2)

            #         def pushNoti(self,text):
            #             # self.err_signal.emit(text)
            #             pass

            #     self.raiseThread = startThread()
            #     self.raiseThread.start()
    
    def setCookieToUore(self,index,cookie,uore,loginByCookieWindow=None):
        cookie = cookie.replace('\n','')
        item = self.item(index,COOKIE_INDEX)
        if self.mainWd.mode == 'Instagram':
            sql_query = '''UPDATE profilesTableInstagram 
                SET cookies_browser = ?  WHERE uore = ?'''
            item.cookie = cookie
        if self.mainWd.mode == 'Threads':
            sql_query = '''UPDATE profilesTableInstagram 
                SET cookies_threads_browser = ?  WHERE uore = ?'''
            item.cookies_threads_browser = cookie

        self.mainWd.cursor.execute(sql_query, (cookie, uore))
        self.mainWd.conn.commit()
        item.setText(cookie)
       
        # self.setItem(index,COOKIE_INDEX,item)
        if loginByCookieWindow:
            loginByCookieWindow.close()
    
    def checkAvailableRemainStorage(self):
        # Lấy thông tin về ổ đĩa
        total, used, free = shutil.disk_usage("/")

        # Chuyển đổi dung lượng từ byte sang gigabyte
        free_gb = free / (2**30)

        # Kiểm tra nếu dung lượng còn lại dưới 6GB
        if free_gb < 6:
            return False
        else:
            return True

    def createEmulator(self,typeCreate,uore,long,la,dialog=None):
    
        availableStorage = self.checkAvailableRemainStorage()
        if not availableStorage:
            pushNotification('Ổ cứng của bạn không còn đủ chỗ để tạo thêm mới giả lập! Vui lòng dọn dẹp...')
            return
        loading_modal_widget = LoadingWidget()
        self.createLd = createEmulatorThread(typeCreate,uore,long,la)
        self.createLd.err.connect(pushNotification)
        self.createLd.updateUi.connect(loading_modal_widget.loading_modal_ui.label.setText)
        self.createLd.start()

        # tạo hoạt ảnh chạy
        loading_modal_widget.move(self.mainWd.window.x()+100,self.mainWd.window.y()+100)
        loading_modal_widget.show()
       
        while not self.createLd.isFinished():
            QApplication.processEvents()

        loading_modal_widget.close()
        loading_modal_widget.deleteLater()
        
        

    def bulkRefingerprint(self,win = False, mac = False, android = False):
        platform = []
        if win:
            platform.append('win')
        if mac:
            platform.append('mac')
        if android:
            platform.append('android')
        
        if len(platform) == 0:
            pushNotification('Bạn phải chọn ít nhất 1 nền tảng')
            return
        
        loading_modal_widget = QWidget()
        loading_modal_widget.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        loading_modal_widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        loading_modal_ui = ui_createBrowserFilesModal.Ui_Form()
        loading_modal_ui.setupUi(loading_modal_widget)
        loading_modal_ui.label.setText('Đang đổi, vui lòng đợi!')
        movie = QMovie(":/animated-gif/soon.gif")
        loading_modal_ui.runningCar.setScaledContents(True)
        loading_modal_ui.runningCar.setMovie(movie)
        movie.start()
        loading_modal_widget.show()
        QApplication.processEvents()
        self.stateDone = ''
        thisWidget = self
        self.records = {}
        for indexTarget in thisWidget.unique_arr:
            uore = thisWidget.item(indexTarget, EMAIL_INDEX).text()
            thisWidget.mainWd.cursor.execute("SELECT * FROM profilesTableInstagram WHERE uore = ?", (uore,))
            record = thisWidget.mainWd.cursor.fetchone()
            self.records[indexTarget] = record

        class theThread(QThread):
            def run(self):
                for indexTarget in thisWidget.unique_arr:
                    profileName = thisWidget.item(indexTarget, PROFILENAME_INDEX).text()
                    record = thisWidget.records[indexTarget]
                    thisWidget.stateDone = thisWidget.stateDone + thisWidget.reFingerprintThisAccount(record,True,profileName,platform)
        
        thr = theThread()
        thr.start()
        while not thr.isFinished():
            QApplication.processEvents()

        movie.stop()
        loading_modal_widget.close()
        loading_modal_widget.deleteLater()
        pushNotificationPlain(self.stateDone)

    


    def reFingerprintThisAccount(self,record,multiple= False,profileName=None, platform = None):
 
   
        theid = record[columns_db_index['id_gologin']]

        if theid != None and theid != '':
            RunProfile = GoLogin({
                "profile_id": str(theid), # ID profile
                "folderBrowser": os.path.join(os.getcwd(),'data\.gologin'), # Đường dẫn folder lưu browser và fonts
                "tmpdir": os.path.join(os.getcwd(),'data\Go Profiles') # Đường dẫn lưu
            })
            # try:
            #     proxy_type = record[19]
            #     proxys = proxy.split(':')
            #     host = proxys[0]
            #     port = proxys[1]
            #     usernameprx = proxys[2]
            #     passwordprx = proxys[3]
            # except:
            #     proxy_type = 'none'
            #     host = ''
            #     port = ''
            #     usernameprx = ''
            #     passwordprx = ''
            try:
                RunProfile.reFingerPrint({
                    "version": '118.0.5993.70',
                    "os": random.choice(platform),
                    "name": f"SSMATool-{self.generate_random_string(6)}",
                    "canvas": {
                        "mode": 'noise'
                    },
                    "canvasMode": 'noise',
                    "webRTC": {
                        "mode": 'noise',
                    },
                    "webRtc": {
                        "mode": 'noise',
                    },
                    "webGL": {
                        "mode": 'noise',
                    },
                    "audioContext": {
                        "mode": True,
                    },
                    "clientRects": {
                        "mode": True,
                    },

                    "geoLocation": {
                        "mode": 'noise',
                    }, 
                    "geolocation": {
                        "mode": 'noise',
                    },
                    "googleServicesEnabled": True,
                    "doNotTrack": True
                })
                if multiple:
                    return  f'<html><head/><body><p>Re-Fingerprint thành công Tài khoản: <b style=" color:#2ed573;">{profileName}</b></p></body></html>\n'
                  

                pushNotification('Thành công')
                return
            except Exception as e:
                if multiple:
                    return f'<html><head/><body><p>Không thể Re-Fingerprint hồ sơ: <b style=" color:#ff4757;">{profileName}</b><span style=" color:#000000;"> vì: {str(e)}</span></p></body></html>\n'
                 
                pushNotification(f'Lỗi khi RefingerPrint vì:<br>{traceback.format_exc()}')
                return
            # API_ENDPOINT = 'http://127.0.0.1:53200/api/v2/'
            # ACTION_UPDATE = API_ENDPOINT + 'profile-random-fingerprint-configuration'
            # rs = updateBrowserFingerprint(ACTION_UPDATE,theid)
            # if rs != True:
                
            # else:
                
        else:
            if multiple:
                return f'<html><head/><body><p>Hồ sơ: <b style=" color:#ff4757;">{profileName}</b><span style=" color:#000000;"> chưa tạo trình duyệt Undetected</span></p></body></html>\n'
            pushNotification('Bạn chưa tạo trình duyệt Undetected!<br>Vui lòng Mở trình duyệt để auto tạo trình duyệt!')

    def openRaiseAdvWindow(self,listIndex):
        theIdProject = self.mainWd.projectCombobox.itemData(self.mainWd.projectCombobox.currentIndex())
   
        try:
            
            raiseScreen:RaiseScreenWindow = self.raiseProjects[theIdProject]
            raiseScreen.activateWindow()
            return
            # if isinstance(driver, str):
            # self.error = True
            # self.errorString = driver
            # self.update_ERRORS_signal.emit(self.errorString)
        except KeyError:
            # print('KeyError ở đây')
            pass
        except:
            print(f"==>> openRaiseAdvWindow error: {traceback.format_exc()}")
            
        
        raiseScreen = RaiseScreenWindow(self,listIndex,theIdProject)
        self.raiseProjects[theIdProject] = raiseScreen
        raiseScreen.showLeftTab()
        
        raiseScreen.show()
        QApplication.processEvents()
        # raiseScreen.manager = Manager()
        # raiseScreen.queue = raiseScreen.manager.Queue()
        # print('Khởi động Queue thành công')
        
    def moveAllToTotal(self,listUore):
        
        try:
            lock.acquire(True)
            for theUore in listUore:
                sql_query = '''
                UPDATE profilesTableInstagram
                SET project_container = ?
                WHERE uore = ?
                '''
                self.mainWd.cursor.execute(sql_query, (0, theUore))
                self.mainWd.conn.commit()
        finally:
            lock.release()
      
        self.mainWd.loadProfilesToTable()
             
    def moveToProject(self,uore,listUore = None,toTotal = False):
        def moveNow(dialog):
            userData = dialog.combo_box.itemData(dialog.combo_box.currentIndex())
            if not listUore:
                sql_query = '''
                UPDATE profilesTableInstagram
                SET project_container = ?
                WHERE uore = ?
                '''
                self.mainWd.cursor.execute(sql_query, (userData, uore))
                self.mainWd.conn.commit()
            else:
                for theUore in listUore:
                    sql_query = '''
                    UPDATE profilesTableInstagram
                    SET project_container = ?
                    WHERE uore = ?
                    '''
                    self.mainWd.cursor.execute(sql_query, (userData, theUore))

                self.mainWd.conn.commit()

            for indexTarget in reversed(sorted(self.unique_arr)):
                self.removeRow(indexTarget)
           
                

            dialog.close()
      

        dialog = ChooseProjectDialog(self.mainWd)
        dialog.okeBtn.clicked.connect(lambda: moveNow(dialog))
        dialog.cancelBtn.clicked.connect(lambda: dialog.close())
        dialog.exec()

    def setMusicBypass(self,index,rows = None):
        thisTable = self
        
        class MusicBypassWidget(QWidget):
            def __init__(self):
                super(MusicBypassWidget, self).__init__()

                self.init_ui()

            def init_ui(self):
                # Tạo và cấu hình QPlainTextEdit
                plain_text_edit = QPlainTextEdit(self)
                plain_text_edit.setPlaceholderText("Nhập tên bài hát ở đây.. Mỗi tên bài hát là 1 dòng")

                # Tạo và cấu hình QPushButton
                button = QPushButton('Thêm vào cơ sở dữ liệu', self)
                button.clicked.connect(lambda: self.display_text())

                # Sắp xếp các thành phần trong QWidget sử dụng QVBoxLayout
                layout = QVBoxLayout(self)
                layout.addWidget(plain_text_edit)
                layout.addWidget(button)

                # Thiết lập kích thước cửa sổ và tiêu đề
                # self.setGeometry(100, 100, 600, 400)
                self.setWindowIcon(QIcon(':/logo/icon-sw.png'))
                self.setWindowTitle('Danh sách nhạc')

            def display_text(self):
                # Lấy văn bản từ QPlainTextEdit và hiển thị nó (đơn giản là in ra console)
                text = self.layout().itemAt(0).widget().toPlainText()
                
                conn = sqlite3.connect('./data/profilesDATA.db')
                cursor = conn.cursor()
                if rows:
                    for indx in rows:
                        uore = thisTable.item(indx, EMAIL_INDEX).text()
                        sql_query = '''UPDATE profilesTableInstagram 
                        SET music_bypass = ? WHERE uore = ?'''
                        cursor.execute(sql_query, (text, uore))
                else:
                    uore = thisTable.item(index, EMAIL_INDEX).text()
                    sql_query = '''UPDATE profilesTableInstagram 
                        SET music_bypass = ? WHERE uore = ?'''
                    cursor.execute(sql_query, (text, uore))
                conn.commit()
                conn.close()

                pushNotification('Thêm thành công')
                self.close()
                return
                
        
        self.musicbypass = MusicBypassWidget()
        self.musicbypass.show()

    

    def getLocFolder(self):
        rs = QFileDialog.getExistingDirectory(QMainWindow(), caption='Select Location:')
        return rs

    def setVideoFolder(self,index,uore,folder_path = None):
        if not folder_path:
            folder_path = self.getLocFolder()
            if folder_path == '':
                return
        self.setItem(index,FOLDERUPLOAD_INDEX,QTableWidgetItemCenter(folder_path))
        conn = sqlite3.connect('./data/profilesDATA.db')
        cursor = conn.cursor()
        sql_query = '''UPDATE profilesTableInstagram 
            SET folder_upload = ? WHERE uore = ?'''
        cursor.execute(sql_query, (folder_path, uore))
        conn.commit()
        conn.close()

    def loadVideoFromFolderToTable(self,profileName,folder_path):

        
        def convert_to_hms(seconds):
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        
        

        for file in os_sorted(os.listdir(folder_path)):
            full = os.path.join(folder_path,file)            
            absolute_file_path = str(Path.cwd() / full)
            if '-RENDERED' in absolute_file_path:
                continue
            command = ['ffprobe','-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', absolute_file_path]
            startupinfo = None
            if os.name == 'nt':
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            try:
                output = subprocess.check_output(command,startupinfo=startupinfo)
            except Exception as e:
                pushNotification(f'Có vẻ như bạn chưa cài depencies hoặc bạn đã làm sai cách, vui lòng xem lại video hướng dẫn load từ thư mục! Lý do:<br>{str(e)}')
                return
            file_split = file.split('.')
            title = file_split[0]
            numRow = self.mainWd.videoTable.rowCount()
            dropdownPrivacy = QComboBox()
            dropdownPrivacy.addItems(['Public','Schedule'])
            dropdownPrivacy.currentIndexChanged.connect(
                            lambda selected_index, row=numRow: self.mainWd.changePrivacyOfThisRow(row, selected_index))
            rspc = QProgressBar()
            rspc.setValue(100)

            self.mainWd.videoTable.insertRow(numRow)
            
            self.mainWd.videoTable.setItem(    
                                numRow, 0, QTableWidgetItem(title))
            
            item = QTableWidgetItem("None")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.mainWd.videoTable.setItem(    
                                numRow, 1, QTableWidgetItem(item))
            self.mainWd.videoTable.setItem(    

                                numRow, 2, QTableWidgetItem(item))
            
            item = QTableWidgetItem(format(convert_to_hms(int(float(output)))))
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.mainWd.videoTable.setItem(    
                                numRow, 3, QTableWidgetItem(item))
            
            self.mainWd.videoTable.setCellWidget(    
                                numRow, 4, dropdownPrivacy)
            
            self.mainWd.videoTable.setCellWidget(    
                                numRow, 8, rspc)
            self.mainWd.videoTable.setItem(    
                                numRow, 14, QTableWidgetItem(absolute_file_path))
            
            result = '[' + profileName + ']'
            self.mainWd.videoTable.setItem(numRow,6,QTableWidgetItem(result))

    def openSettingProxyUABeforeChange(self):

        self.changeProxyUAWindow = BulkChangeProxyUAWindow(self)
        self.changeProxyUAWindow.show()
    
    def openExportOptions(self):
        self.exportAccountWd = ExportAccountsWindow(self)
        self.exportAccountWd.show()

    def openSettingBeforeChange(self):
        theIdProject = self.mainWd.projectCombobox.itemData(self.mainWd.projectCombobox.currentIndex())

        self.changeInfoWindow = BulkChangeInfoWindow(self,theIdProject)
        self.changeInfoWindow.show()

        
    def deleteThisAccount(self):
        # Kết nối đến database
       
        def deleteFromRow(theRow):
            username_to_delete = self.item(theRow, EMAIL_INDEX).text()
            self.mainWd.cursor.execute("SELECT * FROM profilesTableInstagram WHERE uore = ?", (username_to_delete,))
            record = self.mainWd.cursor.fetchone()
            id_browser = record[columns_db_index['id_browser']]
          
            id_gologin = record[columns_db_index['id_gologin']]
            

            sql_query = "SELECT * FROM browsersTable WHERE id = ?"
            self.mainWd.cursor.execute(sql_query, (id_browser,))
            result = self.mainWd.cursor.fetchone()
            path_browser = result[1]
            try:
                shutil.rmtree(os.path.abspath(path_browser))
            except:
                pass

            try:
                goprofile = os.path.join(os.getcwd(),f'data/Go Profiles/{id_gologin}')
                print(f"==>> goprofile: {goprofile}")
                shutil.rmtree(goprofile)
                print('xóa thư mục profile go thành công')
            except:
                pass

            self.mainWd.cursor.execute(f"DELETE FROM profilesTableInstagram WHERE uore=?", (username_to_delete,))
            self.mainWd.cursor.execute(f"DELETE FROM browsersTable WHERE id= ?", (id_browser,))
            self.removeRow(theRow)
            self.mainWd.conn.commit()
            

        try:
            lock.acquire(True)
            for row in reversed(sorted(self.unique_arr)):
                deleteFromRow(row)
        finally:
            lock.release()
    
    def openAndViewThisAccount(self,index,uore,uploader_id):
        
        try:
            accountHelper:AccountHelper = self.accountHelpers[uore]
        
            threading.Thread(target=accountHelper.startBrowser,args=(1,)).start()
           
        except:
            accountHelper = self.accountHelperGenerate(index,uore,uploader_id)
        
            threading.Thread(target=accountHelper.startBrowser,args=(1,)).start()
            
        

        # self.worker = PlaywrightWorker()
        # self.worker.finished.connect(lambda: print("Playwright task completed"))
        # self.worker.start()
        # return
        
    def raiseThisAccountByLD(self,index,uore):
        
        try:
         
            raise_thread:RaiseThisAccountByLD = self.rasingThreads[index]
            if raise_thread.isRunning():
                raise_thread.ldCtrler.Close()
                raise_thread.forceStop = True
                raise_thread.terminate()
                # pushNotification('Bạn đang nuôi tài khoản này rồi!')
                return
        except:
            raise_thread = RaiseThisAccountByLD(index,uore)
            raise_thread.pushErrors.connect(pushNotification)
            self.rasingThreads[index] = raise_thread
            raise_thread.start()    

    def raiseThisAccount(self,index,uore):
        
        try:
            raise_thread:RaiseThisAccount = self.rasingThreads[index]
            if raise_thread.isRunning():
                raise_thread.browser.quit()
                raise_thread.forceStop = True
                raise_thread.terminate()
            del self.rasingThreads[index]
            # raise_thread.terminate()
            return
        except:
            raise_thread = RaiseThisAccount(index,uore)
            raise_thread.pushErrors.connect(pushNotification)
            self.rasingThreads[index] = raise_thread
            raise_thread.start()

    def goLoginThisAccountByLD(self,index,uore):
        
        try:
            login_thread:LoginThisAccountByLD = self.loginThreadsLD[index]
            
            if login_thread.isRunning():
                login_thread.forceClose = True
                login_thread.ldCtler.Close()
                time.sleep(1)
                login_thread.terminate()
                pushNotification('Đã dừng đăng nhập!')
                # login_thread.wait()
                # login_thread.deleteLater()
                return
            else:
                login_thread = LoginThisAccountByLD(index,uore)
                login_thread.stateAccount.connect(self.changeStateAccountFuncLD)
                login_thread.pushErrors.connect(pushNotification)
                self.loginThreadsLD[index] = login_thread
                login_thread.start()
        except:
            
            login_thread = LoginThisAccountByLD(index,uore)
            login_thread.stateAccount.connect(self.changeStateAccountFuncLD)
            login_thread.pushErrors.connect(pushNotification)
            self.loginThreadsLD[index] = login_thread
            login_thread.start()

    def accountHelperGenerate(self,index,uore,uploader_id):
        theIdProject = self.mainWd.projectCombobox.itemData(self.mainWd.projectCombobox.currentIndex())
        self.mainWd.cursor.execute("SELECT * FROM profilesTableInstagram WHERE uore = ?", (uore,))
        record = self.mainWd.cursor.fetchone()
        accountHelper = AccountHelper(theIdProject,record,uploader_id)
        accountHelper.mode = self.mainWd.mode
        accountHelper.stateAccount.connect(self.changeStateAccountFunc)
        accountHelper.setForegroundWindow.connect(ctypes.windll.user32.SetForegroundWindow)
        accountHelper.pushErrors.connect(pushNotification)

        self.accountHelpers[uore] = accountHelper
        
        iditem = self.cellWidget(index,IDTIKTOK_INDEX)

        statusitem = self.cellWidget(index,STATUSBROWSER_INDEX)
        statusitem1 = self.cellWidget(index,STATUSBROWSERTHREADS_INDEX)

        cookieitem = self.item(index,COOKIE_INDEX)

        self.accountHelpersItemTable[uore] = (iditem.ui.avatar,iditem,statusitem.label,statusitem1.label,cookieitem)

        return accountHelper

    def goLoginThisAccount(self,index,uore,uploader_id):
        
      
        try:
            
            accountHelper:AccountHelper = self.accountHelpers[uore]
            accountHelper.mode = self.mainWd.mode
            accountHelper.startLogin()
  
        except:
          
            accountHelper = self.accountHelperGenerate(index,uore,uploader_id)
            accountHelper.startLogin()

    def changeStateAccountFuncLD(self,index,text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setItem(index, IDTIKTOK_INDEX, item)
        item = QTableWidgetItem("Đã đăng nhập")
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setItem(index, STATUSBROWSERTHREADS_INDEX, item)    
    
    def changeStateAccountFunc(self,uore,text,cookie,fullavt,theIdProject):
        
      
        now = self.mainWd.projectCombobox.itemData(self.mainWd.projectCombobox.currentIndex())

        if self.mainWd.mode == 'Instagram':
            sql_query = '''UPDATE profilesTableInstagram 
                SET username_on_instagram = ?, state_loggin_browser = ? ,cookies_browser = ? ,avt_path = ?  WHERE uore = ?'''
        if self.mainWd.mode == 'Threads':
            sql_query = '''UPDATE profilesTableInstagram 
                SET username_on_threads = ?, state_loggin_browser_threads = ? ,cookies_threads_browser = ? ,avt_thread_path = ?  WHERE uore = ?'''
        
        try:
            lock.acquire(True)
            self.mainWd.cursor.execute(sql_query, (text, True, cookie, fullavt , uore))
            self.mainWd.conn.commit()
        finally:
            lock.release()
        
       

        if int(now) == int(theIdProject):

            mainitem = self.accountHelpersItemTable[uore]
            
            label:QLabel = mainitem[0]
            iditem:QLabel = mainitem[1]
            statusitem:QLabel = mainitem[2]
            statusitem1:QLabel = mainitem[3]
            cookieitem:QTableWidgetItemCenter = mainitem[4]

            if fullavt and os.path.isfile(fullavt):
                pixmap = QPixmap(fullavt)
                print('co tao r')
            else:
                pixmap = QPixmap(':/photos/user-avatar.jpg')
                print('k co tao r')

            pixmap = self.createCircularPixmap(pixmap)
            label.setPixmap(pixmap)
            pixmap = QPixmap(':/colored-icon/record.png')


            if self.mainWd.mode == 'Instagram':
                iditem.ui.image_path = fullavt
                iditem.ui.mainAccount.setText(text)
                statusitem.status = 1
                statusitem.setPixmap(pixmap)

            if self.mainWd.mode == 'Threads':
                iditem.ui.avt_threads_path = fullavt
                iditem.ui.subAccount.setText(text)
                statusitem1.status = 1
                statusitem1.setPixmap(pixmap)

            cookieitem.setText(cookie)
