# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
import smtplib
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,QLineEdit,QTextEdit,QAction,QCheckBox,QWidget,QComboBox,QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui
from email.mime.text import MIMEText
from email.header import Header

class Ui_Form(QMainWindow):

    def __init__(self):
        super(Ui_Form,self).__init__()
        #self.setWindowIcon(QtGui.QIcon('Logo.png'))
        self.my_dict = {}
        with open('email.txt')as f:
            for line in f:
                ((key,val)) = line.split(',')
                self.my_dict[key] = val
        #print (self.my_dict)


        self.setupUi(Form)

        #Populate Combobox
        for k,v in self.my_dict.items():
            self.comboBox1.addItem(k)


    def setupUi(self,Form):

        Form.setObjectName("Form")
        Form.resize(386, 413)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")


        self.comboBox1 = QtWidgets.QComboBox(Form)
        self.comboBox1.setObjectName("comboBox1")
        self.verticalLayout.addWidget(self.comboBox1)


        self.textBox2 = QtWidgets.QLineEdit(Form)
        self.textBox2.setObjectName("textBox2")
        self.textBox2.setPlaceholderText('Visitante')


        self.verticalLayout.addWidget(self.textBox2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        self.checkBox_0 = QtWidgets.QCheckBox(Form)
        self.checkBox_0.setObjectName("checkBox_0")
        self.verticalLayout_2.addWidget(self.checkBox_0)


        self.checkBox_1 = QtWidgets.QCheckBox(Form)
        self.checkBox_1.setObjectName("checkBox_1")
        self.verticalLayout_2.addWidget(self.checkBox_1)


        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)


        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")


        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_4.addWidget(self.checkBox_4)


        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_4.addWidget(self.checkBox_5)


        self.checkBox_6 = QtWidgets.QCheckBox(Form)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_4.addWidget(self.checkBox_6)


        self.checkBox_7 = QtWidgets.QCheckBox(Form)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_4.addWidget(self.checkBox_7)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 2, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBox3 = QtWidgets.QTextEdit(Form)
        self.textBox3.setObjectName("textBox3")
        self.horizontalLayout.addWidget(self.textBox3)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn2 = QtWidgets.QPushButton(Form)
        self.btn2.setObjectName("btn2")
        self.verticalLayout_3.addWidget(self.btn2)
        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn3 = QtWidgets.QPushButton(Form)
        self.btn3.setObjectName("btn3")
        self.verticalLayout_5.addWidget(self.btn3)
        self.gridLayout.addLayout(self.verticalLayout_5, 3, 1, 1, 2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn1 = QtWidgets.QPushButton(Form)
        self.btn1.setObjectName("btn1")
        self.verticalLayout_6.addWidget(self.btn1)
        self.gridLayout.addLayout(self.verticalLayout_6, 3, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #self.show()
        #My code Goes here

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowIcon(QtGui.QIcon('logo.png'))
        Form.setWindowTitle(_translate("Form", "Recados"))
        self.checkBox_0.setText(_translate("Form", "Telefonou"))
        self.checkBox_1.setText(_translate("Form", "Veio ca"))
        self.checkBox_2.setText(_translate("Form", "Deseja Falar"))
        self.checkBox_3.setText(_translate("Form", "Deseja Ve-lo"))
        self.checkBox_4.setText(_translate("Form", "Volta a Telefonar"))
        self.checkBox_5.setText(_translate("Form", "Volta Ca"))
        self.checkBox_6.setText(_translate("Form", "Pede para telefonar"))
        self.checkBox_7.setText(_translate("Form", "Urgente"))
        self.btn2.setText(_translate("Form", "Enviar"))
        self.btn2.clicked.connect(self.getTextContent)
        self.btn3.setText(_translate("Form", "Limpar tudo"))
        self.btn3.clicked.connect(self.clearAll)
        self.btn1.setText(_translate("Form", "Sair"))
        self.btn1.clicked.connect(self.close_Application)

    def clearAll(self):                     #bad code over here iteration
        self.textBox2.clear();
        self.textBox3.clear();

        self.checkBox_0.setChecked(False)
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)

    def close_Application(self):
        choice = QMessageBox.question(self,'Warning!',"Tem a certeza que pretende sair?", QMessageBox.Yes|QMessageBox.No,QMessageBox.No)

        if (choice == QMessageBox.Yes):
            sys.exit()
        else:
            pass

    def getTextContent(self):
        #spaguetti code: can't iterate through them
        content = []
        status = []

        content.append(self.textBox2.text())
        content.append(self.textBox3.toPlainText())

        if self.checkBox_0.isChecked():
            status.append(self.checkBox_0.text())
        if self.checkBox_1.isChecked():
            status.append(self.checkBox_1.text())
        if self.checkBox_2.isChecked():
            status.append(self.checkBox_2.text())
        if self.checkBox_3.isChecked():
            status.append(self.checkBox_3.text())
        if self.checkBox_4.isChecked():
            status.append(self.checkBox_4.text())
        if self.checkBox_5.isChecked():
            status.append(self.checkBox_5.text())
        if self.checkBox_6.isChecked():
            status.append(self.checkBox_6.text())
        if self.checkBox_7.isChecked():
            status.append(self.checkBox_7.text())

        #Save content to file
        file = open('testfile.txt','w')
        log = open ('history.txt','a')

        file.write('\n')
        file.write('Recado da recepcao! \n\n')
        file.write('Ola '+ self.comboBox1.currentText()+'\n\nO Sr(a) '+content[0]+'\n\n')
        file.write('\n'.join([str(x) for x in status]))
        file.write('\ne deixou o seguinte recado: \n\n'+content[1]+'.\n\n')
        file.close()
        #Save Log of visits and messages

        log.write('\n')
        log.write('Log Recado da recepcao! \n\n')
        log.write('Ola '+ self.comboBox1.currentText()+'\n\nO Sr(a) '+content[0]+'\n\n')
        log.write('\n'.join([str(x) for x in status]))
        log.write('\ne deixou o seguinte recado: \n\n'+content[1]+'.\n\n')
        log.write(time.strftime('%H:%M:%S\n'))
        log.write(time.strftime('%x'))
        log.close()

        #Send mail
        targetMail = self.my_dict[str(self.comboBox1.currentText())]
        to = targetMail.strip()
        gmail_user = 'secretaria@bento.cv'
        gmail_pwd = 'bento123.'
        smtpserver = smtplib.SMTP("mail.bento.cv",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(gmail_user, gmail_pwd)
        header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: Recado Da Recepcao\n'
        print (header)
        with open('testfile.txt','rb') as fp:
            msg = MIMEText(fp.read())
        smtpserver.sendmail(str(gmail_user), str(to),header+str(msg))
        print ('done!')
        smtpserver.close()
        self.clearAll()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    #ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
