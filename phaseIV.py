import sys
import mysql.connector as s
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit,
    QHBoxLayout, QLabel)





'''
class Login (QWidget):
    def __init__(self):
        super.__init__()

        self.setWindowTitle("Login")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()

        self.prompt1 = QLabel("ID")
        self.prompt2 = QLabel("Password")
        self.line1 = QLineEdit()
        self.line2 = QLineEdit()

        self.b1 = QPushButton("Login")


        self.hbox1.addWidget(prompt1)
'''





class CreateCorporation (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Corporation")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.prompt1 = QLabel("Corporation ID")
        self.line1 = QLineEdit()
        self.prompt2 = QLabel("Long Name")
        self.line2 = QLineEdit()
        self.prompt3 = QLabel("Short Name")
        self.line3 = QLineEdit()
        self.prompt4 = QLabel("Reserved Assets")
        self.line4 = QLineEdit()

        self.b1 = QPushButton("Cancel")
        self.b2 = QPushButton("Create")
        self.b1.clicked.connect(self.on_b1_click)
        self.b2.clicked.connect(self.on_b2_click)

        self.hbox1.addWidget(self.prompt1)
        self.hbox1.addWidget(self.line1)
        self.hbox2.addWidget(self.prompt2)
        self.hbox2.addWidget(self.line2)
        self.hbox3.addWidget(self.prompt3)
        self.hbox3.addWidget(self.line3)
        self.hbox4.addWidget(self.prompt4)
        self.hbox4.addWidget(self.line4)
        self.hbox5.addWidget(self.b1)
        self.hbox5.addWidget(self.b2)


        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.line1.setText("")
        self.line2.setText("")
        self.line3.setText("")
        self.line4.setText("")

    def on_b2_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        createcorp = mydb.cursor()
        try:
            args = [self.line1.text(),self.line2.text(), self.line3.text(), int(self.line4.text())]
            createcorp.callproc("create_corporation", args)
            mydb.commit()
            createcorp.close()
            mydb.close()
        except:
            print("oops")





class CreateBank (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Bank")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.hbox6 = QHBoxLayout()
        self.hbox7 = QHBoxLayout()
        self.hbox8 = QHBoxLayout()
        self.hbox9 = QHBoxLayout()
        self.hbox10 = QHBoxLayout()
        self.prompt1 = QLabel("Bank ID")
        self.line1 = QLineEdit()
        self.prompt2 = QLabel("Bank Name")
        self.line2 = QLineEdit()
        self.prompt3 = QLabel("Street Address")
        self.line3 = QLineEdit()
        self.prompt4 = QLabel("City")
        self.line4 = QLineEdit()
        self.prompt5 = QLabel("State")
        self.line5 = QLineEdit()
        self.prompt6 = QLabel("Zip Code")
        self.line6 = QLineEdit()
        self.prompt7 = QLabel("Reserved Assets")
        self.line7 = QLineEdit()
        self.prompt8 = QLabel("Corporation ID")
        self.line8 = QLineEdit()
        self.prompt9 = QLabel("Manager")
        self.line9 = QLineEdit()

        self.b1 = QPushButton("Cancel")
        self.b2 = QPushButton("Create")
        self.b1.clicked.connect(self.on_b1_click)
        self.b2.clicked.connect(self.on_b2_click)

        self.hbox1.addWidget(self.prompt1)
        self.hbox1.addWidget(self.line1)
        self.hbox2.addWidget(self.prompt2)
        self.hbox2.addWidget(self.line2)
        self.hbox3.addWidget(self.prompt3)
        self.hbox3.addWidget(self.line3)
        self.hbox4.addWidget(self.prompt4)
        self.hbox4.addWidget(self.line4)
        self.hbox5.addWidget(self.prompt5)
        self.hbox5.addWidget(self.line5)
        self.hbox6.addWidget(self.prompt6)
        self.hbox6.addWidget(self.line6)
        self.hbox7.addWidget(self.prompt7)
        self.hbox7.addWidget(self.line7)
        self.hbox8.addWidget(self.prompt8)
        self.hbox8.addWidget(self.line8)
        self.hbox9.addWidget(self.prompt9)
        self.hbox9.addWidget(self.line9)
        self.hbox10.addWidget(self.b1)
        self.hbox10.addWidget(self.b2)


        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addLayout(self.hbox6)
        self.vbox.addLayout(self.hbox7)
        self.vbox.addLayout(self.hbox8)
        self.vbox.addLayout(self.hbox9)
        self.vbox.addLayout(self.hbox10)
        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.line1.setText("")
        self.line2.setText("")
        self.line3.setText("")
        self.line4.setText("")
        self.line5.setText("")
        self.line6.setText("")
        self.line7.setText("")
        self.line8.setText("")
        self.line9.setText("")

    def on_b2_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        createbank = mydb.cursor()
        try:
            args = [self.line1.text(),self.line2.text(), self.line3.text(), self.line4.text(), self.line5.text(), self.line6.text(), int(self.line7.text()), self.line8.text(), self.line9.text(), ""]
            createbank.callproc("create_bank", args)
            mydb.commit()
            createbank.close()
            mydb.close()
        except:
            print("oops")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CreateBank()
    main.show()
    sys.exit(app.exec_())



