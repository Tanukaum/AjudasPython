import sys
from PySide6.QtCore import Qt, Slot, QTimer
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,400)
        self.setWindowTitle("Botão")
        self.main_vLayout = QVBoxLayout()

        self.button = QPushButton('Botão Clicável')
        self.main_vLayout.addWidget(self.button)
        self.button.clicked.connect(self.clique)
        
        self.setLayout(self.main_vLayout)

    def clique(self):
        print(self.button.text())

#Inicialização da Aplicação
app = QApplication([])
window = Window()
window.show()

sys.exit(app.exec())