'''
import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setGeometry(50,50,500,300)
window.setWindowTitle("PyQt Tutorial!")

window.show()
'''

import sys
from PyQt4 import QtGui,QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,300,500)
        self.setWindowTitle('Hell Yeah!!!')
        self.setWindowIcon(QtGui.QIcon('/Users/bentolima/Desktop/Logo.png'))
        self.home()

    def home(self):
        btn = QtGui.QPushButton('Quit',self)
        btn.clicked.connect(self.close_Application)
        #btn.resize(100,100)
        btn.resize(btn.sizeHint())
        btn.move(0,0)
        self.show()

    def close_Application(self):
        print('Good Bye!')
        sys.exit()

def main():
    app = QtGui.QApplication(sys.argv)
    Gui = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
