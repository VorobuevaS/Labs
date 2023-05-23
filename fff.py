from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedWidth(500)
        self.setFixedHeight(620)
        self.setWindowTitle("Калькулятор")
        self.plus = 0
        self.ravno = False
        self.ravno2 = False
        self.spisok = []
        self.spisokdeistvii = []
        self.sh = 0
        self.k = 0
        self.u()

    '''def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()'''

    def u(self):
        self.btn = QPushButton("1", self)
        self.btn.setGeometry(20, 140, 100, 100)
        self.btn.setStyleSheet("background-color: lightyellow")
        self.btn.setFont(QFont("Arial", 16))
        self.btn2 = QPushButton("2", self)
        self.btn2.setGeometry(140, 140, 100, 100)
        self.btn2.setStyleSheet("background-color: lightyellow")
        self.btn2.setFont(QFont("Arial", 16))
        self.btn0 = QPushButton("0", self)
        self.btn0.setGeometry(20, 500, 100, 100)
        self.btn0.setStyleSheet("background-color: lightyellow")
        self.btn0.setFont(QFont("Arial", 16))
        self.btn3 = QPushButton("3", self)
        self.btn3.setGeometry(260, 140, 100, 100)
        self.btn3.setStyleSheet("background-color: lightyellow")
        self.btn3.setFont(QFont("Arial", 16))
        self.btn4 = QPushButton("4", self)
        self.btn4.setGeometry(20, 260, 100, 100)
        self.btn4.setStyleSheet("background-color: lightyellow")
        self.btn4.setFont(QFont("Arial", 16))
        self.btn5 = QPushButton("5", self)
        self.btn5.setGeometry(140, 260, 100, 100)
        self.btn5.setStyleSheet("background-color: lightyellow")
        self.btn5.setFont(QFont("Arial", 16))
        self.btn6 = QPushButton("6", self)
        self.btn6.setGeometry(260, 260, 100, 100)
        self.btn6.setStyleSheet("background-color: lightyellow")
        self.btn6.setFont(QFont("Arial", 16))
        self.btn7 = QPushButton("7", self)
        self.btn7.setGeometry(20, 380, 100, 100)
        self.btn7.setStyleSheet("background-color: lightyellow")
        self.btn7.setFont(QFont("Arial", 16))
        self.btn8 = QPushButton("8", self)
        self.btn8.setGeometry(140, 380, 100, 100)
        self.btn8.setStyleSheet("background-color: lightyellow")
        self.btn8.setFont(QFont("Arial", 16))
        self.btn9 = QPushButton("9", self)
        self.btn9.setGeometry(260, 380, 100, 100)
        self.btn9.setStyleSheet("background-color: lightyellow")
        self.btn9.setFont(QFont("Arial", 16))
        self.l = QLabel(self)
        self.l.move(20, 20)
        self.l.setStyleSheet("background-color: lightgreen")
        self.l.setFixedWidth(460)
        self.l.setFixedHeight(100)
        self.l.setFont(QFont("Arial", 24))
        self.btn10 = QPushButton("+", self)
        self.btn10.setGeometry(380, 140, 100, 100)
        self.btn10.setFont(QFont("Arial", 16))
        self.btn10.setStyleSheet("background-color: lightgreen")
        self.btn11 = QPushButton("-", self)
        self.btn11.setGeometry(380, 260, 100, 100)
        self.btn11.setFont(QFont("Arial", 16))
        self.btn11.setStyleSheet("background-color: lightgreen")
        self.btn12 = QPushButton("*", self)
        self.btn12.setGeometry(380, 380, 100, 100)
        self.btn12.setFont(QFont("Arial", 16))
        self.btn12.setStyleSheet("background-color: lightgreen")
        self.btn13 = QPushButton("/", self)
        self.btn13.setGeometry(380, 500, 100, 100)
        self.btn13.setFont(QFont("Arial", 16))
        self.btn13.setStyleSheet("background-color: lightgreen")
        self.btn14 = QPushButton("=", self)
        self.btn14.setGeometry(140, 500, 220, 100)
        self.btn14.setFont(QFont("Arial", 16))
        self.btn14.setStyleSheet("background-color: lightblue")
        self.btn0.clicked.connect(self.act0)
        self.btn.clicked.connect(self.act1)
        self.btn2.clicked.connect(self.act2)
        self.btn3.clicked.connect(self.act3)
        self.btn4.clicked.connect(self.act4)
        self.btn5.clicked.connect(self.act5)
        self.btn6.clicked.connect(self.act6)
        self.btn7.clicked.connect(self.act7)
        self.btn8.clicked.connect(self.act8)
        self.btn9.clicked.connect(self.act9)
        self.btn10.clicked.connect(self.act10)
        self.btn14.clicked.connect(self.act14)
        self.btn11.clicked.connect(self.act11)
        self.btn12.clicked.connect(self.act12)
        self.btn13.clicked.connect(self.act13)
    '''def retranslated(self, MainWindow):
        t = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(t("MainWindow", "MainWindow"))
        self.btn.setText(t("MainWindow", "Push Button"))
        self.btn2.setText(t("MainWindow", "Push Button"))'''
    def act0(self):
        if self.ravno2 == False:
          z = "0"
          self.l.setText(str(eval(self.l.text() + z)))
        else:
            self.l.clear()
            self.spisok.clear()
            self.spisokdeistvii.clear()
            self.sh = 0
            z = "0"
            self.l.setText(str(eval(self.l.text() + z)))
            self.ravno2 = False
    def act1(self):
        if self.ravno2 == False:
          z = "1"
          self.l.setText(str(eval(self.l.text() + z)))
        else:
            self.l.clear()
            self.spisok.clear()
            self.spisokdeistvii.clear()
            self.sh = 0
            z = "1"
            self.l.setText(str(eval(self.l.text() + z)))
            self.ravno2 = False
    def act3(self):
        if self.ravno2 == False:
          z = "3"
          self.l.setText(str(eval(self.l.text() + z)))
        else:
            self.l.clear()
            self.spisok.clear()
            self.spisokdeistvii.clear()
            self.sh = 0
            z = "3"
            self.l.setText(str(eval(self.l.text() + z)))
            self.ravno2 = False
    def act2(self):
        if self.ravno2 == False:
            z = "2"
            self.l.setText(str(eval(self.l.text() + z)))
        else:
            self.l.clear()
            self.spisok.clear()
            self.spisokdeistvii.clear()
            self.sh = 0
            z = "2"
            self.l.setText(str(eval(self.l.text() + z)))
            self.ravno2 = False
    def act4(self):
        if self.ravno2 == False:
          z = "4"
          self.l.setText(str(eval(self.l.text() + z)))
        else:
            self.l.clear()
            self.spisok.clear()
            self.spisokdeistvii.clear()
            self.sh = 0
            z = "4"
            self.l.setText(str(eval(self.l.text() + z)))
            self.ravno2 = False
    def act5(self):
        if self.ravno2 == False:
          z = "5"
          self.l.setText(str(eval(self.l.text() + z)))
        else:
            self.l.clear()
            self.spisok.clear()
            self.spisokdeistvii.clear()
            self.sh = 0
            z = "5"
            self.l.setText(str(eval(self.l.text() + z)))
            self.ravno2 = False

    def act6(self):
        if self.ravno2 == False:
          z = "6"
          self.l.setText(str(eval(self.l.text() + z)))
        else:
            self.l.clear()
            self.spisok.clear()
            self.spisokdeistvii.clear()
            self.sh = 0
            z = "6"
            self.l.setText(str(eval(self.l.text() + z)))
            self.ravno2 = False

    def act7(self):
        if self.ravno2 == False:
          z = "7"
          self.l.setText(str(eval(self.l.text() + z)))
        else:
            self.l.clear()
            self.spisok.clear()
            self.spisokdeistvii.clear()
            self.sh = 0
            z = "7"
            self.l.setText(str(eval(self.l.text() + z)))
            self.ravno2 = False
    def act8(self):
        if self.ravno2 == False:
          z = "8"
          self.l.setText(str(eval(self.l.text() + z)))
        else:
            self.l.clear()
            self.spisok.clear()
            self.spisokdeistvii.clear()
            self.sh = 0
            z = "8"
            self.l.setText(str(eval(self.l.text() + z)))
            self.ravno2 = False

    def act9(self):
        if self.ravno2 == False:
          z = "9"
          self.l.setText(str(eval(self.l.text() + z)))
        else:
            self.l.clear()
            self.spisok.clear()
            self.spisokdeistvii.clear()
            self.sh = 0
            z = "9"
            self.l.setText(str(eval(self.l.text() + z)))
            self.ravno2 = False
    def act11(self):
          z = "-"
          self.spisok.append(self.l.text())
          self.l.setText(str(self.l.text() + z))
          self.spisokdeistvii.append(2)
          self.l.clear()
          self.sh += 1
    def act10(self):
           z = "+"
           self.spisok.append(self.l.text())
           self.l.setText(str(self.l.text() + z))
           self.spisokdeistvii.append(1)
           self.l.clear()
           self.sh += 1
    def act12(self):
           z = "*"
           self.spisok.append(self.l.text())
           self.l.setText(str(self.l.text() + z))
           self.spisokdeistvii.append(3)
           self.l.clear()
           self.sh += 1
    def act13(self):
           z = "/"
           self.spisok.append(self.l.text())
           self.l.setText(str(self.l.text() + z))
           self.spisokdeistvii.append(4)
           self.l.clear()
           self.sh += 1
    def act14(self):
           self.ravno2 = True
           self.spisok.append(self.l.text())
           self.spisokdeistvii.append(5)
           self.sh += 1
           for i in range(0, self.sh, 1):
               if self.spisokdeistvii[i] == 1 and i == 0:
                  self.k = int(self.spisok[i]) + int(self.spisok[i+1])
               elif self.spisokdeistvii[i] == 1 and i != 0:
                   self.k = int(self.k) + int(self.spisok[i+1])

               elif self.spisokdeistvii[i] == 2 and i == 0:
                   self.k = (int(self.spisok[i]) - int(self.spisok[i+1]))
               elif self.spisokdeistvii[i] == 2 and i != 0:
                   self.k = int(self.k) - int(self.spisok[i+1])

               elif self.spisokdeistvii[i] == 3 and i == 0:
                   self.k = (int(self.spisok[i]) * int(self.spisok[i+1]))
               elif self.spisokdeistvii[i] == 3 and i != 0:
                   self.k = int(self.k) * int(self.spisok[i+1])

               elif self.spisokdeistvii[i] == 4 and i == 0:
                   if self.spisok[i+1] == 0:
                      self.l.clear()
                      self.l.setText(str("Error"))
                   self.k = (int(self.spisok[i]) / int(self.spisok[i+1]))

               elif self.spisokdeistvii[i] == 4 and i != 0:
                   if self.spisok[i+1] == 0:
                      self.l.clear()
                      self.l.setText("Error")
                   self.k = int(self.k) / int(self.spisok[i+1])

               elif self.spisokdeistvii[i] == 5:
                       self.l.setText(str(self.k))
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())