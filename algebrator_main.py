from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.setEnabled(True)
        Window.setFixedSize(960, 540)
        Window.setStyleSheet("background-color: rgb(54, 54, 54);")

        self.login = QtWidgets.QLineEdit(parent=Window)
        self.login.setGeometry(QtCore.QRect(360, 180, 240, 24))
        self.login.setTabletTracking(False)
        self.login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.login.setObjectName("login")

        self.background_1 = QtWidgets.QLabel(parent=Window)
        self.background_1.setGeometry(QtCore.QRect(120, 30, 720, 480))
        self.background_1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(70, 70, 70, 255), stop:1 rgba(137, 135, 135, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(70, 70, 70, 255), stop:1 rgba(137, 135, 135, 255));")
        self.background_1.setText("")
        self.background_1.setObjectName("background_1")

        self.background = QtWidgets.QLabel(parent=Window)
        self.background.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.background.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 128, 167, 255), stop:1 rgba(0, 0, 36, 255));")
        self.background.setText("")
        self.background.setObjectName("background")

        self.frame = QtWidgets.QLabel(parent=Window)
        self.frame.setGeometry(QtCore.QRect(240, 70, 480, 60))
        self.frame.setObjectName("frame")

        self.frame_2 = QtWidgets.QLabel(parent=Window)
        self.frame_2.setGeometry(QtCore.QRect(300, 140, 360, 220))
        self.frame_2.setText("")
        self.frame_2.setObjectName("frame_2")

        self.label_log = QtWidgets.QLabel(parent=Window)
        self.label_log.setGeometry(QtCore.QRect(360, 160, 241, 21))
        self.label_log.setStyleSheet("")
        self.label_log.setObjectName("label_log")

        self.password = QtWidgets.QLineEdit(parent=Window)
        self.password.setGeometry(QtCore.QRect(360, 230, 240, 24))
        self.password.setTabletTracking(False)
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setObjectName("password")

        self.label_password = QtWidgets.QLabel(parent=Window)
        self.label_password.setGeometry(QtCore.QRect(360, 210, 241, 21))
        self.label_password.setStyleSheet("")
        self.label_password.setObjectName("label_password")

        self.enter_button = QtWidgets.QPushButton(parent=Window)
        self.enter_button.setGeometry(QtCore.QRect(360, 310, 240, 24))
        self.enter_button.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.enter_button.setObjectName("enter_button")

        self.frame_3 = QtWidgets.QLabel(parent=Window)
        self.frame_3.setGeometry(QtCore.QRect(300, 370, 360, 100))
        self.frame_3.setText("")
        self.frame_3.setObjectName("frame_3")

        self.reg_button = QtWidgets.QPushButton(parent=Window)
        self.reg_button.setGeometry(QtCore.QRect(360, 425, 240, 24))
        self.reg_button.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.reg_button.setObjectName("reg_button")

        self.label_reg = QtWidgets.QLabel(parent=Window)
        self.label_reg.setGeometry(QtCore.QRect(360, 390, 241, 21))
        self.label_reg.setStyleSheet("")
        self.label_reg.setObjectName("label_reg")

        self.error_enter_label = QtWidgets.QLabel(parent=Window)
        self.error_enter_label.setGeometry(QtCore.QRect(390, 335, 201, 21))
        self.error_enter_label.setObjectName("error_enter_label")

        self.visibility_password_button = QtWidgets.QPushButton(parent=Window)
        self.visibility_password_button.setGeometry(QtCore.QRect(360, 270, 120, 23))
        self.visibility_password_button.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.visibility_password_button.setObjectName("visibility_password_button")

        self.background.raise_()
        self.background_1.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.login.raise_()
        self.label_log.raise_()
        self.password.raise_()
        self.label_password.raise_()
        self.enter_button.raise_()
        self.frame_3.raise_()
        self.reg_button.raise_()
        self.label_reg.raise_()
        self.visibility_password_button.raise_()
        self.error_enter_label.raise_()

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Algebrator"))
        self.frame.setText(_translate("Window", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">Algebrator </span></p></body></html>"))
        self.label_log.setText(_translate("Window", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Имя пользователя:</span></p></body></html>"))
        self.label_password.setText(_translate("Window", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Пароль:</span></p></body></html>"))
        self.enter_button.setWhatsThis(_translate("Window", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Войти</span></p></body></html>"))
        self.enter_button.setText(_translate("Window", "Войти"))
        self.enter_button.setStyleSheet("background-color: rgb(0, 108, 187); border-radius: 6px; color: white; font-size: 13px; font: Verdana")
        self.reg_button.setWhatsThis(_translate("Window", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Войти</span></p></body></html>"))
        self.reg_button.setText(_translate("Window", "Зарегистрироваться"))
        self.reg_button.setStyleSheet("background-color: rgb(0, 108, 187); border-radius: 6px; color: white; font-size: 13px; font: Verdana")
        self.label_reg.setText(_translate("Window", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Нет аккаунта?</span></p></body></html>"))
        self.visibility_password_button.setText(_translate("Window", "Показать пароль"))
        self.visibility_password_button.setStyleSheet("background-color: rgb(40, 167, 234); border-radius: 4px; color: black; font-size: 13px; font: Verdana")
        self.error_enter_label.setText(_translate("Window","<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color: rgb(54, 54, 54);\"></span></p></body></html>"))
