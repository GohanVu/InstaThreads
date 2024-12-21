from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from source.loginForm import LoginForm


if __name__ == "__main__":
    app = QApplication([])
    loginWindow = LoginForm()
    loginWindow.show()
    app.exec()
