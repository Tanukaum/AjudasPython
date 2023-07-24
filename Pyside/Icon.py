import sys
from PySide6.QtCore import Qt, Slot, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,300,100)
        self.setWindowTitle("Ícone")
        self.setWindowIcon(QIcon(r'Pyside/Imgs/icon.ico'))
        self.main_vLayout = QVBoxLayout()

        
        self.setLayout(self.main_vLayout)



#Inicialização da Aplicação
app = QApplication([])
window = Window()
window.show()

sys.exit(app.exec())