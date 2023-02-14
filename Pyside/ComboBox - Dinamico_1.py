'''
################################## FROM ######################################
# https://learndataanalysis.org/create-a-dependent-combo-box-pyqt5-tutorial/ #
##############################################################################
'''

import sys
from PySide6.QtWidgets import (QApplication, QVBoxLayout, QWidget, QComboBox)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,300,100)
        self.setWindowTitle("ComboBox - Dinâmico 1")
        self.main_vLayout = QVBoxLayout()

        self.combobox_1 = QComboBox()
        self.main_vLayout.addWidget(self.combobox_1)

        self.combobox_1.addItem('Par', ['2', '4' , '6'])
        self.combobox_1.addItem('Ímpar', ['1', '3' , '5'])


        self.combobox_2 = QComboBox()
        self.main_vLayout.addWidget(self.combobox_2)

        self.combobox_1.currentIndexChanged.connect(self.update_combo2)
        self.update_combo2(self.combobox_1.currentIndex())

		
        self.setLayout(self.main_vLayout)

    def update_combo2(self, index):
        self.combobox_2.clear()
        box_2 = self.combobox_1.itemData(index)

        if box_2:
            self.combobox_2.addItems(box_2)

    

#Inicialização da Aplicação
app = QApplication([])
window = Window()
window.show()

sys.exit(app.exec())