import sys
from PySide6.QtCore import Qt, Slot, QTimer
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,280,20)
        self.setWindowTitle("Recall Function - Timer 1s")
        self.main_vLayout = QVBoxLayout()

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.main_vLayout.addWidget(self.label)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_function)
        self.timer.start()

        self.counter = 0
        
        self.setLayout(self.main_vLayout)

    def recurring_function(self):
        self.counter +=1
        self.label.setText("Contador de 1s: %d" % self.counter)

#Inicialização da Aplicação
app = QApplication([])
window = Window()
window.show()

sys.exit(app.exec())