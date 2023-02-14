import sys
from PySide6.QtCore import Qt, Slot, QTimer
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,100,100)
        self.setWindowTitle("Gif")
        self.main_vLayout = QVBoxLayout()

        self.label = QLabel(self)
        self.main_vLayout.addWidget(self.label)
        
        self.movie = QMovie(r'Imgs\loop.gif')
        self.label.setMovie(self.movie)
		
        self.movie.start()

        self.setLayout(self.main_vLayout)



#Inicialização da Aplicação
app = QApplication([])
window = Window()
window.show()

sys.exit(app.exec())