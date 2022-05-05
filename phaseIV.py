import sys
import mysql.connector as s
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit,
    QHBoxLayout, QLabel, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView)






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

        admindata = cursor.fetchall()

        cursor.execute("select * from customer natural join person")

        customerdata = cursor.fetchall()

        cursor.execute("select manager, pwd from bank join person on perID = manager")

        managerdata = cursor.fetchall()
        if (self.line1.text(), self.line2.text()) in admindata:
            self.w = AdminHome()
            self.w.show()
            self.close()
        elif (self.line1.text(), self.line2.text()) in customerdata and (self.line1.text(), self.line2.text()) in managerdata:
            self.w = JointHome()
            self.w.show()
            self.close()
        elif (self.line1.text(), self.line2.text()) in customerdata:
            self.w = CustomerHome()
            self.w.show()
            self.close()

        elif (self.line1.text(), self.line2.text()) in managerdata:
            self.w = ManagerHome()
            self.w.show()
            self.close()
        else:
            self.setWindowTitle("Invald Login!")
            self.line1.setText("")
            self.line2.setText("")


class JointHome (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Customer or Manager?")

        self.vbox = QVBoxLayout()
        self.b1 = QPushButton("Manager")
        self.b2 = QPushButton("Customer")

        self.b1.clicked.connect(self.on_b1_click)
        self.b2.clicked.connect(self.on_b2_click)

        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)

        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.w = ManagerHome()
        self.w.show()
        self.close()

    def on_b2_click(self):
        self.w = CustomerHome()
        self.w.show()
        self.close()



class AdminHome (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Admin Menu")
        self.hbox = QHBoxLayout()
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()

        self.b1 = QPushButton("View Stats")
        self.b1.clicked.connect(self.on_b1_click)
        self.b2 = QPushButton("Create Corporation")
        self.b2.clicked.connect(self.on_b2_click)
        self.b3 = QPushButton("Create Fee")
        self.b3.clicked.connect(self.on_b3_click)
        self.b4 = QPushButton("Manage Users")
        self.b4.clicked.connect(self.on_b4_click)
        self.b5 = QPushButton("Manage Overdraft")
        self.b5.clicked.connect(self.on_b5_click)
        self.b6 = QPushButton("Hire Worker")
        self.b6.clicked.connect(self.on_b6_click)
        self.b7 = QPushButton("Pay Employees")
        self.b7.clicked.connect(self.on_b7_click)
        self.b8 = QPushButton("Replace Manager")
        self.b8.clicked.connect(self.on_b8_click)
        self.b9 = QPushButton("Manage Accounts")
        self.b9.clicked.connect(self.on_b9_click)
        self.b10 = QPushButton("Create Bank")
        self.b10.clicked.connect(self.on_b10_click)

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

    def on_b1_click(self):
        self.w = ViewStats()
        self.w.show()
        self.close()

    def on_b2_click(self):
        self.w = CreateCorporation()
        self.w.show()
        self.close()

    def on_b3_click(self):
        self.w = CreateFee()
        self.w.show()
        self.close()

    def on_b4_click(self):
        self.w = ManageUserPage()
        self.w.show()
        self.close()

    def on_b5_click(self):
        self.w = ManageOverdraft()
        self.w.show()
        self.close()

    def on_b6_click(self):
        self.w = HireWorkerA()
        self.w.show()
        self.close()

    def on_b7_click(self):
        self.w = PayEmployeesA()
        self.w.show()
        self.close()

    def on_b8_click(self):
        self.w = ReplaceManager()
        self.w.show()
        self.close()

    def on_b9_click(self):
        self.w = ManageAccountsA()
        self.w.show()
        self.close()

    def on_b10_click(self):
        self.w = CreateBank()
        self.w.show()
        self.close()


class ManagerHome (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manager Menu")

        self.vbox = QVBoxLayout()

        self.b1 = QPushButton("Pay Employee")
        self.b1.clicked.connect(self.on_b1_click)
        self.b2 = QPushButton("Hire Worker")
        self.b2.clicked.connect(self.on_b2_click)

        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)

        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.w = PayEmployeesM()
        self.w.show()
        self.close()


    def on_b2_click(self):
        self.w = HireWorkerM()
        self.w.show()
        self.close()





class CustomerHome (QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Customer Menu")

        self.vbox = QVBoxLayout()
        self.b1 = QPushButton("Manage Accounts")
        self.b1.clicked.connect(self.on_b1_click)
        self.b2 = QPushButton("Depost/Withdrawal")
        self.b2.clicked.connect(self.on_b2_click)
        self.b3 = QPushButton("Manage Overdraft")
        self.b3.clicked.connect(self.on_b3_click)
        self.b4 = QPushButton("Make Transfer")
        self.b4.clicked.connect(self.on_b4_click)



        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)
        self.vbox.addWidget(self.b3)
        self.vbox.addWidget(self.b4)

        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.w = ManageAccountsC()
        self.w.show()
        self.close()

    def on_b2_click(self):
        self.w = DepoWith()
        self.w.show()
        self.close()


    def on_b3_click(self):
        self.w = ManageOverdraftC()
        self.w.show()
        self.close()

    def on_b4_click(self):
        self.w = AccountTransfer()
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
            self.setWindowTitle("Success!")
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
        self.hbox11 = QHBoxLayout()
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
        self.prompt10 = QLabel("Employee")
        self.line10 = QLineEdit()

        self.b1 = QPushButton("Cancel")
        self.b2 = QPushButton("Create")
        self.b1.clicked.connect(self.on_b1_click)
        self.b2.clicked.connect(self.on_b2_click)
        self.b3 = QPushButton("Return to Home")
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
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
        createbank = mydb.cursor()
        self.setWindowTitle("Success")
        try:
            args = [self.line1.text(),self.line2.text(), self.line3.text(), self.line4.text(), self.line5.text(), self.line6.text(), int(self.line7.text()), self.line8.text(), self.line9.text(), self.line10.text()]
            createbank.callproc("create_bank", args)
            mydb.commit()
            createbank.close()
            mydb.close()
        except:
            self.setWindowTitle("Error Occurred!")


    def on_b3_click(self):
        self.w = AdminHome()
        self.w.show()
        self.close()




class ManageUserPage (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage Users")

        self.vbox = QVBoxLayout()

        self.b1 = QPushButton("Create Employee Role")
        self.b2 = QPushButton("Create Customer Role")
        self.b3 = QPushButton("Stop Employee Role")
        self.b4 = QPushButton("Stop Customer Role")
        self.b5 = QPushButton("Return to Home")

        self.b1.clicked.connect(self.on_b1_click)
        self.b2.clicked.connect(self.on_b2_click)
        self.b3.clicked.connect(self.on_b3_click)
        self.b4.clicked.connect(self.on_b4_click)
        self.b5.clicked.connect(self.on_b5_click)

        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)
        self.vbox.addWidget(self.b3)
        self.vbox.addWidget(self.b4)
        self.vbox.addWidget(self.b5)

        self.setLayout(self.vbox)
    def on_b1_click(self):
        self.w = StartEmployeeRole()
        self.w.show()
        self.close()

    def on_b2_click(self):
        self.w = StartCustomerRole()
        self.w.show()
        self.close()

    def on_b3_click(self):
        self.w = StopEmployeeRole()
        self.w.show()
        self.close()

    def on_b4_click(self):
        self.w = StopCustomerRole()
        self.w.show()
        self.close()

    def on_b5_click(self):
        self.w = AdminHome()
        self.w.show()
        self.close()







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
        self.b3 = QPushButton("Return to Manage Users")
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success")
        except:
            self.setWindowTitle("Error Occurred!")

    def on_b3_click(self):
        self.w = ManageUserPage()
        self.w.show()
        self.close()




class StartCustomerRole (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Start Customer Role")
        self.vbox = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox11 = QHBoxLayout()
        self.prompt1 = QLabel("Customer ID")
        self.line1 = QLineEdit()
        

        self.b1 = QPushButton("Cancel")
        self.b2 = QPushButton("Create")
        self.b1.clicked.connect(self.on_b1_click)
        self.b2.clicked.connect(self.on_b2_click)
        self.b3 = QPushButton("Return to Manage Users")
        self.b3.clicked.connect(self.on_b3_click)

        self.hbox1.addWidget(self.prompt1)
        self.hbox1.addWidget(self.line1)
       
        self.hbox11.addWidget(self.b1)
        self.hbox11.addWidget(self.b2)


        self.vbox.addLayout(self.hbox1)
       
        self.vbox.addWidget(self.b3)
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
            startcustrole.callproc("create_cust_role", args)
            mydb.commit()
            startcustrole.close()
            mydb.close()
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")

    def on_b3_click(self):
        self.w = ManageUserPage()
        self.w.show()
        self.close()




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
        self.b3 = QPushButton("Return to Manage Users")
        self.b3.clicked.connect(self.on_b3_click)

        self.hbox1.addWidget(self.prompt1)
        self.hbox1.addWidget(self.line1)
        self.hbox2.addWidget(self.b1)
        self.hbox2.addWidget(self.b2)


        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")

    def on_b3_click(self):
        self.w = ManageUserPage()
        self.w.show()
        self.close()






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
        self.b3 = QPushButton("Return to Manage Users")
        self.b3.clicked.connect(self.on_b3_click)

        self.hbox1.addWidget(self.prompt1)
        self.hbox1.addWidget(self.line1)
        self.hbox2.addWidget(self.b1)
        self.hbox2.addWidget(self.b2)


        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")


    def on_b3_click(self):
        self.w = ManageUserPage()
        self.w.show()
        self.close()




class HireWorkerA (QWidget):
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
        self.b3 = QPushButton("Return to Home")
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")

    def on_b3_click(self):
        self.w = AdminHome()
        self.w.show()
        self.close()

class HireWorkerM (QWidget):
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
        self.b3 = QPushButton("Return to Home")
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")

    def on_b3_click(self):
        self.w = ManagerHome()
        self.w.show()
        self.close()

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
        self.b3 = QPushButton("Return to Home")
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")



    def on_b3_click(self):
        self.w = AdminHome()
        self.w.show()
        self.close()





class ManageAccountsA (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manage Accounts")

        self.vbox = QVBoxLayout()
        self.b1 = QPushButton("Add Account Access")
        self.b2 = QPushButton("Remove Account Access")
        self.b3 = QPushButton("Return to Home")

        self.b1.clicked.connect(self.on_b1_click)
        self.b2.clicked.connect(self.on_b2_click)
        self.b3.clicked.connect(self.on_b3_click)

        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)
        self.vbox.addWidget(self.b3)

        self.setLayout(self.vbox)


    def on_b1_click(self):
        self.w = AddAccountAccessA()
        self.w.show()
        self.close()

    def on_b2_click(self):
        self.w = RemoveAccountAccessA()
        self.w.show()
        self.close()

    def on_b3_click(self):
        self.w = AdminHome()
        self.w.show()
        self.close()






class AddAccountAccessA (QWidget):
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
        self.b3 = QPushButton("Return to Manage Accounts")
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")

    def on_b3_click(self):
        self.w = ManageAccountsA()
        self.w.show()
        self.close()





class RemoveAccountAccessA (QWidget):
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
        self.b3 = QPushButton("Return to Manage Accounts")
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")


    def on_b3_click(self):
        self.w = ManageAccountsA()
        self.w.show()
        self.close()

class ManageAccountsC (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manage Accounts")

        self.vbox = QVBoxLayout()
        self.b1 = QPushButton("Add Account Access")
        self.b2 = QPushButton("Remove Account Access")
        self.b3 = QPushButton("Return to Home")

        self.b1.clicked.connect(self.on_b1_click)
        self.b2.clicked.connect(self.on_b2_click)
        self.b3.clicked.connect(self.on_b3_click)

        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)
        self.vbox.addWidget(self.b3)

        self.setLayout(self.vbox)


    def on_b1_click(self):
        self.w = AddAccountAccessC()
        self.w.show()
        self.close()

    def on_b2_click(self):
        self.w = RemoveAccountAccessC()
        self.w.show()
        self.close()

    def on_b3_click(self):
        self.w = CustomerHome()
        self.w.show()
        self.close()






class AddAccountAccessC (QWidget):
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
        self.b3 = QPushButton("Return to Manage Accounts")
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")

    def on_b3_click(self):
        self.w = ManageAccountsC()
        self.w.show()
        self.close()





class RemoveAccountAccessC (QWidget):
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
        self.b3 = QPushButton("Return to Manage Accounts")
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")


    def on_b3_click(self):
        self.w = ManageAccountsC()
        self.w.show()
        self.close()






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
        self.b3 = QPushButton("Return to Home")
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")


    def on_b3_click(self):
        self.w = AdminHome()
        self.w.show()
        self.close()







class ManageOverdraftA (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manage Overdraft")

        self.vbox = QVBoxLayout()

        self.b1 = QPushButton("Start Overdraft")
        self.b2 = QPushButton("Stop Overdraft")
        self.b3 = QPushButton("Return to Home")

        self.b1.clicked.connect(self.on_b1_click)
        self.b2.clicked.connect(self.on_b2_click)
        self.b3.clicked.connect(self.on_b3_click)

        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)
        self.vbox.addWidget(self.b3)

        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.w = StartOverdraftA()
        self.w.show()
        self.close()

    def on_b2_click(self):
        self.w = StopOverdraftA()
        self.w.show()
        self.close()

    def on_b3_click(self):
        self.w = AdminHome()
        self.w.show()
        self.close()









class StartOverdraftA (QWidget):
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
        self.b3 = QPushButton("Return to Manage Overdraft")
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")

    def on_b3_click(self):
        self.w = ManageOverdraftA()
        self.w.show()
        self.close()



class StopOverdraftA (QWidget):
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
        self.b3 = QPushButton("Return to Manage Overdraft")
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")

    def on_b3_click(self):
        self.w = ManageOverdraftA()
        self.w.show()
        self.close()


class ManageOverdraftC (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manage Overdraft")

        self.vbox = QVBoxLayout()

        self.b1 = QPushButton("Start Overdraft")
        self.b2 = QPushButton("Stop Overdraft")
        self.b3 = QPushButton("Return to Home")

        self.b1.clicked.connect(self.on_b1_click)
        self.b2.clicked.connect(self.on_b2_click)
        self.b3.clicked.connect(self.on_b3_click)

        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)
        self.vbox.addWidget(self.b3)

        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.w = StartOverdraftC()
        self.w.show()
        self.close()

    def on_b2_click(self):
        self.w = StopOverdraftC()
        self.w.show()
        self.close()

    def on_b3_click(self):
        self.w = CustomerHome()
        self.w.show()
        self.close()









class StartOverdraftC (QWidget):
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
        self.b3 = QPushButton("Return to Manage Overdraft")
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")

    def on_b3_click(self):
        self.w = ManageOverdraftC()
        self.w.show()
        self.close()



class StopOverdraftC (QWidget):
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
        self.b3 = QPushButton("Return to Manage Overdraft")
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")

    def on_b3_click(self):
        self.w = ManageOverdraftC()
        self.w.show()
        self.close()


class DepoWith (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Deposit or Withdraw?")

        self.vbox = QVBoxLayout()
        self.b1 = QPushButton("Deposit")
        self.b2 = QPushButton("Withdraw")
        self.b3 = QPushButton("Return to Home")

        self.b1.clicked.connect(self.on_b1_click)
        self.b2.clicked.connect(self.on_b2_click)
        self.b3.clicked.connect(self.on_b3_click)

        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)
        self.vbox.addWidget(self.b3)

        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.w = AccountDeposit()
        self.w.show()
        self.close()

    def on_b2_click(self):
        self.w = AccountWithdrawal()
        self.w.show()
        self.close()

    def on_b3_click(self):
        self.w = CustomerHome()
        self.w.show()
        self.close()





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
        self.b3 = QPushButton("Return to selection")
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")

    def on_b3_click(self):
        self.w = DepoWith()
        self.w.show()
        self.close()





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
        self.b3 = QPushButton("Return to selection")
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")

    def on_b3_click(self):
        self.w = DepoWith()
        self.w.show()
        self.close()





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
        self.b3 = QPushButton("Return to Home")
        self.b3.clicked.connect(self.on_b3_click)

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
        self.vbox.addWidget(self.b3)
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
            self.setWindowTitle("Success!")
        except:
            self.setWindowTitle("Error Occurred!")

    def on_b3_click(self):
        self.w = CustomerHome()
        self.w.show()
        self.close()




class ViewStats (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("View Stats")
        self.b1 = QPushButton("Display Account Stats")
        self.b2 = QPushButton("Display Corporation Stats")
        self.b3 = QPushButton("Display Bank Stats")
        self.b4 = QPushButton("Display Customer Stats")
        self.b5 = QPushButton("Display Employee Stats")
        self.b6 = QPushButton("Return To Admin Home")

        self.b1.clicked.connect(self.on_b1_click)
        self.b2.clicked.connect(self.on_b2_click)
        self.b3.clicked.connect(self.on_b3_click)
        self.b4.clicked.connect(self.on_b4_click)
        self.b5.clicked.connect(self.on_b5_click)
        self.b6.clicked.connect(self.on_b6_click)

        self.vbox = QVBoxLayout()

        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)
        self.vbox.addWidget(self.b3)
        self.vbox.addWidget(self.b4)
        self.vbox.addWidget(self.b5)
        self.vbox.addWidget(self.b6)

        self.setLayout(self.vbox)

    def on_b1_click(self):
        self.accountStats = DisplayAccountStats()
        self.accountStats.show()
        self.close()

    def on_b2_click(self):
        self.corpStats = DisplayCorporationStats()
        self.corpStats.show()
        self.close()

    def on_b3_click(self):
        self.bankStats = DisplayBankStats()
        self.bankStats.show()
        self.close()

    def on_b4_click(self):
        self.custStats = DisplayCustomerStats()
        self.custStats.show()
        self.close()

    def on_b5_click(self):
        self.empStats = DisplayEmployeeStats()
        self.empStats.show()
        self.close()

    def on_b6_click(self):
        self.adHome = AdminHome()
        self.adHome.show()
        self.close()



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


class DisplayCorporationStats (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Display Corporation Stats")
        self.vbox = QVBoxLayout()
        self.table = QTableWidget()
        self.b1 = QPushButton("Return To View Stats")
        self.b1.clicked.connect(self.on_b1_click)

        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["Corporation ID", "Short Name", "Formal Name", "Number of\nBanks", "Corporation\nAssets ($)", "Total Assets ($)"])
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        cur = mydb.cursor()
        sqlquery = "select * from display_corporation_stats"
        tablerow = 0
        rows = cur.execute(sqlquery)
        data = cur.fetchall()
        self.table.setRowCount(len(data))
        for row in data:
            self.table.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.table.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
            self.table.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            self.table.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
            self.table.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
            self.table.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
            tablerow += 1

        cur.close()
        mydb.close()

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)


        self.vbox.addWidget(self.table)
        self.vbox.addWidget(self.b1)
        self.setLayout(self.vbox)

    def on_b1_click(self):

        self.stats = ViewStats()
        self.stats.show()
        self.close()


class DisplayBankStats (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Display Bank Stats")
        self.vbox = QVBoxLayout()
        self.table = QTableWidget()
        self.b1 = QPushButton("Return To View Stats")
        self.b1.clicked.connect(self.on_b1_click)

        self.table.setColumnCount(10)
        self.table.setHorizontalHeaderLabels(["Bank ID", "Corporation Name", "Bank Name", "Street", "State", "Zip", "Number\nof\nAccounts", "Bank Assets ($)", "Total Assets ($)"])
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        cur = mydb.cursor()
        sqlquery = "select * from display_bank_stats"
        tablerow = 0
        rows = cur.execute(sqlquery)
        data = cur.fetchall()
        self.table.setRowCount(len(data))
        for row in data:
            self.table.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.table.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
            self.table.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            self.table.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
            self.table.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
            self.table.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
            self.table.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))
            self.table.setItem(tablerow, 7, QTableWidgetItem(str(row[7])))
            self.table.setItem(tablerow, 8, QTableWidgetItem(str(row[8])))
            self.table.setItem(tablerow, 9, QTableWidgetItem(str(row[9])))
            tablerow += 1

        cur.close()
        mydb.close()

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(8, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(9, QHeaderView.ResizeToContents)


        self.vbox.addWidget(self.table)
        self.vbox.addWidget(self.b1)
        self.setLayout(self.vbox)

    def on_b1_click(self):

        self.stats = ViewStats()
        self.stats.show()
        self.close()


class DisplayCustomerStats (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Display Customer Stats")
        self.vbox = QVBoxLayout()
        self.table = QTableWidget()
        self.b1 = QPushButton("Return To View Stats")
        self.b1.clicked.connect(self.on_b1_click)

        self.table.setColumnCount(11)
        self.table.setHorizontalHeaderLabels(["Customer ID", "Tax ID", "Full Name", "DOB", "Date Joined", "Street", "City", "State", "Zip Code", "Number of\nAccounts", "Assets"])
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        cur = mydb.cursor()
        sqlquery = "select * from display_customer_stats"
        tablerow = 0
        rows = cur.execute(sqlquery)
        data = cur.fetchall()
        self.table.setRowCount(len(data))
        for row in data:
            self.table.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.table.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
            self.table.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            self.table.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
            self.table.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
            self.table.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
            self.table.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))
            self.table.setItem(tablerow, 7, QTableWidgetItem(str(row[7])))
            self.table.setItem(tablerow, 8, QTableWidgetItem(str(row[8])))
            self.table.setItem(tablerow, 9, QTableWidgetItem(str(row[9])))
            self.table.setItem(tablerow, 10, QTableWidgetItem(str(row[10])))
            tablerow += 1

        cur.close()
        mydb.close()

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(8, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(9, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(10, QHeaderView.ResizeToContents)


        self.vbox.addWidget(self.table)
        self.vbox.addWidget(self.b1)
        self.setLayout(self.vbox)

    def on_b1_click(self):

        self.stats = ViewStats()
        self.stats.show()
        self.close()





class DisplayEmployeeStats (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Display Employee Stats")
        self.vbox = QVBoxLayout()
        self.table = QTableWidget()
        self.b1 = QPushButton("Return To View Stats")
        self.b1.clicked.connect(self.on_b1_click)

        self.table.setColumnCount(11)
        self.table.setHorizontalHeaderLabels(["Employee ID", "Tax ID", "Full Name", "DOB", "Date Joined", "Street", "City", "State", "Zip Code", "Number of Banks\nEmployed At", "Assets"])
        mydb = s.connect(
            host = 'localhost',
            database = 'bank_management',
            username = 'root',
            password = 'barnsley')
        cur = mydb.cursor()
        sqlquery = "select * from display_employee_stats"
        tablerow = 0
        rows = cur.execute(sqlquery)
        data = cur.fetchall()
        self.table.setRowCount(len(data))
        for row in data:
            self.table.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.table.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
            self.table.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            self.table.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
            self.table.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
            self.table.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
            self.table.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))
            self.table.setItem(tablerow, 7, QTableWidgetItem(str(row[7])))
            self.table.setItem(tablerow, 8, QTableWidgetItem(str(row[8])))
            self.table.setItem(tablerow, 9, QTableWidgetItem(str(row[9])))
            self.table.setItem(tablerow, 10, QTableWidgetItem(str(row[10])))
            tablerow += 1

        cur.close()
        mydb.close()

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(8, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(9, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(10, QHeaderView.ResizeToContents)


        self.vbox.addWidget(self.table)
        self.vbox.addWidget(self.b1)
        self.setLayout(self.vbox)

    def on_b1_click(self):

        self.stats = ViewStats()
        self.stats.show()
        self.close()




class PayEmployeesA (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pay Employees")

        self.vbox = QVBoxLayout()

        self.b1 = QPushButton("Pay Now")
        self.b1.clicked.connect(self.on_b1_click)
        self.b2 = QPushButton("Return Home")
        self.b2.clicked.connect(self.on_b2_click)

        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)
        self.setLayout(self.vbox)




    def on_b1_click(self):
        mydb = s.connect(
        host = 'localhost',
        database = 'bank_management',
        username = 'root',
        password = 'barnsley')
        pay = mydb.cursor()
        try:
            pay.callproc("pay_employees")
            mydb.commit()
            pay.close()
            mydb.close()
        except:
            self.setWindowTitle("Error Occurred!")


    def on_b2_click(self):
        self.w = AdminHome()
        self.w.show()
        self.close()

class PayEmployeesM (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pay Employees")

        self.vbox = QVBoxLayout()

        self.b1 = QPushButton("Pay Now")
        self.b1.clicked.connect(self.on_b1_click)
        self.b2 = QPushButton("Return Home")
        self.b2.clicked.connect(self.on_b2_click)

        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b2)
        self.setLayout(self.vbox)


    def on_b1_click(self):
        mydb = s.connect(
        host = 'localhost',
        database = 'bank_management',
        username = 'root',
        password = 'barnsley')
        pay = mydb.cursor()
        try:
            pay.callproc("pay_employees")
            mydb.commit()
            pay.close()
            mydb.close()
        except:
            self.setWindowTitle("Error Occurred!")

    def on_b2_click(self):
        self.w = ManagerHome()
        self.w.show()
        self.close()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Login()
    main.show()
    sys.exit(app.exec_())



