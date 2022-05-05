import sys
import mysql.connector as s
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit,
    QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHeaderView)






class Login (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()

        self.prompt1 = QLabel("ID")
        self.prompt2 = QLabel("Password")
        self.line1 = QLineEdit()
        self.line2 = QLineEdit()

        self.b1 = QPushButton("Login")
        self.b1.clicked.connect(self.on_b1_click)


        self.hbox1.addWidget(self.prompt1)
        self.hbox1.addWidget(self.line1)
        self.hbox2.addWidget(self.prompt2)
        self.hbox2.addWidget(self.line2)

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self.b1)

        self.setLayout(self.vbox)


    def on_b1_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')




        cursor = mydb.cursor()

        cursor.execute("select * from system_admin natural join person")

        data = cursor.fetchall()
        if (self.line1.text(), self.line2.text()) in data:
            self.w = AdminHome()
            self.w.show()
            self.close()
        else:
            self.setWindowTitle("Invald Login!")
            self.line1.setText("")
            self.line2.setText("")




class AdminHome (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Admin Menu")
        self.hbox = QHBoxLayout()
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()

        self.b1 = QPushButton("View Stats")
        self.b2 = QPushButton("Create Corporation")
        self.b2.clicked.connect(self.on_b2_click)
        self.b3 = QPushButton("Create Fee")
        self.b4 = QPushButton("Manage Users")
        self.b5 = QPushButton("Manage Overdraft")
        self.b6 = QPushButton("Hire Worker")
        self.b7 = QPushButton("Pay Employees")
        self.b8 = QPushButton("Replace Manager")
        self.b9 = QPushButton("Manage Accounts")
        self.b10 = QPushButton("Create Bank")

        self.vbox1.addWidget(self.b1)
        self.vbox1.addWidget(self.b2)
        self.vbox1.addWidget(self.b3)
        self.vbox1.addWidget(self.b4)
        self.vbox1.addWidget(self.b5)
        self.vbox2.addWidget(self.b6)
        self.vbox2.addWidget(self.b7)
        self.vbox2.addWidget(self.b8)
        self.vbox2.addWidget(self.b9)
        self.vbox2.addWidget(self.b10)

        self.hbox.addLayout(self.vbox1)
        self.hbox.addLayout(self.vbox2)

        self.setLayout(self.hbox)

    def on_b2_click(self):
        self.w = CreateCorporation()
        self.w.show()
        self.close()
















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
        self.b3 = QPushButton("Return to Home")
        self.b1.clicked.connect(self.on_b1_click)
        self.b2.clicked.connect(self.on_b2_click)
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.line1.setText("")
        self.line2.setText("")
        self.line3.setText("")
        self.line4.setText("")
        self.setWindowTitle("Create Corporation")

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
            self.setWindowTitle("Invalid Inputs/Blank Inputs")
    def on_b3_click(self):
        self.w = AdminHome()
        self.w.show()
        self.close()

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
            
            
            
            
            
            
class StartEmployeeRole (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Start Employee Role")
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
        self.hbox11 = QHBoxLayout()
        self.hbox12 = QHBoxLayout()
        self.hbox13 = QHBoxLayout()
        self.hbox14 = QHBoxLayout()
        self.prompt1 = QLabel("Employee ID")
        self.line1 = QLineEdit()
        self.prompt2 = QLabel("Tax ID")
        self.line2 = QLineEdit()
        self.prompt3 = QLabel("First Name")
        self.line3 = QLineEdit()
        self.prompt4 = QLabel("Last Name")
        self.line4 = QLineEdit()
        self.prompt5 = QLabel("Birthdate")
        self.line5 = QLineEdit()
        self.prompt6 = QLabel("Street Address")
        self.line6 = QLineEdit()
        self.prompt7 = QLabel("City")
        self.line7 = QLineEdit()
        self.prompt8 = QLabel("Zip Code")
        self.line8 = QLineEdit()
        self.prompt9 = QLabel("Date Joined")
        self.line9 = QLineEdit()
        self.prompt10 = QLabel("Salary")
        self.line10 = QLineEdit()
        self.prompt11 = QLabel("Payments")
        self.line11 = QLineEdit()
        self.prompt12 = QLabel("Earned")
        self.line12 = QLineEdit()
        self.prompt13 = QLabel("Password")
        self.line13 = QLineEdit()

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
        self.hbox10.addWidget(self.prompt10)
        self.hbox10.addWidget(self.line10)
        self.hbox11.addWidget(self.prompt11)
        self.hbox11.addWidget(self.line11)
        self.hbox12.addWidget(self.prompt12)
        self.hbox12.addWidget(self.line12)
        self.hbox13.addWidget(self.prompt13)
        self.hbox13.addWidget(self.line13)
        self.hbox14.addWidget(self.b1)
        self.hbox14.addWidget(self.b2)


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
        self.vbox.addLayout(self.hbox11)
        self.vbox.addLayout(self.hbox12)
        self.vbox.addLayout(self.hbox13)
        self.vbox.addLayout(self.hbox14)
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
        self.line10.setText("")
        self.line11.setText("")
        self.line12.setText("")
        self.line13.setText("")

    def on_b2_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        startemprole = mydb.cursor()
        try:
            args = [self.line1.text(),self.line2.text(), self.line3.text(), self.line4.text(), self.line5.text(), self.line6.text(), self.line7.text(), self.line8.text(), self.line9.text(), self.line10.text(), int(self.line11.text()), int(self.line12.text()), self.line13.text()]
            startemprole.callproc("start_employee_role", args)
            mydb.commit()
            startemprole.close()
            mydb.close()
        except:
            print("oops")






class StartCustomerRole (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Start Customer Role")
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
        self.hbox11 = QHBoxLayout()
        self.prompt1 = QLabel("Customer ID")
        self.line1 = QLineEdit()
        self.prompt2 = QLabel("Tax ID")
        self.line2 = QLineEdit()
        self.prompt3 = QLabel("First Name")
        self.line3 = QLineEdit()
        self.prompt4 = QLabel("Last Name")
        self.line4 = QLineEdit()
        self.prompt5 = QLabel("Birthdate")
        self.line5 = QLineEdit()
        self.prompt6 = QLabel("Street Address")
        self.line6 = QLineEdit()
        self.prompt7 = QLabel("City")
        self.line7 = QLineEdit()
        self.prompt8 = QLabel("Zip Code")
        self.line8 = QLineEdit()
        self.prompt9 = QLabel("Date Joined")
        self.line9 = QLineEdit()
        self.prompt10 = QLabel("Password")
        self.line10 = QLineEdit()

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
        self.hbox10.addWidget(self.prompt10)
        self.hbox10.addWidget(self.line10)
        self.hbox11.addWidget(self.b1)
        self.hbox11.addWidget(self.b2)


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
        self.vbox.addLayout(self.hbox11)
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
        self.line10.setText("")

    def on_b2_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        startcustrole = mydb.cursor()
        try:
            args = [self.line1.text(),self.line2.text(), self.line3.text(), self.line4.text(), self.line5.text(), self.line6.text(), self.line7.text(), self.line8.text(), self.line9.text(), self.line10.text()]
            startcustrole.callproc("start_customer_role", args)
            mydb.commit()
            startcustrole.close()
            mydb.close()
        except:
            print("oops")






class StopEmployeeRole (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stop Employee Role")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.prompt1 = QLabel("Employee ID")
        self.line1 = QLineEdit()

        self.b1 = QPushButton("Cancel")
        self.b2 = QPushButton("Create")
        self.b1.clicked.connect(self.on_b1_click)
        self.b2.clicked.connect(self.on_b2_click)

        self.hbox1.addWidget(self.prompt1)
        self.hbox1.addWidget(self.line1)
        self.hbox2.addWidget(self.b1)
        self.hbox2.addWidget(self.b2)


        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.line1.setText("")

    def on_b2_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        stopemprole = mydb.cursor()
        try:
            args = [self.line1.text()]
            stopemprole.callproc("stop_employee_role", args)
            mydb.commit()
            stopemprole.close()
            mydb.close()
        except:
            print("oops")







class StopCustomerRole (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stop Customer Role")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.prompt1 = QLabel("Customer ID")
        self.line1 = QLineEdit()

        self.b1 = QPushButton("Cancel")
        self.b2 = QPushButton("Create")
        self.b1.clicked.connect(self.on_b1_click)
        self.b2.clicked.connect(self.on_b2_click)

        self.hbox1.addWidget(self.prompt1)
        self.hbox1.addWidget(self.line1)
        self.hbox2.addWidget(self.b1)
        self.hbox2.addWidget(self.b2)


        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.line1.setText("")

    def on_b2_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        stopcustrole = mydb.cursor()
        try:
            args = [self.line1.text()]
            stopcustrole.callproc("stop_customer_role", args)
            mydb.commit()
            stopcustrole.close()
            mydb.close()
        except:
            print("oops")

            





class HireWorker (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hire Worker")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.prompt1 = QLabel("Employee ID")
        self.line1 = QLineEdit()
        self.prompt2 = QLabel("Bank ID")
        self.line2 = QLineEdit()
        self.prompt3 = QLabel("Employee Salary")
        self.line3 = QLineEdit()

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
        self.hbox4.addWidget(self.b1)
        self.hbox4.addWidget(self.b2)


        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.line1.setText("")
        self.line2.setText("")
        self.line3.setText("")

    def on_b2_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        hirework = mydb.cursor()
        try:
            args = [self.line1.text(),self.line2.text(), int(self.line3.text())]
            hirework.callproc("hire_worker", args)
            mydb.commit()
            hirework.close()
            mydb.close()
        except:
            print("oops")





class ReplaceManager (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Replace Manager")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.prompt1 = QLabel("Manager ID")
        self.line1 = QLineEdit()
        self.prompt2 = QLabel("Bank ID")
        self.line2 = QLineEdit()
        self.prompt3 = QLabel("Manager Salary")
        self.line3 = QLineEdit()

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
        self.hbox4.addWidget(self.b1)
        self.hbox4.addWidget(self.b2)


        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.line1.setText("")
        self.line2.setText("")
        self.line3.setText("")

    def on_b2_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        replacemanager = mydb.cursor()
        try:
            args = [self.line1.text(),self.line2.text(), int(self.line3.text())]
            replacemanager.callproc("replace_manager", args)
            mydb.commit()
            replacemanager.close()
            mydb.close()
        except:
            print("oops")

            
            
            
class AddAccountAccess (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Account Access")
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
        self.hbox11 = QHBoxLayout()
        self.hbox12 = QHBoxLayout()
        self.hbox13 = QHBoxLayout()
        self.prompt1 = QLabel("Requester ID")
        self.line1 = QLineEdit()
        self.prompt2 = QLabel("Customer ID")
        self.line2 = QLineEdit()
        self.prompt3 = QLabel("Account Type")
        self.line3 = QComboBox()
        self.line3.addItems(["Savings", "Market", "Checking"])
        self.prompt4 = QLabel("Bank ID")
        self.line4 = QLineEdit()
        self.prompt5 = QLabel("Account ID")
        self.line5 = QLineEdit()
        self.prompt6 = QLabel("Balance")
        self.line6 = QLineEdit()
        self.prompt7 = QLabel("Interest Rate")
        self.line7 = QLineEdit()
        self.prompt8 = QLabel("Deposit Date")
        self.line8 = QLineEdit()
        self.prompt9 = QLabel("Minimum Balance")
        self.line9 = QLineEdit()
        self.prompt10 = QLabel("Current Number of Withdrawls")
        self.line10 = QLineEdit()
        self.prompt11 = QLabel("Maximum Number of Withdrawls")
        self.line11 = QLineEdit()
        self.prompt12 = QLabel("Current Date")
        self.line12 = QLineEdit()

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
        self.hbox10.addWidget(self.prompt10)
        self.hbox10.addWidget(self.line10)
        self.hbox11.addWidget(self.prompt11)
        self.hbox11.addWidget(self.line11)
        self.hbox12.addWidget(self.prompt12)
        self.hbox12.addWidget(self.line12)
        self.hbox13.addWidget(self.b1)
        self.hbox13.addWidget(self.b2)


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
        self.vbox.addLayout(self.hbox11)
        self.vbox.addLayout(self.hbox12)
        self.vbox.addLayout(self.hbox13)
        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.line1.setText("")
        self.line2.setText("")
        self.line4.setText("")
        self.line5.setText("")
        self.line6.setText("")
        self.line7.setText("")
        self.line8.setText("")
        self.line9.setText("")
        self.line10.setText("")
        self.line11.setText("")
        self.line12.setText("")

    def on_b2_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        addaccess = mydb.cursor()
        try:
            args = [self.line1.text(),self.line2.text(), self.line3.currentText(), self.line4.text(), self.line5.text(), int(self.line6.text()), int(self.line7.text()), self.line8.text(), int(self.line9.text()), int(self.line10.text()), int(self.line11.text()), self.line12.text()]
            addaccess.callproc("add_account_access", args)
            mydb.commit()
            addaccess.close()
            mydb.close()
        except:
            print("oops")





class RemoveAccountAccess (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remove Account Access")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.prompt1 = QLabel("Requester ID")
        self.line1 = QLineEdit()
        self.prompt2 = QLabel("Sharer ID")
        self.line2 = QLineEdit()
        self.prompt3 = QLabel("Bank ID")
        self.line3 = QLineEdit()
        self.prompt4 = QLabel("Account ID")
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
        removeaccess = mydb.cursor()
        try:
            args = [self.line1.text(),self.line2.text(), self.line3.text(), self.line4.text()]
            removeaccess.callproc("remove_account_access", args)
            mydb.commit()
            removeaccess.close()
            mydb.close()
        except:
            print("oops")





            
class CreateFee (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Fee")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.prompt1 = QLabel("Bank ID")
        self.line1 = QLineEdit()
        self.prompt2 = QLabel("Account ID")
        self.line2 = QLineEdit()
        self.prompt3 = QLabel("Fee Type")
        self.line3 = QComboBox()
        self.line3.addItems(["fee", "low balance", "overdraft", "administrative", "frequency", "withdrawl", "credit union", "other"])

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
        self.hbox4.addWidget(self.b1)
        self.hbox4.addWidget(self.b2)


        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.line1.setText("")
        self.line2.setText("")

    def on_b2_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        createfee = mydb.cursor()
        try:
            args = [self.line1.text(),self.line2.text(), self.line3.currentText()]
            createfee.callproc("create_fee", args)
            mydb.commit()
            createfee.close()
            mydb.close()
        except:
            print("oops")
            
            
            
            
class StartOverdraft (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Start Overdraft")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.hbox6 = QHBoxLayout()
        self.prompt1 = QLabel("Requester ID")
        self.line1 = QLineEdit()
        self.prompt2 = QLabel("Checking Bank ID")
        self.line2 = QLineEdit()
        self.prompt3 = QLabel("Checking Account ID")
        self.line3 = QLineEdit()
        self.prompt4 = QLabel("Savings Bank ID")
        self.line4 = QLineEdit()
        self.prompt5 = QLabel("Savings Account ID")
        self.line5 = QLineEdit()

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
        self.hbox6.addWidget(self.b1)
        self.hbox6.addWidget(self.b2)


        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addLayout(self.hbox6)
        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.line1.setText("")
        self.line2.setText("")
        self.line3.setText("")
        self.line4.setText("")
        self.line5.setText("")

    def on_b2_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        startoverdraft = mydb.cursor()
        try:
            args = [self.line1.text(),self.line2.text(), self.line3.text(), self.line4.text(), self.line5.text()]
            startoverdraft.callproc("start_overdraft", args)
            mydb.commit()
            startoverdraft.close()
            mydb.close()
        except:
            print("oops")





class StopOverdraft (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stop Overdraft")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.prompt1 = QLabel("Requester ID")
        self.line1 = QLineEdit()
        self.prompt2 = QLabel("Checking Bank ID")
        self.line2 = QLineEdit()
        self.prompt3 = QLabel("Checking Account ID")
        self.line3 = QLineEdit()

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
        self.hbox4.addWidget(self.b1)
        self.hbox4.addWidget(self.b2)


        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.line1.setText("")
        self.line2.setText("")
        self.line3.setText("")

    def on_b2_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        stopoverdraft = mydb.cursor()
        try:
            args = [self.line1.text(),self.line2.text(), self.line3.text()]
            stopoverdraft.callproc("stop_overdraft", args)
            mydb.commit()
            stopoverdraft.close()
            mydb.close()
        except:
            print("oops")





class AccountDeposit (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Account Deposit")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.hbox6 = QHBoxLayout()
        self.prompt1 = QLabel("Requester ID")
        self.line1 = QLineEdit()
        self.prompt2 = QLabel("Deposit Amount")
        self.line2 = QLineEdit()
        self.prompt3 = QLabel("Bank ID")
        self.line3 = QLineEdit()
        self.prompt4 = QLabel("Account ID")
        self.line4 = QLineEdit()
        self.prompt5 = QLabel("Deposit Date")
        self.line5 = QLineEdit()

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
        self.hbox6.addWidget(self.b1)
        self.hbox6.addWidget(self.b2)


        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addLayout(self.hbox6)
        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.line1.setText("")
        self.line2.setText("")
        self.line3.setText("")
        self.line4.setText("")
        self.line5.setText("")

    def on_b2_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        deposit = mydb.cursor()
        try:
            args = [self.line1.text(), int(self.line2.text()), self.line3.text(), self.line4.text(), self.line5.text()]
            deposit.callproc("account_deposit", args)
            mydb.commit()
            deposit.close()
            mydb.close()
        except:
            print("oops")





class AccountWithdrawal (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Account Withdrawal")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.hbox6 = QHBoxLayout()
        self.prompt1 = QLabel("Requester ID")
        self.line1 = QLineEdit()
        self.prompt2 = QLabel("Withdrawal Amount")
        self.line2 = QLineEdit()
        self.prompt3 = QLabel("Bank ID")
        self.line3 = QLineEdit()
        self.prompt4 = QLabel("Account ID")
        self.line4 = QLineEdit()
        self.prompt5 = QLabel("Withdrawal Date")
        self.line5 = QLineEdit()

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
        self.hbox6.addWidget(self.b1)
        self.hbox6.addWidget(self.b2)


        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addLayout(self.hbox6)
        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.line1.setText("")
        self.line2.setText("")
        self.line3.setText("")
        self.line4.setText("")
        self.line5.setText("")

    def on_b2_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        withdrawal = mydb.cursor()
        try:
            args = [self.line1.text(), int(self.line2.text()), self.line3.text(), self.line4.text(), self.line5.text()]
            withdrawal.callproc("account_withdrawal", args)
            mydb.commit()
            withdrawal.close()
            mydb.close()
        except:
            print("oops")





class AccountTransfer (QWidget):
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
        self.prompt1 = QLabel("Requester ID")
        self.line1 = QLineEdit()
        self.prompt2 = QLabel("Transfer Amount")
        self.line2 = QLineEdit()
        self.prompt3 = QLabel("Bank ID - Transfer From")
        self.line3 = QLineEdit()
        self.prompt4 = QLabel("Account ID - Transfer From")
        self.line4 = QLineEdit()
        self.prompt5 = QLabel("Bank ID - Transfer To")
        self.line5 = QLineEdit()
        self.prompt6 = QLabel("Account ID - Transfer To")
        self.line6 = QLineEdit()
        self.prompt7 = QLabel("Transfer Date")
        self.line7 = QLineEdit()

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
        self.hbox8.addWidget(self.b1)
        self.hbox8.addWidget(self.b2)


        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addLayout(self.hbox6)
        self.vbox.addLayout(self.hbox7)
        self.vbox.addLayout(self.hbox8)
        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.line1.setText("")
        self.line2.setText("")
        self.line3.setText("")
        self.line4.setText("")
        self.line5.setText("")
        self.line6.setText("")
        self.line7.setText("")

    def on_b2_click(self):
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        transfer = mydb.cursor()
        try:
            args = [self.line1.text(), int(self.line2.text()), self.line3.text(), self.line4.text(), self.line5.text(), self.line6.text(), self.line7.text()]
            transfer.callproc("account_transfer", args)
            mydb.commit()
            transfer.close()
            mydb.close()
        except:
            print("oops")
            
 class ViewStats (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("View Stats")
        self.b1 = QPushButton("Display Account Stats")
        self.b2 = QPushButton("Display Corporation Stats")
        self.b3 = QPushButton("Display Bank Stats")
        self.b4 = QPushButton("Display Customer Stats")
        self.b5 = QPushButton("Display Employee Stats")
        self.vbox = QVBoxLayout()

        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)
        self.vbox.addWidget(self.b3)
        self.vbox.addWidget(self.b4)
        self.vbox.addWidget(self.b5)

        self.setLayout(self.vbox)

        
        
 class DisplayAccountStats (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Display Account Stats")
        self.vbox = QVBoxLayout()
        self.table = QTableWidget()
        self.b1 = QPushButton("Return To View Stats")
        self.b1.clicked.connect(self.on_b1_click)
         
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Bank", "Account ID", "Account Balance ($)", "Number of\nOwners"])
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        cur = mydb.cursor()
        sqlquery = "select * from display_account_stats"
        tablerow = 0
        rows = cur.execute(sqlquery)
        data = cur.fetchall()
        self.table.setRowCount(len(data))
        for row in data:
            self.table.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.table.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
            self.table.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            self.table.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
            tablerow += 1

        cur.close()
        mydb.close()

        header = self.table.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)


        self.vbox.addWidget(self.table)
        self.vbox.addWidget(self.b1)
        self.setLayout(self.vbox)

    def on_b1_click(self):

        self.stats = ViewStats()
        self.stats.show()
        self.close()
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Login()
    main.show()
    sys.exit(app.exec_())
