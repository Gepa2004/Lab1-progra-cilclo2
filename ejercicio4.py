import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MascotasWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.mascota1_label = QLabel("Datos de la primera mascota:")
        layout.addWidget(self.mascota1_label)

        self.nombre_mascota1 = QLineEdit("Nombre:")
        layout.addWidget(self.nombre_mascota1)

        self.edad_mascota1 = QLineEdit("Edad:")
        layout.addWidget(self.edad_mascota1)

        self.raza_mascota1 = QLineEdit("Raza:")
        layout.addWidget(self.raza_mascota1)

        self.mascota2_label = QLabel("Datos de la segunda mascota:")
        layout.addWidget(self.mascota2_label)

        self.nombre_mascota2 = QLineEdit("Nombre:")
        layout.addWidget(self.nombre_mascota2)

        self.edad_mascota2 = QLineEdit("Edad:")
        layout.addWidget(self.edad_mascota2)

        self.raza_mascota2 = QLineEdit("Raza:")
        layout.addWidget(self.raza_mascota2)

        self.mascota3_label = QLabel("Datos de la tercera mascota:")
        layout.addWidget(self.mascota3_label)

        self.nombre_mascota3 = QLineEdit("Nombre:")
        layout.addWidget(self.nombre_mascota3)

        self.edad_mascota3 = QLineEdit("Edad.")
        layout.addWidget(self.edad_mascota3)

        self.raza_mascota3 = QLineEdit("Raza:")
        layout.addWidget(self.raza_mascota3)

        self.button = QPushButton("Mostrar información de las mascotas")
        self.button.clicked.connect(self.show_info)
        layout.addWidget(self.button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setWindowTitle('Datos de Mascotas')
        self.show()

    def show_info(self):
        mascota1 = f"Mascota 1 - Nombre: {self.nombre_mascota1.text()}, Edad: {self.edad_mascota1.text()}, Raza: {self.raza_mascota1.text()}"
        mascota2 = f"Mascota 2 - Nombre: {self.nombre_mascota2.text()}, Edad: {self.edad_mascota2.text()}, Raza: {self.raza_mascota2.text()}"
        mascota3 = f"Mascota 3 - Nombre: {self.nombre_mascota3.text()}, Edad: {self.edad_mascota3.text()}, Raza: {self.raza_mascota3.text()}"

        self.result_label.setText(f"{mascota1}\n{mascota2}\n{mascota3}")

app = QApplication(sys.argv)
window = MascotasWindow()
sys.exit(app.exec_())
