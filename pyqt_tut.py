import sys
from PyQt4 import QtGui,QtCore
from mail import sendMail



class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,300,600)                     #Automatic size=?
        self.setWindowTitle('PyQt Tutorial')
        self.setWindowIcon(QtGui.QIcon('/Users/bentolima/Desktop/Logo.png'))

        extractAction = QtGui.QAction('&Exit',self)
        extractAction.setStatusTip('Leave the app!')
        extractAction.setShortcut('q')
        extractAction.triggered.connect(self.close_Application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        #Import name File
        dict = {}
        with open('nomes.txt')as f:
            for line in f:
                (key,val) = line.split(',')
                dict[key] = val
        print (dict)


        self.home()

        #Populate Combobox
        for k,v in dict.items():
            self.comboBox1.addItem(k)

#Our Window changing shit
    def home(self):
        #Exit Button
        btn1 = QtGui.QPushButton('Exit',self)
        btn1.clicked.connect(self.close_Application)
        #btn.resize(100,100)
        btn1.resize(btn1.sizeHint())
        btn1.move(200,500)

        #Send Button
        btn2 = QtGui.QPushButton('Enviar',self)
        btn2.clicked.connect(self.getTextContent)
        #btn2.clicked.connect(self.getBoxStatus)
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



        self.textBox1 =  QtGui.QTextEdit(self)
        self.textBox1.setText('Visitado')
        self.textBox1.move(20,170)
        self.textBox1.resize(200,30)
        '''

        self.textBox2 = QtGui.QTextEdit(self)
        self.textBox2.setText('Visitante')
        self.textBox2.move (20,210)
        self.textBox2.resize(200,30)

        self.textBox3 = QtGui.QTextEdit(self)
        self.textBox3.move(20,250)
        self.textBox3.setText('Mensagem')
        self.textBox3.resize(250,200)


        #text_show2 = QtGui.QTextEdit()
        #text_show2.setText('SHOW2STR')
        #text_show2.setReadOnly(True)
        #text_show2.resize(200,10)


        #self.text = QtGui.QTextEdit(self)
        #self.text.move(0,400)


        #checkboxes
        self.checkBox = QtGui.QCheckBox('Telefonou',self)
        self.checkBox.move(10,10)
        #self.checkBox.stateChanged.connect(self.printsomeshit) ##dunno yet

        self.checkBox1 = QtGui.QCheckBox('Veio Ca',self)
        self.checkBox1.move(10,40)
        #self.checkBox1.stateChanged.connect(self.printsomeshit) ##dunno yet

        self.checkBox2 = QtGui.QCheckBox('Deseja Falar',self)
        self.checkBox2.move(10,70)
        #self.checkBox2.stateChanged.connect(self.printsomeshit) ##dunno yet

        self.checkBox3 = QtGui.QCheckBox('deseja ve-lo',self)
        self.checkBox3.move(10,100)
        #self.checkBox3.stateChanged.connect(self.printsomeshit) ##dunno yet

        self.checkBox4 = QtGui.QCheckBox('Volta a telefonar',self)
        self.checkBox4.move(150,10)
        #self.checkBox4.stateChanged.connect(self.printsomeshit) ##dunno yet

        self.checkBox5 = QtGui.QCheckBox('Volta Ca',self)
        self.checkBox5.move(150,40)
        #self.checkBox5.stateChanged.connect(self.printsomeshit) ##dunno yet

        self.checkBox6 = QtGui.QCheckBox('Pede para telefonar',self)
        self.checkBox6.move(150,70)
        #self.checkBox6.stateChanged.connect(self.printsomeshit) ##dunno yet

        self.checkBox7 = QtGui.QCheckBox('Urgente',self)
        self.checkBox7.move(150,100)
        #self.checkBox7.stateChanged.connect(self.printsomeshit) ##dunno yet

        self.comboBox1 = QtGui.QComboBox(self)
        self.comboBox1.move(20,170)
        #populate ComboBox
        #for k,v in dict.items():
        #    comboBox1.addItem(k)


        self.show()

    def close_Application(self):
        #print('Good Bye!')
        #sys.exit()
        choice = QtGui.QMessageBox.question(self,'Warning!','Are you sure you want to leave?',
        QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)

        if (choice == QtGui.QMessageBox.Yes):
            sys.exit()
        else:
            pass

    def printsomeshit(self):
        print('to do later')

    def clearAll(self):                     #bad code over here iteration
        #self.textBox1.clear();
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

        #iterate through Qcheckboxes/QtextEdit identify the selected ones/messages
        #print selected and content to terminal
        '''
    def getBoxStatus(self):     #more spaguetti code
        status = []

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
            status.append(self.checkBox.text())
        if self.checkBox5.isChecked():
            status.append(self.checkBox.text())
        if self.checkBox6.isChecked():
            status.append(self.checkBox6.text())

        return status
        '''


    def getTextContent(self):
        #bad code here cant iterate through them
        content = []
        status = []

        #content.append(self.textBox1.toPlainText())
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
            status.append(self.checkBox.text())
        if self.checkBox5.isChecked():
            status.append(self.checkBox.text())
        if self.checkBox6.isChecked():
            status.append(self.checkBox6.text())

        #Store the message in a string and return it.

        print ('\n\n')
        print ('Recado da recepcao! \n\n')
        print('Ola '+self.comboBox1.currentText()+ '\n\nO Sr(a) '+content[0]+'\n\n')

        print '\n'.join([str(x) for x in status])

        print('\ne deixou o seguinte recado: \n\n'+content[1]+'.\n\n')

        #Save content to file
        file = open('testfile.txt','w')

        file.write('\n')
        file.write('Recado da recepcao! \n\n')
        file.write('Ola '+ self.comboBox1.currentText()+'\n\nO Sr(a) '+content[0]+'\n\n')
        file.write('\n'.join([str(x) for x in status]))
        file.write('\ne deixou o seguinte recado: \n\n'+content[1]+'.\n\n')
        file.close()

    #Load File to Dictionary
    '''
    def importMail():
        d = {}
        with open('nomes.txt')as f:
            for line in f:
                (key,val) = line.split(',')
                d[key] = val
        print (d)
    '''



def main():
    app = QtGui.QApplication(sys.argv)
    Gui = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
