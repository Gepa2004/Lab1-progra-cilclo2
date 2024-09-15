import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class PasswordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        layout = QVBoxLayout()

        self.label = QLabel("Ingrese su clave:")
        layout.addWidget(self.label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password) 
        layout.addWidget(self.password_input)

        self.button = QPushButton("Mostrar clave ingresada")
        self.button.clicked.connect(self.show_password)
        layout.addWidget(self.button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setWindowTitle('Clave Secreta')
        self.show()

    def show_password(self):
   
        password = self.password_input.text()

        self.result_label.setText(f"La clave es: {password}")

app = QApplication(sys.argv)
window = PasswordWindow()
sys.exit(app.exec_())
