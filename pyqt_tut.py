import sys
from PyQt4 import QtGui,QtCore



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

        self.home()



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
        btn2.clicked.connect(self.printsomeshit)                 #code Send email
        btn2.resize(btn2.sizeHint())
        btn2.move (20,500)

        #Clear Everything button
        btn3 = QtGui.QPushButton('Limpar tudo',self)
        btn3.clicked.connect(self.printsomeshit)                 #code Clear All
        btn3.resize(btn3.sizeHint())
        btn3.move(92,500)

        '''
        #ToolBar
        extractAction = QtGui.QAction(QtGui.QIcon('/Users/bentolima/Desktop/Logo.png'),'Merda de Programa',self)
        extractAction.triggered.connect(self.close_Application)
        self.toolBar = self.addToolBar('extraction')
        self.toolBar.addAction(extractAction)

        '''

        textBox1 =  QtGui.QTextEdit(self)
        textBox1.setText('Visitado')
        textBox1.move(20,170)
        textBox1.resize(200,30)

        textBox2 = QtGui.QTextEdit(self)
        textBox2.setText('Visitante')
        textBox2.move (20,210)
        textBox2.resize(200,30)

        textBox3 = QtGui.QTextEdit(self)
        textBox3.move(20,250)
        textBox3.setText('Mensagem')
        textBox3.resize(250,200)


        #text_show2 = QtGui.QTextEdit()
        #text_show2.setText('SHOW2STR')
        #text_show2.setReadOnly(True)
        #text_show2.resize(200,10)


        #self.text = QtGui.QTextEdit(self)
        #self.text.move(0,400)


        #checkboxes
        checkBox = QtGui.QCheckBox('Telefonou',self)
        checkBox.move(10,10)
        checkBox.stateChanged.connect(self.printsomeshit) ##dunno yet

        checkBox1 = QtGui.QCheckBox('Veio Ca',self)
        checkBox1.move(10,40)
        checkBox1.stateChanged.connect(self.printsomeshit) ##dunno yet

        checkBox2 = QtGui.QCheckBox('Deseja Falar',self)
        checkBox2.move(10,70)
        checkBox2.stateChanged.connect(self.printsomeshit) ##dunno yet

        checkBox3 = QtGui.QCheckBox('deseja ve-lo',self)
        checkBox3.move(10,100)
        checkBox3.stateChanged.connect(self.printsomeshit) ##dunno yet

        checkBox4 = QtGui.QCheckBox('Volta a telefonar',self)
        checkBox4.move(150,10)
        checkBox4.stateChanged.connect(self.printsomeshit) ##dunno yet

        checkBox5 = QtGui.QCheckBox('Volta Ca',self)
        checkBox5.move(150,40)
        checkBox5.stateChanged.connect(self.printsomeshit) ##dunno yet

        checkBox6 = QtGui.QCheckBox('Pede para telefonar',self)
        checkBox6.move(150,70)
        checkBox6.stateChanged.connect(self.printsomeshit) ##dunno yet

        checkBox7 = QtGui.QCheckBox('Urgente',self)
        checkBox7.move(150,100)
        checkBox7.stateChanged.connect(self.printsomeshit) ##dunno yet

        self.show()

    def close_Application(self):
        #print('Good Bye!')
        #sys.exit()
        choice = QtGui.QMessageBox.question(self,'Warning!','Are you sure you want to leave?',
        QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)

        if (choice == QtGui.QMessageBox.Yes):
            print('GTFO')
            sys.exit()
        else:
            pass

    def printsomeshit(self):
        print('to do later')


def main():
    app = QtGui.QApplication(sys.argv)
    Gui = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
