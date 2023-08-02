import sys
from PySide6.QtCore import Qt, Slot, QTimer
from PySide6.QtGui import QMovie, QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,400)
        self.setWindowTitle("Janela Básica")
        self.main_vLayout = QVBoxLayout()
        self.label_image = QLabel()
        self.main_vLayout.addWidget(self.label_image)
        
        self.image = QImage(r'Pyside/Imgs/images.jpg')
        self.pixmap = QPixmap(self.image.scaledToWidth(100))
        self.label_image.setPixmap(self.pixmap)


        
        self.setLayout(self.main_vLayout)



#Inicialização da Aplicação
app = QApplication([])
window = Window()
window.show()

sys.exit(app.exec())