import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class PersonaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.datos_labels = []
        self.datos_inputs = []

        datos = ["Nombre", "Edad", "Dirección", "Correo Electrónico", "Teléfono",
                 "Ocupación", "Nacionalidad", "Género", "Estado Civil", "Hobbies"]

        for dato in datos:
            label = QLabel(f"Ingrese su {dato}:")
            input_field = QLineEdit()

            layout.addWidget(label)
            layout.addWidget(input_field)

            self.datos_labels.append(label)
            self.datos_inputs.append(input_field)

        self.button = QPushButton("Mostrar datos ingresados")
        self.button.clicked.connect(self.show_info)
        layout.addWidget(self.button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setWindowTitle('Ingreso de Datos de una Persona')
        self.show()

    def show_info(self):
        resultado = []
        for label, input_field in zip(self.datos_labels, self.datos_inputs):
            resultado.append(f"{label.text().replace('Ingrese su ', '')}: {input_field.text()}")

        self.result_label.setText("\n".join(resultado))

app = QApplication(sys.argv)
window = PersonaWindow()
sys.exit(app.exec_())
