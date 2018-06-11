import sys
import smtplib
import time
from PyQt4 import QtGui,QtCore
from email.mime.text import MIMEText
from email.header import Header



class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,300,600)                     #Automatic size=?
        self.setWindowTitle('Recados')
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        extractAction = QtGui.QAction('&Sair',self)
        extractAction.setStatusTip('Leave the app!')
        #extractAction.setShortcut('q')
        extractAction.triggered.connect(self.close_Application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        #Import name File
        self.my_dict = {}
        with open('email.txt')as f:
            for line in f:
                (key,val) = line.split(',')
                self.my_dict[key] = val
        print (self.my_dict)


        self.home()

        #Populate Combobox
        for k,v in self.my_dict.items():
            self.comboBox1.addItem(k)

#Our Window changing shit
    def home(self):
        #Exit Button
        btn1 = QtGui.QPushButton('Sair',self)
        btn1.clicked.connect(self.close_Application)
        #btn.resize(100,100)
        btn1.resize(btn1.sizeHint())
        btn1.move(200,500)

        #Send Button
        btn2 = QtGui.QPushButton('Enviar',self)
        btn2.clicked.connect(self.getTextContent)
        btn2.resize(btn2.sizeHint())
        btn2.move (20,500)

        #Clear Everything button
        btn3 = QtGui.QPushButton('Limpar tudo',self)
        btn3.clicked.connect(self.clearAll)
        btn3.resize(btn3.sizeHint())
        btn3.move(92,500)

        '''
        #ToolBar
        extractAction = QtGui.QAction(QtGui.QIcon('/Users/bentolima/Desktop/Logo.png'),'Merda de Programa',self)
        extractAction.triggered.connect(self.close_Application)
        self.toolBar = self.addToolBar('extraction')
        self.toolBar.addAction(extractAction)
        '''

        self.textBox2 = QtGui.QTextEdit(self)
        self.textBox2.setText('Visitante')
        self.textBox2.move (20,210)
        self.textBox2.resize(200,30)

        self.textBox3 = QtGui.QTextEdit(self)
        self.textBox3.move(20,250)
        self.textBox3.setText('Mensagem')
        self.textBox3.resize(250,200)


        #checkboxes
        self.checkBox = QtGui.QCheckBox('Telefonou',self)
        self.checkBox.move(10,10)

        self.checkBox1 = QtGui.QCheckBox('Veio Ca',self)
        self.checkBox1.move(10,40)

        self.checkBox2 = QtGui.QCheckBox('Deseja Falar',self)
        self.checkBox2.move(10,70)

        self.checkBox3 = QtGui.QCheckBox('deseja ve-lo',self)
        self.checkBox3.move(10,100)

        self.checkBox4 = QtGui.QCheckBox('Volta a telefonar',self)
        self.checkBox4.move(150,10)

        self.checkBox5 = QtGui.QCheckBox('Volta Ca',self)
        self.checkBox5.move(150,40)

        self.checkBox6 = QtGui.QCheckBox('Pede para telefonar',self)
        self.checkBox6.move(150,70)

        self.checkBox7 = QtGui.QCheckBox('Urgente',self)
        self.checkBox7.move(150,100)

        self.comboBox1 = QtGui.QComboBox(self)
        self.comboBox1.move(20,170)

        self.show()

    def close_Application(self):
        choice = QtGui.QMessageBox.question(self,'Warning!','Tem a certeza que pretende sair?',
        QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)

        if (choice == QtGui.QMessageBox.Yes):
            sys.exit()
        else:
            pass


    def clearAll(self):                     #bad code over here iteration
        self.textBox2.clear();
        self.textBox3.clear();

        self.checkBox.setChecked(False)
        self.checkBox1.setChecked(False)
        self.checkBox2.setChecked(False)
        self.checkBox3.setChecked(False)
        self.checkBox4.setChecked(False)
        self.checkBox5.setChecked(False)
        self.checkBox6.setChecked(False)
        self.checkBox7.setChecked(False)

    def getTextContent(self):
        #spaguetti code: can't iterate through them
        content = []
        status = []

        content.append(self.textBox2.toPlainText())
        content.append(self.textBox3.toPlainText())

        if self.checkBox.isChecked():
            status.append(self.checkBox.text())
        if self.checkBox1.isChecked():
            status.append(self.checkBox1.text())
        if self.checkBox2.isChecked():
            status.append(self.checkBox2.text())
        if self.checkBox3.isChecked():
            status.append(self.checkBox3.text())
        if self.checkBox4.isChecked():
            status.append(self.checkBox4.text())
        if self.checkBox5.isChecked():
            status.append(self.checkBox5.text())
        if self.checkBox5.isChecked():
            status.append(self.checkBox6.text())
        if self.checkBox6.isChecked():
            status.append(self.checkBox7.text())

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
        print header
        with open('testfile.txt','rb') as fp:
            msg = MIMEText(fp.read())
        smtpserver.sendmail(str(gmail_user), str(to),header+str(msg))
        print 'done!'
        smtpserver.close()
        self.clearAll()






def main():
    app = QtGui.QApplication(sys.argv)
    Gui = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
