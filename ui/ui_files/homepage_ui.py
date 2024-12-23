# Form implementation generated from reading ui file 'd:\InstaThread\ui\ui_files\homepage.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 823)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Iconshortcut/IconShortcut.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainLayout = QtWidgets.QWidget(parent=self.centralwidget)
        self.mainLayout.setStyleSheet("QWidget#mainLayout {\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"background: #f0eeef;\n"
"}")
        self.mainLayout.setObjectName("mainLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainLayout)
        self.verticalLayout.setContentsMargins(1, 0, 1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QtWidgets.QWidget(parent=self.mainLayout)
        self.top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top.setObjectName("top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.top)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(155, 42))
        self.label.setMaximumSize(QtCore.QSize(155, 36))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label.setPixmap(QtGui.QPixmap(":/logoHomepage/instaThreads.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.toggleSidebarBtn = QtWidgets.QPushButton(parent=self.top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleSidebarBtn.sizePolicy().hasHeightForWidth())
        self.toggleSidebarBtn.setSizePolicy(sizePolicy)
        self.toggleSidebarBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.toggleSidebarBtn.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.toggleSidebarBtn.setStyleSheet("QPushButton{\n"
"text-align:left;\n"
"padding:6px;\n"
"border-radius:0;\n"
"color:black;\n"
"background:transparent\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"      border: 0px solid #747d8c;  \n"
"    color: black; /* Màu chữ khi hover */  \n"
"    background-color: #d5d4d4; /* Màu nền khi hover */  \n"
"    border-radius : 4px\n"
"   \n"
"}\n"
"")
        self.toggleSidebarBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconSidebar/switchBtn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toggleSidebarBtn.setIcon(icon1)
        self.toggleSidebarBtn.setIconSize(QtCore.QSize(30, 30))
        self.toggleSidebarBtn.setObjectName("toggleSidebarBtn")
        self.horizontalLayout.addWidget(self.toggleSidebarBtn)
        self.projectOptions = QtWidgets.QWidget(parent=self.top)
        self.projectOptions.setStyleSheet("QPushButton {\n"
"background : transparent;\n"
"border : 0;\n"
"padding : 0;\n"
"color: black\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"      border: 0px solid #747d8c;  \n"
"    color: black; /* Màu chữ khi hover */  \n"
"    background-color: #d5d4d4; /* Màu nền khi hover */  \n"
"    border-radius : 4px\n"
"   \n"
"}")
        self.projectOptions.setObjectName("projectOptions")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.projectOptions)
        self.horizontalLayout_3.setContentsMargins(16, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(51, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.projectCombobox = QtWidgets.QComboBox(parent=self.projectOptions)
        self.projectCombobox.setIconSize(QtCore.QSize(20, 20))
        self.projectCombobox.setObjectName("projectCombobox")
        self.horizontalLayout_3.addWidget(self.projectCombobox)
        self.addProjBtn = QtWidgets.QPushButton(parent=self.projectOptions)
        font = QtGui.QFont()
        font.setFamily("Open Sans Medium")
        self.addProjBtn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/project/addBtn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.addProjBtn.setIcon(icon2)
        self.addProjBtn.setIconSize(QtCore.QSize(20, 20))
        self.addProjBtn.setObjectName("addProjBtn")
        self.horizontalLayout_3.addWidget(self.addProjBtn)
        self.editProjBtn = QtWidgets.QPushButton(parent=self.projectOptions)
        font = QtGui.QFont()
        font.setFamily("Open Sans Medium")
        self.editProjBtn.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/project/editProjectBtn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.editProjBtn.setIcon(icon3)
        self.editProjBtn.setIconSize(QtCore.QSize(20, 20))
        self.editProjBtn.setObjectName("editProjBtn")
        self.horizontalLayout_3.addWidget(self.editProjBtn)
        self.resetProjBtn = QtWidgets.QPushButton(parent=self.projectOptions)
        font = QtGui.QFont()
        font.setFamily("Open Sans Medium")
        self.resetProjBtn.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/project/resetProjectBtn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.resetProjBtn.setIcon(icon4)
        self.resetProjBtn.setIconSize(QtCore.QSize(20, 20))
        self.resetProjBtn.setObjectName("resetProjBtn")
        self.horizontalLayout_3.addWidget(self.resetProjBtn)
        spacerItem1 = QtWidgets.QSpacerItem(14, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.deleteProjBtn = QtWidgets.QPushButton(parent=self.projectOptions)
        font = QtGui.QFont()
        font.setFamily("Open Sans Medium")
        self.deleteProjBtn.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/project/deleteProjectBtn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.deleteProjBtn.setIcon(icon5)
        self.deleteProjBtn.setIconSize(QtCore.QSize(20, 20))
        self.deleteProjBtn.setObjectName("deleteProjBtn")
        self.horizontalLayout_3.addWidget(self.deleteProjBtn)
        self.horizontalLayout.addWidget(self.projectOptions)
        spacerItem2 = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.switchLayoutBtn = QtWidgets.QVBoxLayout()
        self.switchLayoutBtn.setObjectName("switchLayoutBtn")
        self.horizontalLayout.addLayout(self.switchLayoutBtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalWidget_3 = QtWidgets.QWidget(parent=self.top)
        self.horizontalWidget_3.setStyleSheet("color: black")
        self.horizontalWidget_3.setObjectName("horizontalWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalWidget_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans Medium")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.horizontalWidget_3)
        self.pushButton_4.setStyleSheet("background: transparent;\n"
"border: 0")
        self.pushButton_4.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/browser/chrome.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon6)
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalWidget_3)
        self.label_3.setMinimumSize(QtCore.QSize(20, 20))
        self.label_3.setMaximumSize(QtCore.QSize(20, 20))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/profile/profile.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.username = QtWidgets.QLabel(parent=self.horizontalWidget_3)
        self.username.setObjectName("username")
        self.horizontalLayout_4.addWidget(self.username)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.label_5 = QtWidgets.QLabel(parent=self.horizontalWidget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.dateExp = QtWidgets.QLabel(parent=self.horizontalWidget_3)
        self.dateExp.setObjectName("dateExp")
        self.horizontalLayout_4.addWidget(self.dateExp)
        spacerItem6 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.horizontalLayout.addWidget(self.horizontalWidget_3)
        self.horizontalWidget_4 = QtWidgets.QWidget(parent=self.top)
        self.horizontalWidget_4.setStyleSheet("QPushButton {\n"
"background: transparent;\n"
"border : 0\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border: 0px solid #747d8c;  \n"
"    color: black; /* Màu chữ khi hover */  \n"
"    background-color: #bbbbbb; /* Màu nền khi hover */  \n"
"    border-radius : 4px \n"
"}\n"
"\n"
"#closeBtnProj:hover { \n"
"    background-color: #ff4800  /* Màu nền khi hover cho nút closeBtnProj */  \n"
"}  ")
        self.horizontalWidget_4.setObjectName("horizontalWidget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.minimizeBtnProj = QtWidgets.QPushButton(parent=self.horizontalWidget_4)
        self.minimizeBtnProj.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/iconBtn/minimizeBtn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.minimizeBtnProj.setIcon(icon7)
        self.minimizeBtnProj.setIconSize(QtCore.QSize(16, 16))
        self.minimizeBtnProj.setObjectName("minimizeBtnProj")
        self.horizontalLayout_6.addWidget(self.minimizeBtnProj)
        self.scaleBtnProj = QtWidgets.QPushButton(parent=self.horizontalWidget_4)
        self.scaleBtnProj.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/iconBtn/scaleUpBtn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.scaleBtnProj.setIcon(icon8)
        self.scaleBtnProj.setIconSize(QtCore.QSize(16, 16))
        self.scaleBtnProj.setObjectName("scaleBtnProj")
        self.horizontalLayout_6.addWidget(self.scaleBtnProj)
        self.closeBtnProj = QtWidgets.QPushButton(parent=self.horizontalWidget_4)
        self.closeBtnProj.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/iconBtn/closeBtn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.closeBtnProj.setIcon(icon9)
        self.closeBtnProj.setIconSize(QtCore.QSize(16, 16))
        self.closeBtnProj.setObjectName("closeBtnProj")
        self.horizontalLayout_6.addWidget(self.closeBtnProj)
        self.horizontalLayout.addWidget(self.horizontalWidget_4)
        self.verticalLayout.addWidget(self.top, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.body = QtWidgets.QWidget(parent=self.mainLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setStyleSheet("QWidget#body {  \n"
"    background: url(:/background/threadsBackground.jpg);  \n"
"    background-repeat: no-repeat; /* Đảm bảo hình không lặp lại */  \n"
"    background-position: left; /* Căn giữa hình nền */  \n"
"    background-size: cover; /* Resize hình nền để bao phủ toàn bộ widget */  \n"
"    border-radius : 3px\n"
"}")
        self.body.setObjectName("body")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.smallSidebar = QtWidgets.QWidget(parent=self.body)
        self.smallSidebar.setMinimumSize(QtCore.QSize(50, 0))
        self.smallSidebar.setMaximumSize(QtCore.QSize(50, 16777215))
        self.smallSidebar.setStyleSheet("QPushButton{\n"
"text-align:center;\n"
"padding:6px;\n"
"border-radius:0;\n"
"color:black;\n"
"background:transparent\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 0px solid #747d8c;\n"
"    border-radius : 7px;\n"
"    color: black;\n"
"    background-color: white;\n"
"}")
        self.smallSidebar.setObjectName("smallSidebar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.smallSidebar)
        self.verticalLayout_2.setContentsMargins(0, 19, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.smallHomepageSidebar = QtWidgets.QPushButton(parent=self.smallSidebar)
        self.smallHomepageSidebar.setMinimumSize(QtCore.QSize(45, 45))
        self.smallHomepageSidebar.setMaximumSize(QtCore.QSize(45, 45))
        self.smallHomepageSidebar.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/iconSidebar/homePageSidebar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.smallHomepageSidebar.setIcon(icon10)
        self.smallHomepageSidebar.setObjectName("smallHomepageSidebar")
        self.verticalLayout_2.addWidget(self.smallHomepageSidebar)
        self.smallUploadSidebar = QtWidgets.QPushButton(parent=self.smallSidebar)
        self.smallUploadSidebar.setMinimumSize(QtCore.QSize(45, 45))
        self.smallUploadSidebar.setMaximumSize(QtCore.QSize(45, 45))
        self.smallUploadSidebar.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/iconSidebar/uploadSidebar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.smallUploadSidebar.setIcon(icon11)
        self.smallUploadSidebar.setObjectName("smallUploadSidebar")
        self.verticalLayout_2.addWidget(self.smallUploadSidebar)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.horizontalLayout_2.addWidget(self.smallSidebar)
        self.sidebar = QtWidgets.QWidget(parent=self.body)
        self.sidebar.setMinimumSize(QtCore.QSize(135, 0))
        self.sidebar.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.sidebar.setFont(font)
        self.sidebar.setStyleSheet("QPushButton{\n"
"text-align:left;\n"
"padding:6px;\n"
"border-radius:0;\n"
"color:black;\n"
"font-weight: bold;\n"
"background:transparent\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 0px solid #747d8c;\n"
"    border-radius : 7px;\n"
"    color: black;\n"
"    background-color: #f7f5f6;\n"
"}")
        self.sidebar.setObjectName("sidebar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.sidebar)
        self.verticalLayout_3.setContentsMargins(0, 19, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.homepageSidebar = QtWidgets.QPushButton(parent=self.sidebar)
        self.homepageSidebar.setMinimumSize(QtCore.QSize(0, 45))
        self.homepageSidebar.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.homepageSidebar.setFont(font)
        self.homepageSidebar.setIcon(icon10)
        self.homepageSidebar.setObjectName("homepageSidebar")
        self.verticalLayout_3.addWidget(self.homepageSidebar)
        self.uploadSidebar = QtWidgets.QPushButton(parent=self.sidebar)
        self.uploadSidebar.setMinimumSize(QtCore.QSize(0, 45))
        self.uploadSidebar.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.uploadSidebar.setFont(font)
        self.uploadSidebar.setIcon(icon11)
        self.uploadSidebar.setObjectName("uploadSidebar")
        self.verticalLayout_3.addWidget(self.uploadSidebar)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.horizontalLayout_2.addWidget(self.sidebar)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.body)
        self.stackedWidget.setStyleSheet("background : transparent")
        self.stackedWidget.setObjectName("stackedWidget")
        self.homepageTab = QtWidgets.QWidget()
        self.homepageTab.setStyleSheet("QWidget#homepageTab{\n"
"background:transparent;\n"
"}")
        self.homepageTab.setObjectName("homepageTab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.homepageTab)
        self.horizontalLayout_5.setContentsMargins(0, 21, 21, 21)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.homepageDisplay = QtWidgets.QWidget(parent=self.homepageTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.homepageDisplay.setFont(font)
        self.homepageDisplay.setStyleSheet("QWidget#homepageDisplay {\n"
"background : white;\n"
"border-radius: 23px;\n"
"color: black\n"
"}\n"
"")
        self.homepageDisplay.setObjectName("homepageDisplay")
        self.homepageDisplayLayout = QtWidgets.QVBoxLayout(self.homepageDisplay)
        self.homepageDisplayLayout.setObjectName("homepageDisplayLayout")
        self.horizontalWidget = QtWidgets.QWidget(parent=self.homepageDisplay)
        self.horizontalWidget.setStyleSheet("QPushButton{\n"
"color: black\n"
"}")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.categorySearch = QtWidgets.QComboBox(parent=self.horizontalWidget)
        self.categorySearch.setMinimumSize(QtCore.QSize(0, 0))
        self.categorySearch.setStyleSheet("QComboBox {\n"
"                color: black;  /* Set text color to black */\n"
"                background-color: white;  /* Set background color to white */\n"
"                border: 1px solid gray;  /* Optional: Add a border */\n"
"                border-radius: 5px;  /* Optional: Add rounded corners */\n"
"                padding: 5px;  /* Optional: Add padding */\n"
"            }\n"
"            QComboBox QAbstractItemView {\n"
"                color: black;  /* Set text color for dropdown items to black */\n"
"                background-color: white;  /* Set background color for dropdown items to white */\n"
"                selection-background-color: lightgray;  /* Optional: Set background color for selected item */\n"
"                selection-color: black;  /* Optional: Set text color for selected item */\n"
"            }\n"
"            QComboBox::drop-down {\n"
"                border: none;  /* Remove border from drop-down button */\n"
"                width: 20px;  /* Set the width of the drop-down button */\n"
"            }\n"
"            QComboBox::down-arrow {\n"
"                image: url(:/icons/down_arrow.png);  /* Set a custom down arrow image */\n"
"                width: 10px;  /* Set the width of the down arrow */\n"
"                height: 10px;  /* Set the height of the down arrow */\n"
"                right: 5px;  /* Position the arrow 5px from the right */\n"
"            }")
        self.categorySearch.setObjectName("categorySearch")
        self.horizontalLayout_7.addWidget(self.categorySearch)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.horizontalWidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_7.addWidget(self.lineEdit)
        spacerItem9 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.addAccBtn = QtWidgets.QPushButton(parent=self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.addAccBtn.setFont(font)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/account/addAcc.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.addAccBtn.setIcon(icon12)
        self.addAccBtn.setObjectName("addAccBtn")
        self.horizontalLayout_7.addWidget(self.addAccBtn)
        spacerItem10 = QtWidgets.QSpacerItem(19, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.addMoreAcc = QtWidgets.QPushButton(parent=self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.addMoreAcc.setFont(font)
        self.addMoreAcc.setStyleSheet("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/account/addmoreAcc.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.addMoreAcc.setIcon(icon13)
        self.addMoreAcc.setIconSize(QtCore.QSize(19, 19))
        self.addMoreAcc.setObjectName("addMoreAcc")
        self.horizontalLayout_7.addWidget(self.addMoreAcc)
        spacerItem11 = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.homepageDisplayLayout.addWidget(self.horizontalWidget, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout_5.addWidget(self.homepageDisplay)
        self.stackedWidget.addWidget(self.homepageTab)
        self.uploadTab = QtWidgets.QWidget()
        self.uploadTab.setObjectName("uploadTab")
        self.stackedWidget.addWidget(self.uploadTab)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.body)
        self.gridLayout.addWidget(self.mainLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "instathread"))
        self.addProjBtn.setText(_translate("MainWindow", "Thêm"))
        self.editProjBtn.setText(_translate("MainWindow", "Sửa"))
        self.resetProjBtn.setText(_translate("MainWindow", "Reset"))
        self.deleteProjBtn.setText(_translate("MainWindow", "Xóa"))
        self.label_2.setText(_translate("MainWindow", "Trình duyệt:"))
        self.username.setText(_translate("MainWindow", "user"))
        self.label_5.setText(_translate("MainWindow", "Hết hạn:"))
        self.dateExp.setText(_translate("MainWindow", "11/3/24"))
        self.homepageSidebar.setText(_translate("MainWindow", "Trang Chủ"))
        self.uploadSidebar.setText(_translate("MainWindow", "Tải Lên"))
        self.addAccBtn.setText(_translate("MainWindow", "Thêm"))
        self.addMoreAcc.setText(_translate("MainWindow", "Thêm nhiều"))
