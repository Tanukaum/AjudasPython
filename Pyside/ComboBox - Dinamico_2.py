import sys
import requests
from bs4 import BeautifulSoup
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QVBoxLayout, QWidget, QComboBox)

global App, Index
App = ''
Index = ''

#Usado para listar quais máquinas estão sendo verificadas e as aplicações de cada uma delas
url_of_all_machines = ['IP_ADDRESS']
list_nicks_machines = list()
list_programs = list()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,300,100)
        self.setWindowTitle("ComboBox - Dinâmico 2")
        self.main_vLayout = QVBoxLayout()

            
        self.setLayout(self.main_vLayout)
        self.get_machines_names(url_of_all_machines)
		
        self.combo_machine_name = QComboBox()
        self.main_vLayout.addWidget(self.combo_machine_name)
		
        self.combo_app = QComboBox()
        self.main_vLayout.addWidget(self.combo_app)

        for i in range(len(list_nicks_machines)):
            list_programs.clear()
            list_programs.append('Choose the Application')
			
            if i != 0:
                self.get_app_list(url_of_all_machines)
			
            self.combo_machine_name.addItem(list_nicks_machines[i], list_programs)

        self.combo_machine_name.currentIndexChanged.connect(self.updateAppCombo)
        self.combo_machine_name.activated.connect(self.on_change_machine)
        self.combo_app.activated.connect(self.on_change_app)

        self.updateAppCombo(self.combo_machine_name.currentIndex())
    
    def get_machines_names(self, URL_of_all):
        list_nicks_machines.clear()
        list_nicks_machines.append('Choose the Machine')
        for i in range(len(URL_of_all)):
            self.response = requests.get(URL_of_all[i] + '/check')
            self.soup = BeautifulSoup(self.response.text, 'html.parser')
            self.machine_name = self.soup.find(id = 'machine_name')
			
            list_nicks_machines.append(self.machine_name.text)
		

    def get_app_list(self, machine_url):
        for url in machine_url:
            self.response = requests.get(url + '/check')
            self.soup = BeautifulSoup(self.response.text, 'html.parser')
            self.apps_names = self.soup.find_all(id = 'app_name')
            for app_name in self.apps_names:
                list_programs.append(app_name.text)
	
    @Slot()
    def updateAppCombo(self, index):
        global Index
        Index = int(self.combo_machine_name.currentIndex())
		
        self.combo_app.clear()
        apps_list = self.combo_machine_name.itemData(index)
        if apps_list:
            self.combo_app.addItems(apps_list)
		
	
    @Slot()
    def on_change_app(self):
        global App
        App = self.combo_app.currentText()
		
        if (App == '') or App == ('Choose the Application'):
            return
        else:
            self.label.setText('Working on app: ' + App)
		

    @Slot()
    def on_change_machine(self):
        global Index
        Index = self.combo_machine_name.currentIndex()
        if Index != 0:
            self.label.setText('Working on machine: ' + list_nicks_machines[Index] + '   URL: ' + url_of_all_machines[Index-1])


#Inicialização da Aplicação
app = QApplication([])
window = Window()
window.show()

sys.exit(app.exec())