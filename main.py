import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('my name is ARPHAN')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Projet SGBD')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        button = QPushButton('inscription', self)
        button.clicked.connect(self.buttonClicked)

        layout.addWidget(button)
        self.setLayout(layout)

    def buttonClicked(self):
        print('client inscrit')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())





