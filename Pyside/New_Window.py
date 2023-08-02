import sys
from PySide6.QtCore import Qt, Slot, QTimer
from PySide6.QtGui import QMovie, QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget)

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,400)
        self.setWindowTitle("Janela Básica")
        self.main_vLayout = QVBoxLayout()
        self.label_nw = QLabel('Janela 2')
        self.main_vLayout.addWidget(self.label_nw)

        self.setLayout(self.main_vLayout)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.window2 = Window2()

        self.setGeometry(100,100,500,400)
        self.setWindowTitle("Janela Básica")
        self.main_vLayout = QVBoxLayout()
        self.label = QLabel('Janela 1')
        self.main_vLayout.addWidget(self.label)

        self.button = QPushButton('Botão Clicável')
        self.main_vLayout.addWidget(self.button)
        self.button.clicked.connect(self.clique)
        
        
        self.setLayout(self.main_vLayout)

    def clique(self):
        if self.window2.isVisible():
            self.window2.hide()
        else:
            self.window2.show()
        
        print(self.window2.label_nw.text())

            




#Inicialização da Aplicação
app = QApplication([])
window = MainWindow()
window.show()

sys.exit(app.exec())