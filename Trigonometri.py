import sys
import math

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setFixedSize(400, 150)
        self.move(300, 300)
        self.setWindowTitle('Trigonometri')

        self.label1 = QLabel()
        self.label1.setText('Masukkan sudut')
        self.linepertama = QLineEdit()
        horizontalLine = QFrame()
        horizontalLine.setFrameShape(QFrame.HLine)
        horizontalLine.setFrameShadow(QFrame.Sunken)

        self.sin = QRadioButton('Sinus')
        self.cos = QRadioButton('Cosinus')
        self.tan = QRadioButton('Tangen')

        self.myfont = QFont()
        self.myfont.setBold(True)
        self.hasil = QLabel()
        self.hasil.setFont(self.myfont)
        self.hasil.setText('Hasil')
        self.hitung = QPushButton()
        self.hitung.setText('Hitung')

        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.linepertama, 0, 1, 1, 3)
        layout.addWidget(self.sin, 2, 0)
        layout.addWidget(self.cos, 2, 1)
        layout.addWidget(self.tan, 2, 2)
#        layout.addWidget(self.bagi, 2, 3)
        layout.addWidget(horizontalLine, 4, 0, 1, 4)
        layout.addWidget(self.hasil, 5, 0, 1, 2)
        layout.addWidget(self.hitung, 6, 0, 1, 4)

        self.hitung.clicked.connect(self.hitungan)
        self.setLayout(layout)

    def hitungan(self):
        a = float(self.linepertama.text())
        #derajat * math.pi/180
        a = math.radians(a)

        if self.sin.isChecked():
            sinus = math.sin(a)
            self.hasil.setText('Hasil sinus : ' + str(sinus))
        elif self.cos.isChecked():
            cos = math.cos(a)
            self.hasil.setText('Hasil cosinus : ' + str(cos))
        elif self.tan.isChecked():
            tan = math.tan(a)
            self.hasil.setText('Hasil Tangen : ' + str(tan))
        else:
            self.hasil.setText('Belum memilih operasi trigonometri')


if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()