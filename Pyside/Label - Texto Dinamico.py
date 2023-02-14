import sys
from PySide6.QtCore import Qt, Slot, QTimer
from PySide6.QtGui import QMovie, QFont
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget)
i = 0
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,100,100)
        self.setWindowTitle("Label Dinâmico")
        self.main_vLayout = QVBoxLayout()

        self.label = QLabel(self)
        self.label.setFont(QFont('Arial', 20))
        self.label.setText('Label Dinâmico')
        self.label.setAlignment(Qt.AlignHCenter)
        self.main_vLayout.addWidget(self.label)

        self.button = QPushButton('Botão Clicável')
        self.main_vLayout.addWidget(self.button)
        self.button.clicked.connect(self.change_label)
        
        self.setLayout(self.main_vLayout)

    @Slot()
    def change_label(self):
        global i
        if i == 0:
            self.label.setText('0')
            i = 1
        elif i == 1:
            self.label.setText('1')
            i = 0
    
#Inicialização da Aplicação
app = QApplication([])
window = Window()
window.show()

sys.exit(app.exec())