import sys
import random
from PySide6.QtCore import Qt, Slot, QTimer
from PySide6.QtGui import QMovie,QFont, QColor
from PySide6.QtWidgets import (QApplication, QListWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget,QListWidgetItem)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,400)
        self.setWindowTitle("Janela Básica")
        self.main_vLayout = QVBoxLayout()

        self.list = QListWidget(self)
        for i in range(5):
            self.list.addItem('item ' + str(i))
        
        #Cor de cada linha diferente
        for i in range(5):
            self.list_item = QListWidgetItem('item ' + str(int(i)+4))
            self.list_item.setBackground(QColor('#FA' + str(random.randint(0, 5000))))#Gerar cor 'aleatória'
            self.list.addItem(self.list_item)


        self.list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list.setMinimumHeight((self.list.sizeHint().height()))

        self.list.setFont(QFont('Arial', 14))
        self.main_vLayout.addWidget(self.list)

        
        self.button = QPushButton('Limpar Lista')
        self.main_vLayout.addWidget(self.button)
        self.button.clicked.connect(self.limpar)
        
        self.setLayout(self.main_vLayout)

    def limpar(self):
        self.list.clear()

#Inicialização da Aplicação
app = QApplication([])
window = Window()
window.show()

sys.exit(app.exec())