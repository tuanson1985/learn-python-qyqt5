import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel,
    QWidget, QVBoxLayout, QHBoxLayout, QCheckBox,
    QGridLayout, QPushButton, QRadioButton, QButtonGroup)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HQGROUP')
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("logo.png"))
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Master card", self)
        self.radio3 = QRadioButton("Gift card", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)

        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        # self.checkbox = QCheckBox("Do you like food?", self)
        # self.button = QPushButton("Click me!", self)
        # self.lable = QLabel("HQGROUP", self)
        self.initUI() 

    def initUI(self):
        self.radio1.setGeometry(10,0,500,100)
        self.radio1.setStyleSheet("font-size: 16px;font-family: Arial")
        self.radio2.setGeometry(10,50,500,100)
        self.radio2.setStyleSheet("font-size: 16px;font-family: Arial")
        self.radio3.setGeometry(10,100,500,100)
        self.radio3.setStyleSheet("font-size: 16px;font-family: Arial")
        self.radio4.setGeometry(10,150,500,100)
        self.radio4.setStyleSheet("font-size: 16px;font-family: Arial")
        self.radio5.setGeometry(10,200,500,100)
        self.radio5.setStyleSheet("font-size: 16px;font-family: Arial")

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)

        # self.checkbox.setGeometry(10,0,500,100)
        # self.checkbox.setStyleSheet("font-size: 16px;font-family: Arial")
        # self.checkbox.setChecked(False)
        # self.checkbox.stateChanged.connect(self.checkbox_changed)
    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")
    # def checkbox_changed(self, state):
    #     print(state)
    
    #     if state == Qt.Checked:
    #         print("You like food")
    #     else:
    #         print("You do not like food")

        # self.button.setGeometry(150, 200,200,100)
        # self.button.setStyleSheet("font-size: 30px")
        # self.button.clicked.connect(self.on_click)

        # self.lable.setGeometry(150,300,200,100)
        # self.lable.setStyleSheet("font-size: 50px")

    # def on_click(self):

        # self.lable.setText("Goodbuye!")

        # print("Button click")
        # self.button.setText("Clicked!")
        # self.button.setDisabled(True)

        # central_widget = QWidget()
        # selt.setCentralWidget(central_widget)

        # label1 = QLabel("#1",selt)
        # label2 = QLabel("#2",selt)
        # label3 = QLabel("#3",selt)
        # label4 = QLabel("#4",selt)
        # label5 = QLabel("#5",selt)

        # label1.setStyleSheet("background-color: red")
        # label2.setStyleSheet("background-color: yellow")
        # label3.setStyleSheet("background-color: green")
        # label4.setStyleSheet("background-color: blue")
        # label5.setStyleSheet("background-color: purple")

        # grid = QGridLayout()

        # grid.addWidget(label1,0,0)
        # grid.addWidget(label2,0,1)
        # grid.addWidget(label3,1,0)
        # grid.addWidget(label4,1,1)
        # grid.addWidget(label5,2,2)

        # central_widget.setLayout(grid)
    
        # hbox = QHBoxLayout()

        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)

        # central_widget.setLayout(hbox)

        # vbox = QVBoxLayout()

        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)

        # central_widget.setLayout(vbox)

        # label = QLabel("Hello", self)
        # label.setFont(QFont("Arial", 30))
        # label.setGeometry(0,0,500,100)
        # label.setStyleSheet("color:blue")
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # label_two = QLabel(self)
        # label_two.setGeometry(0,0,500,500)

        # pixmap = QPixmap("background.jpg")
        # label_two.setPixmap(pixmap)
        # label_two.setScaledContents(True)
        # label_two.setGeometry(
        #     (self.width() - label_two.width()) // 2,
        #     (self.height() - label_two.height()) // 2,
        #     label_two.width(),
        #     label_two.height()
        #     )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

