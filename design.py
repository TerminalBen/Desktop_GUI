# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
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
        self.verticalLayout.addWidget(self.textBox2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_1 = QtWidgets.QCheckBox(Form)
        self.checkBox_1.setObjectName("checkBox_1")
        self.verticalLayout_2.addWidget(self.checkBox_1)
        self.checkBox2 = QtWidgets.QCheckBox(Form)
        self.checkBox2.setObjectName("checkBox2")
        self.verticalLayout_2.addWidget(self.checkBox2)
        self.checkBox3 = QtWidgets.QCheckBox(Form)
        self.checkBox3.setObjectName("checkBox3")
        self.verticalLayout_2.addWidget(self.checkBox3)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox4 = QtWidgets.QCheckBox(Form)
        self.checkBox4.setObjectName("checkBox4")
        self.verticalLayout_4.addWidget(self.checkBox4)
        self.checkBox5 = QtWidgets.QCheckBox(Form)
        self.checkBox5.setObjectName("checkBox5")
        self.verticalLayout_4.addWidget(self.checkBox5)
        self.checkBox6 = QtWidgets.QCheckBox(Form)
        self.checkBox6.setObjectName("checkBox6")
        self.verticalLayout_4.addWidget(self.checkBox6)
        self.checkBox7 = QtWidgets.QCheckBox(Form)
        self.checkBox7.setObjectName("checkBox7")
        self.verticalLayout_4.addWidget(self.checkBox7)
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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.checkBox_3.setText(_translate("Form", "Telefonou"))
        self.checkBox_1.setText(_translate("Form", "Veio ca"))
        self.checkBox2.setText(_translate("Form", "Deseja Falar"))
        self.checkBox3.setText(_translate("Form", "Deseja Ve-lo"))
        self.checkBox4.setText(_translate("Form", "Volta a Telefonar"))
        self.checkBox5.setText(_translate("Form", "Volta Ca"))
        self.checkBox6.setText(_translate("Form", "Pede para telefonar"))
        self.checkBox7.setText(_translate("Form", "Urgente"))
        self.btn2.setText(_translate("Form", "Enviar"))
        self.btn3.setText(_translate("Form", "Limpar tudo"))
        self.btn1.setText(_translate("Form", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

