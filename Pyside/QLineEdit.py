import sys
from PySide6.QtWidgets import (QApplication, QVBoxLayout, QWidget, QLineEdit)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,400)
        self.setWindowTitle("Janela Básica")
        self.main_vLayout = QVBoxLayout()
        
        self.line_edit = QLineEdit()
        self.main_vLayout.addWidget(self.line_edit)
        
        self.setLayout(self.main_vLayout)


#Inicialização da Aplicação
app = QApplication([])
window = Window()
window.show()

sys.exit(app.exec())