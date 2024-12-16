from PyQt6 import QtCore, QtWidgets


class Ui_RegForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Регистрация")
        Form.setFixedSize(400, 308)
        Form.move(760, 379)
        Form.setStyleSheet("background-color: rgb(135, 135, 135);")

        self.reg_label = QtWidgets.QLabel(parent=Form)
        self.reg_label.setGeometry(QtCore.QRect(25, 20, 350, 50))
        self.reg_label.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.reg_label.setObjectName("label")

        self.reg_background = QtWidgets.QLabel(parent=Form)
        self.reg_background.setGeometry(QtCore.QRect(25, 82, 350, 211))
        self.reg_background.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.reg_background.setText("")
        self.reg_background.setObjectName("label_2")

        self.reg_nickname = QtWidgets.QLineEdit(parent=Form)
        self.reg_nickname.setGeometry(QtCore.QRect(40, 110, 321, 21))
        self.reg_nickname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.reg_nickname.setObjectName("lineEdit")

        self.reg_nickname_label = QtWidgets.QLabel(parent=Form)
        self.reg_nickname_label.setEnabled(True)
        self.reg_nickname_label.setGeometry(QtCore.QRect(40, 90, 321, 20))
        self.reg_nickname_label.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.reg_nickname_label.setObjectName("label_3")

        self.reg_password1_label = QtWidgets.QLabel(parent=Form)
        self.reg_password1_label.setEnabled(True)
        self.reg_password1_label.setGeometry(QtCore.QRect(40, 135, 321, 20))
        self.reg_password1_label.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.reg_password1_label.setObjectName("label_4")

        self.reg_password_1 = QtWidgets.QLineEdit(parent=Form)
        self.reg_password_1.setGeometry(QtCore.QRect(40, 155, 321, 21))
        self.reg_password_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.reg_password_1.setObjectName("lineEdit_2")

        self.reg_password2_label = QtWidgets.QLabel(parent=Form)
        self.reg_password2_label.setEnabled(True)
        self.reg_password2_label.setGeometry(QtCore.QRect(40, 180, 321, 20))
        self.reg_password2_label.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.reg_password2_label.setObjectName("label_5")

        self.reg_password2 = QtWidgets.QLineEdit(parent=Form)
        self.reg_password2.setGeometry(QtCore.QRect(40, 200, 321, 21))
        self.reg_password2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.reg_password2.setObjectName("lineEdit_3")

        self.registration_button = QtWidgets.QPushButton(parent=Form)
        self.registration_button.setGeometry(QtCore.QRect(40, 250, 321, 23))
        self.registration_button.setObjectName("pushButton")

        self.error_label = QtWidgets.QLabel(parent=Form)
        self.error_label.setEnabled(True)
        self.error_label.setGeometry(QtCore.QRect(40, 226, 321, 20))
        self.error_label.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.error_label.setObjectName("label_6")

        self.reg_background.raise_()
        self.reg_label.raise_()
        self.reg_nickname.raise_()
        self.reg_nickname_label.raise_()
        self.reg_password1_label.raise_()
        self.reg_password_1.raise_()
        self.reg_password2_label.raise_()
        self.reg_password2.raise_()
        self.registration_button.raise_()
        self.error_label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Региcтрация в Algebrator"))
        self.reg_label.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Регистрация</span></p></body></html>"))
        self.reg_label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Регистрация</span></p></body></html>"))
        self.reg_nickname_label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Введите имя пользователя:</span></p></body></html>"))
        self.reg_password1_label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Установите пароль:</span></p></body></html>"))
        self.reg_password2_label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Повторите пароль:</span></p></body></html>"))
        self.registration_button.setText(_translate("Form", "Зарегистрироваться"))
        self.registration_button.setStyleSheet("background-color: rgb(0, 108, 187); border-radius: 4px; color: white; font-size: 13px; font: Verdana")
        self.error_label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\"> </span></p></body></html>"))
