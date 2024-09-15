import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class NameAgeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        layout = QVBoxLayout()

        self.name_label = QLabel("Ingrese su nombre:")
        layout.addWidget(self.name_label)

        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)

        self.age_label = QLabel("Ingrese su edad:")
        layout.addWidget(self.age_label)

        self.age_input = QLineEdit()
        layout.addWidget(self.age_input)

        self.button = QPushButton("Mostrar Nombre")
        self.button.clicked.connect(self.show_info)
        layout.addWidget(self.button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setWindowTitle('Ingreso de Nombre y Edad')
        self.show()

    def show_info(self):
        name = self.name_input.text()
        age = self.age_input.text()

        self.result_label.setText(f"Nombre: {name}, Edad: {age}")
        self.result_label.setAlignment(Qt.AlignCenter)

app = QApplication(sys.argv)
window = NameAgeWindow()
sys.exit(app.exec_())
