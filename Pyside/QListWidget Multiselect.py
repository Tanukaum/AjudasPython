import sys
from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QListWidget, QVBoxLayout, QWidget, QAbstractItemView, QPushButton)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,400)
        self.setWindowTitle("Janela Básica")
        self.main_vLayout = QVBoxLayout()

        self.list = QListWidget(self)
        self.list.setSelectionMode(QAbstractItemView.MultiSelection)
        ##self.list.setSelectionMode(QAbstractItemView.ExtendedSelection)##Usa Ctrl para selecionar vários
        self.button = QPushButton('Botão Clicável')
        self.main_vLayout.addWidget(self.button)
        self.button.clicked.connect(self.clique)


        for i in range(5):
            self.list.addItem('item ' + str(i))
        
        self.list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list.setMinimumHeight((self.list.sizeHint().height()))

        self.list.setFont(QFont('Arial', 14))

        #self.list.itemClicked.connect(self.printItemText)
        
        self.setLayout(self.main_vLayout)

    def printItemText(self):
        items = self.list.selectedItems()
        x = []
        for i in range(len(items)):
            x.append(str(self.list.selectedItems()[i].text()))

        print('\nPrint ao clicar em item:  ')
        print(x)

    def save_clique(self):
        items = self.list.selectedItems()
        text = []
        index = []
        print(self.list.selectedIndexes())
        for i in range(len(items)):
            text.append(str(self.list.selectedItems()[i].text()))
            index.append(str(self.list.selectedIndexes()[i].row()))
        return text, index

    def clique(self):
        item_text, item_index = self.save_clique()
            
        print('\nPrint pelo botão:  ')
        for text, index in zip(item_text, item_index) :
            print(text + ' - ' + index)
           



#Inicialização da Aplicação
app = QApplication([])
window = Window()
window.show()

sys.exit(app.exec())