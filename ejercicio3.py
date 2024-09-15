import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class CedulaNombreWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.cedula_label = QLabel("Ingrese su número de cédula:")
        layout.addWidget(self.cedula_label)

        self.cedula_input = QLineEdit()
        layout.addWidget(self.cedula_input)

        self.nombre_label = QLabel("Ingrese su nombre completo:")
        layout.addWidget(self.nombre_label)

        self.nombre_input = QLineEdit()
        layout.addWidget(self.nombre_input)

        self.button = QPushButton("Mostrar información")
        self.button.clicked.connect(self.show_info)
        layout.addWidget(self.button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setWindowTitle('Ingreso de Cédula y Nombre')
        self.show()

    def show_info(self):
        cedula = self.cedula_input.text()
        nombre = self.nombre_input.text()

        self.result_label.setText(f"Cédula: {cedula}, Nombre: {nombre}")

app = QApplication(sys.argv)
window = CedulaNombreWindow()
sys.exit(app.exec_())
