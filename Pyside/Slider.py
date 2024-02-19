from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtWidgets import QFileSystemModel, QTreeView, QVBoxLayout, QWidget
import sys
class MainWindow(QtWidgets.QMainWindow):
	# Carrega a interface
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.ui = uic.loadUi('Pyside\\UI\\GUI_slider.ui', self)
        self.setWindowTitle("Slider")
        self.main_vLayout = QVBoxLayout()
        self.slider.valueChanged.connect(self.get_slider_value)
        
        self.setLayout(self.main_vLayout)

    def get_slider_value(self, value):
        print(type(value))


# executa o software
app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())