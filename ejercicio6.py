import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QComboBox, QSpinBox

class NameAgeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.name_label = QLabel("Ingrese su nombre completo:")
        layout.addWidget(self.name_label)

        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)

        self.age_label = QLabel("Seleccione su edad:")
        layout.addWidget(self.age_label)

        self.age_input = QSpinBox()
        self.age_input.setRange(1, 120)  
        layout.addWidget(self.age_input)

        self.gender_label = QLabel("Seleccione su género:")
        layout.addWidget(self.gender_label)

        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Masculino", "Femenino", "Otro"])
        layout.addWidget(self.gender_combo)

        self.button = QPushButton("Mostrar datos")
        self.button.clicked.connect(self.show_info)
        layout.addWidget(self.button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setWindowTitle('Datos personales con Widgets')
        self.setGeometry(100, 100, 400, 200)
        self.show()

    def show_info(self):
        name = self.name_input.text()
        age = self.age_input.value()
        gender = self.gender_combo.currentText()

        self.result_label.setText(f"Nombre: {name}, Edad: {age}, Género: {gender}")

app = QApplication(sys.argv)
window = NameAgeWindow()
sys.exit(app.exec_())
