from .logqtsqlui import Ui_MainWindow
#from logqtsqlui import Ui_MainWindow
import sys
from PyQt5.QtWidgets import (QMainWindow, QDialog, QApplication, QPushButton,
                             QLineEdit, QWidget, QMessageBox, QLabel, QTextEdit)
from PyQt5.QtCore import QRect

#get database import
from . import database
#import database

class Logqtsql(QMainWindow):
    def __init__(self):
        super(Logqtsql, self).__init__()
        self.setWindowOpacity(0.9)

        self.ui_objects = Ui_MainWindow()
        self.ui_objects.setupUi(self)

        #buttons
        self.ui_objects.btn_register.clicked.connect(self.register)
        self.ui_objects.btn_login.clicked.connect(self.login)

        #Qlines edit
        self.ui_objects.ln_password.setEchoMode(QLineEdit.Password)
        self.ui_objects.ln_user.returnPressed.connect(self.login)
        self.ui_objects.ln_password.returnPressed.connect(self.login)

    def register(self):
        self.ui_objects.btn_login.hide()
        self.ui_objects.btn_register.hide()
        self.ui_objects.ln_user.clear()
        self.ui_objects.ln_password.clear()
        
        self.ln_fname = QLineEdit(self)
        self.ln_fname.setGeometry(QRect(80, 440, 251, 41))
        self.ln_fname.setStyleSheet("color: rgb(255, 255, 255);")
        self.ln_fname.setPlaceholderText('Full Name')
        self.ln_fname.show()

        self.ln_email = QLineEdit(self)
        self.ln_email.setGeometry(QRect(80, 500, 251, 41))
        self.ln_email.setStyleSheet("color: rgb(255, 255, 255);")
        self.ln_email.setPlaceholderText('Email')
        self.ln_email.show()

        self.btn_getreg = QPushButton(self, text='Register')
        self.btn_getreg.setGeometry(QRect(100, 550, 211, 51))
        self.btn_getreg.show()
        self.btn_getreg.clicked.connect(self.__makeRegister) #run a private function

        self.btn_backreg = QPushButton(self, text='Back')
        self.btn_backreg.setGeometry(QRect(130, 610, 151, 31))
        self.btn_backreg.show()
        self.btn_backreg.clicked.connect(self.__backRegister) #run a private function

    def login(self):
        user = self.ui_objects.ln_user.text()
        password = self.ui_objects.ln_password.text()

        #database.cursor.execute("""
        #SELECT User,Password FROM registers
        #WHERE (User = ?) AND (Password = ?)
        #""", (user,password))
        
        #OR
        database.cursor.execute("""
        SELECT * FROM registers
        WHERE (User = ?) AND (Password = ?)
        """, (user,password))
        
        verifylogin = database.cursor.fetchone()
        if verifylogin is None:
            QMessageBox.critical(self, 'Login Fail', 'User or Password incorrect.', QMessageBox.Ok)
        else:
            QMessageBox.information(self, 'Login', 'Successfully login.', QMessageBox.Ok)
            Logqtsql.__cleanup(self)
            Logqtsql.__makeloginarea(self, userlogged=verifylogin[3])

    def search(self):
        text2search = self.logged_line_search.text() #get name or email to search into a db
        #select all in db
        database.cursor.execute("""
        SELECT * FROM registers
        WHERE (Email = ?) OR (Name = ?)
        """, (text2search,text2search,))        
        verify = database.cursor.fetchone() #get information
        colnames = [colname[0] for colname in database.cursor.description] #get column names

        if verify == None:
            self.logged_text_output.setText('User not found in database.')
        else:
            #formatting text to display
            text = ''
            for i, key in enumerate(colnames):
                text = ''.join(text+'\n{}: {}'.format(key, verify[i]))
                
            #display text
            self.logged_text_output.setText(text)

    def remove(self):
        text2remove = self.logged_line_search.text() #get name or email to remove from db

        #get information of client
        database.cursor.execute("""
        SELECT * FROM registers
        WHERE (Email = ?) OR (Name = ?)
        """, (text2remove,text2remove,))
        info = database.cursor.fetchone()
        colnames = [colname[0] for colname in database.cursor.description] #get column names

        if info == None:
            QMessageBox.information(self, 'Remove Client', 'Client not found in database.', QMessageBox.Ok)
        else:
            #formatting text to display
            text = ''
            for i, key in enumerate(colnames):
                text = ''.join(text+'\n{}: {}'.format(key, info[i]))
            
            state = QMessageBox.question(self, 'Remove Client',
                                'Are you want to remove the client?:{}'.format(text),
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if state == QMessageBox.Yes:
                database.cursor.execute("""
                DELETE FROM registers
                WHERE (Email = ?) OR (Name = ?)
                """, (text2remove, text2remove,))        
                database.connection.commit()
            else:
                pass

    def logout(self):
        state = QMessageBox.question(self, 'Logout', 'Are you sure you want logout?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if state == QMessageBox.Yes:
            #hide logged field
            self.logged_label.hide()
            self.logged_line_search.hide()
            self.logged_text_output.hide()
            self.logged_btn_search.hide()
            self.logged_btn_remove.hide()
            self.logged_btn_logout.hide()

            #show login field
            self.ui_objects.ln_user.show()
            self.ui_objects.ln_user.clear()
            self.ui_objects.ln_password.show()
            self.ui_objects.ln_password.clear()
            self.ui_objects.btn_login.show()
            self.ui_objects.btn_register.show()
        else:
            pass        

    def __makeloginarea(self, userlogged):
        #label
        self.logged_label = QLabel(self)
        self.logged_label.setText('Logged as {}'.format(userlogged))
        self.logged_label.setStyleSheet(style_labellogin)
        self.logged_label.setGeometry(QRect(20, 320, 381, 41))
        self.logged_label.show()

        #search by name in database
        self.logged_line_search = QLineEdit(self)
        self.logged_line_search.setGeometry(QRect(30, 370, 351, 41))
        self.logged_line_search.setStyleSheet("color: rgb(255, 255, 255);")
        self.logged_line_search.setPlaceholderText('Search by name or email.')
        self.logged_line_search.show()
        self.logged_line_search.returnPressed.connect(self.search)

        #Qtext to display results
        self.logged_text_output = QTextEdit(self)
        self.logged_text_output.setGeometry(QRect(30, 430, 351, 141))
        self.logged_text_output.setStyleSheet("color: rgb(255, 255, 255);")
        self.logged_text_output.setPlaceholderText('Output of search.....')
        self.logged_text_output.show()

        #Button to perform search
        self.logged_btn_search = QPushButton(self, text='Search')
        self.logged_btn_search.setGeometry(QRect(40, 580, 161, 41))
        self.logged_btn_search.show()
        self.logged_btn_search.clicked.connect(self.search)

        #Button to remove information of dataframe
        self.logged_btn_remove = QPushButton(self, text='Remove')
        self.logged_btn_remove.setGeometry(QRect(210, 580, 161, 41))
        self.logged_btn_remove.show()
        self.logged_btn_remove.clicked.connect(self.remove)

        #BUtton to logout
        self.logged_btn_logout = QPushButton(self, text='Logout')
        self.logged_btn_logout.setGeometry(QRect(260, 660, 131, 31))
        self.logged_btn_logout.show()
        self.logged_btn_logout.clicked.connect(self.logout)

        #return logged_line_search, logged_text_output, logged_btn_search, logged_btn_remove, logged_btn_logout

    def __makeRegister(self):
        #get texts
        user = self.ui_objects.ln_user.text()
        password = self.ui_objects.ln_password.text()
        fullname = self.ln_fname.text()
        email = self.ln_email.text()

        if user == "" or password == "" or fullname == "" or email == "":
            QMessageBox.critical(self, 'Register', 'Empty field, fill in all fields.', QMessageBox.Ok)
        else:
            #save information into a database
            database.cursor.execute("""
            INSERT INTO registers (User, Password, Name, Email) VALUES (?, ?, ?, ?)
            """, (user, password, fullname, email)
            )
            database.connection.commit() #salva as alterações no banco de dados

            QMessageBox.information(self, 'Register', 'Successful registration.', QMessageBox.Ok)
            Logqtsql.__backRegister(self)

    def __backRegister(self):
        self.ln_fname.hide()
        self.ln_email.hide()
        self.btn_getreg.hide()
        self.btn_backreg.hide()
        self.ui_objects.ln_user.clear()
        self.ui_objects.ln_password.clear()
        self.ui_objects.btn_login.show()
        self.ui_objects.btn_register.show()
    
    def __cleanup(self):
        self.ui_objects.ln_user.hide()
        self.ui_objects.ln_password.hide()
        self.ui_objects.btn_login.hide()
        self.ui_objects.btn_register.hide()


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Closing Window', 'Do you really want to close this application?\nThe database connection will be closed',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            database.connection.close()
            print('Database connection closed.')
        else:
            event.ignore()

style_labellogin = """
font: 75 18pt "Liberation Serif";
color: rgb(0, 255, 0);
"""

def runGUI():
    app = QApplication(sys.argv)
    gui = Logqtsql()
    gui.show()
    sys.exit(app.exec_())

"""if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Logqtsql()
    gui.show()
    sys.exit(app.exec_())"""
