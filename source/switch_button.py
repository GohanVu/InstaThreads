from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPixmap, QColor, QFont, QPainterPath, QBrush, QPen
from PyQt6.QtCore import QSize, QRectF, QPropertyAnimation, pyqtProperty, Qt

class SwitchButton(QWidget):
    def __init__(self, homePage=None,ui=None):
        super().__init__()
        self.ui = ui
        self.setFixedSize(QSize(153, 30))
        self._checked = False
        self.homePage = homePage
      
        self._background_color = QColor(0, 0, 0)
        self.knob_color = QColor(255, 255, 255)
        self._knob_pos = QRectF(0, 0, 30, 30)
        self.animation = QPropertyAnimation(self, b"knob_pos")
        self.animation.setDuration(200)
        self.setChecked(self._checked)
        self.background_image = QPixmap(":/photos/instagradientsquare.png")
        self.text = "Instagram"
        self.text2 = "Threads"

        # Images for the switch knob
        self.knob_image2 = QPixmap(":/photos/switchinsta.png")
        self.knob_image = QPixmap(":/photos/switchthreads.png")
        
    @pyqtProperty(QRectF)
    def knob_pos(self):
        return self._knob_pos

    @knob_pos.setter
    def knob_pos(self, pos):
        self._knob_pos = pos
        self.update()

    def setChecked(self, checked):
        self._checked = checked
        if self._checked:
            print('threads')
            self.homePage.setUpTheme(1)
            self._background_color = QColor(0, 0, 0)
            self.animation.setStartValue(QRectF(0, 0, 30, 30))
            self.animation.setEndValue(QRectF(123, 0, 30, 30))
        else:
            print('instagram')
            self.homePage.setUpTheme(0)
            self._background_color = QColor(255, 0, 0)
            self.animation.setStartValue(QRectF(123, 0, 30, 30))
            self.animation.setEndValue(QRectF(0, 0, 30, 30))
            
        self.animation.start()

    def mousePressEvent(self, event):
        self.setChecked(not self._checked)
        super().mousePressEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Set font to Open Sans Bold
        font = QFont("Open Sans", 10, QFont.Weight.Bold)
        painter.setFont(font)
        
        # Draw background with rounded corners
        path = QPainterPath()
        path.addRoundedRect(0, 0, 153, 30, 15, 15)

        painter.save()  # Save the painter's state

        if self._checked:
            painter.setBrush(QBrush(self._background_color))
            painter.setPen(QPen())
            painter.drawPath(path)
            painter.setPen(QColor(255, 255, 255))
            painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self.text2)
        else:
            painter.setClipPath(path)
            painter.drawPixmap(0, 0, self.width(), self.height(), self.background_image)
            painter.setPen(QColor(255, 255, 255))
            painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self.text)

        painter.restore()  # Restore the painter's state before drawing the knob

        # Draw the knob with rounded corners
        knob_path = QPainterPath()
        knob_rect = self._knob_pos.toRect()
        knob_path.addRoundedRect(QRectF(knob_rect), 15, 15)  # Convert QRect to QRectF
        painter.setClipPath(knob_path)
        if self._checked:
            painter.drawPixmap(knob_rect, self.knob_image)
        else:
            painter.drawPixmap(knob_rect, self.knob_image2)

        painter.end()
    
