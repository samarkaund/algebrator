import sys
import matplotlib.pyplot as plt

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer

from algebrator_main import Ui_MainWindow
from algebrator_reg import Ui_RegForm
from main_app_window import Ui_AppMainWindow
from profile_ui import Ui_Profile
from theory import Ui_Theory

from db_file import OpenTableDB
from answers import Answers


class SignInWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.open_db = OpenTableDB()

        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.visibility_password_button.clicked.connect(self.visibility_password_function)
        self.enter_button.clicked.connect(self.enter_in_app)
        self.reg_button.clicked.connect(self.open_reg_window)

    def visibility_password_function(self):
        if self.sender().text() == 'Показать пароль':
            self.visibility_password_button.setText('Скрыть пароль')
            self.password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.visibility_password_button.setText('Показать пароль')
            self.password.setEchoMode(QLineEdit.EchoMode.Password)

    def enter_in_app(self):
        self.enter_user = self.login.text()
        self.enter_pswrd = self.password.text()
        if not self.open_db.user_in_db(self.enter_user):
            self.error_enter_label.setText("Неверный логин или пароль")
            self.error_enter_label.setStyleSheet('color: red; background-color: rgb(54, 54, 54);  font-weight:600;  font-size:10pt; font: Verdana;')
        else:
            self.error_enter_label.setText("")
            if self.open_db.corr_log_and_pswrd(self.enter_user, self.enter_pswrd):
                self.close()
                self.app_window = AppMainWindow(self.enter_user)
                self.app_window.show()
            else:
                self.error_enter_label.setText("Неверный логин или пароль")
                self.error_enter_label.setStyleSheet('color: red; background-color: rgb(54, 54, 54);  font-weight:600;  font-size:10pt;')

    def open_reg_window(self):
        self.reg_form = RegForm()
        self.reg_form.show()

    def closeEvent(self, event):
        QApplication.closeAllWindows()
        self.open_db.close_connection()


class RegForm(QWidget, Ui_RegForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.registration_button.clicked.connect(self.add_user_in_db)
        self.reg_password_1.setEchoMode(QLineEdit.EchoMode.Password)
        self.reg_password2.setEchoMode(QLineEdit.EchoMode.Password)

        self.db = OpenTableDB()

    def add_user_in_db(self):
        self.usr = self.reg_nickname.text()
        self.pswrd = self.reg_password_1.text()
        if self.db.user_in_db(self.usr):
            self.error_label.setText("Пользователь с таким именем уже есть")
            self.error_label.setStyleSheet("color: red; background-color: rgb(54, 54, 54);  font-weight:600;  font-size:10pt;")
        elif self.reg_password_1.text() != self.reg_password2.text():
            self.error_label.setText("Пароли не совпадают")
            self.error_label.setStyleSheet("color: red; background-color: rgb(54, 54, 54);  font-weight:600;  font-size:10pt;")
        elif len(self.pswrd) != 6:
            self.error_label.setText("Пароль должен состоять ровно из 6 символов")
            self.error_label.setStyleSheet("color: red; background-color: rgb(54, 54, 54);  font-weight:600;  font-size:10pt;")
        elif len(self.usr) < 6 or len(self.usr) > 15:
            self.error_label.setText("Ник должен содержать от 6 до 15 символов")
            self.error_label.setStyleSheet("color: red; background-color: rgb(54, 54, 54);  font-weight:600;  font-size:10pt;")
        else:
            self.error_label.setText("")
            self.db.add_user(self.usr, self.pswrd)
            QApplication.closeAllWindows()
            self.app_main_window = AppMainWindow(self.usr)
            self.app_main_window.show()

    def closeEvent(self, event):
        self.db.close_connection()


class AppMainWindow(QWidget, Ui_AppMainWindow):
    def __init__(self, username):
        super().__init__()
        self.setupUi(self)

        self.database = OpenTableDB()
        self.ans = Answers()
        self.timer = QTimer(self)
        self.theory = Theory()

        self.timer.timeout.connect(self.update_time)
        self.time_elapsed = 0
        self.time_label = QLabel('00:00:00', self)
        self.time_label.setStyleSheet("font-size: 30px;")
        self.time_label.move(1500, 1500)

        self.username = username
        self.nick_label = QLabel(self)
        self.nick_label.setText(f"{self.username}   Рейтинг : {self.database.return_mmr(self.username)}")
        self.nick_label.setStyleSheet("color: white;  font-weight:600;  font-size:12pt;")
        self.nick_label.move(255, 30)
        self.nick_label.resize(700, 21)
        self.type_and_hard_ur_label = QLabel(self)
        self.type_and_hard_ur_label.setText(f"Добро пожаловать!")
        self.type_and_hard_ur_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
        self.type_and_hard_ur_label.move(250, 25)
        self.type_and_hard_ur_label.resize(800, 175)
        self.hwa = QLabel(self)
        self.hwa.setText("""Как завписывать ответ?

Если дробь можно перевести в десятичную, то ответ записывается в десятичной дроби.
умножение - xf - где (f) какая-то функция, a (x) какое-либо число.
дробь - x/y
дробь где в знаменателе или числителе находится сумма или разность - (x+z)/y или - x/(y+z)

Функции:
-loga(b) - где (a) - основание логарифма, (b) - число логарифма
-квадратный корень - sqrt(x)
-arcsin - arcsin(x)
-arccos - arccos(x)
-arctg - arctg(x)
-arcctg - arcctg(x)

Число Пи - P(латиница)
В отвтах на тригонометрические уравнения, например: P/2+Pn, коэффициент отвечающий за переодичность - n
при этом сразу подразумевается что n принадлежит множеству целых чисел.

""")
        self.hwa.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
        self.hwa.move(250, 160)
        self.hwa.resize(900, 450)
        self.r_ur_label = QLabel(self)
        self.r_ur_label.setText("")
        self.r_ur_label.move(250, 60)
        self.r_ur_label.resize(400, 175)
        self.r_ur_label2 = QLabel(self)
        self.r_ur_label2.setText("")
        self.r_ur_label2.move(250, 350)
        self.r_ur_label2.resize(500, 175)
        self.answer_label = QLabel(self)
        self.answer_label.setText("")
        self.answer_label.move(250, 355)
        self.answer_label.resize(400, 20)
        self.answer_label2 = QLabel(self)
        self.answer_label2.setText("")
        self.answer_label2.move(250, 555)
        self.answer_label2.resize(500, 20)
        self.image = QLabel(self)
        self.image.setScaledContents(True)
        self.image2 = QLabel(self)
        self.image2.setScaledContents(True)
        self.image_logo = QLabel(self)
        self.image_logo.setScaledContents(True)
        pixmap_logo = QPixmap("logo.png")
        self.image_logo.resize(pixmap_logo.size() / 15)
        self.image_logo.move(123, 15)
        self.image_logo.setPixmap(pixmap_logo)
        self.input_answer = QLineEdit(self)
        self.input_answer.move(1000, 2000)
        self.input_answer2 = QLineEdit(self)
        self.input_answer2.move(1000, 2000)
        self.to_answer_button = QPushButton(self)
        self.to_answer_button.setText("Ответить")
        self.to_answer_button.move(1100, 2000)
        self.to_answer_button.setStyleSheet("background-color: rgb(0, 108, 187); border-radius: 6px; color: white; font-size: 13px; font: Verdana")
        self.next_button = QPushButton(self)
        self.next_button.setText("Следующее задание >>>")
        self.next_button.move(1200, 2000)
        self.next_button.setStyleSheet("background-color: rgb(0, 108, 187); border-radius: 6px; color: white; font-size: 13px; font: Verdana")
        self.theory_button = QPushButton(self)
        self.theory_button.setText("Теория к заданиям")
        self.theory_button.move(10, 150)
        self.theory_button.resize(221, 23)
        self.ur_type = ''
        self.type = ''
        self.ur_hard = ''
        self.task = ''
        self.info_label = QLabel(self)
        self.info_label.setText("")
        self.info_label.move(430, 423)
        self.info_label.resize(600, 25)
        self.task_is_completed = False
        self.active = False
        self.attempts = 0
        self.prof = Profile(self.username)

        self.to_answer_button.clicked.connect(self.check_answer)
        self.ExitButton.clicked.connect(self.exit_func)
        self.EasyUrButton.clicked.connect(self.out_ur)
        self.MidUrButton.clicked.connect(self.out_ur)
        self.HardUrButton.clicked.connect(self.out_ur)
        self.next_button.clicked.connect(self.next_task)
        self.profileButton.clicked.connect(self.out_profile)
        self.theory_button.clicked.connect(self.out_theory)

    def start_timer(self):
        if not self.timer.isActive():
            self.timer.start(1000)

    def update_time(self):
        self.time_elapsed += 1
        hours = self.time_elapsed // 3600
        minutes = (self.time_elapsed % 3600) // 60
        seconds = self.time_elapsed % 60
        self.time_label.setText(f'{hours:0>2}:{minutes:0>2}:{seconds:0>2}')

    def out_ur(self):
        self.hwa.move(2500, 160)

        if self.task_is_completed:
            self.next_task()
        elif self.active:
            if self.hard_text != self.sender().text() or self.type != self.SelectUrType.currentText():
                self.time_label.setText('00:00:00')
                self.time_elapsed = 0

        self.active = True
        self.hard_text = self.sender().text()

        if self.hard_text == 'Простые':
            self.ur_hard = 'a'
        elif self.hard_text == 'Средние':
            self.ur_hard = 'b'
        elif self.hard_text == 'Сложные':
            self.ur_hard = 'c'

        self.time_label.move(1060, 100)
        self.ur_type = self.SelectUrType.currentText()

        if self.ur_type == 'Рациональные':
            self.type = 'rac'
        elif self.ur_type == 'Иррациональные':
            self.type = 'irr'
        elif self.ur_type == 'Показательные':
            self.type = 'poc'
        elif self.ur_type == 'Модульные':
            self.type = 'mod'
        elif self.ur_type == 'Логарифмические':
            self.type = 'log'
        elif self.ur_type == 'Тригонометрические':
            self.type = 'trg'
        self.input_answer.setText("")
        self.input_answer2.setText("")
        self.type_and_hard_ur_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
        self.task = self.database.select_not_resolved_task(f"{self.type}_ur", self.ur_hard, self.username)
        if self.task != 'None':
            self.input_answer2.move(250, 1000)
            self.info_label.setText("")
            self.r_ur_label2.setText("")
            self.info_label.move(430, 423)
            self.answer_label2.setText("")
            self.image2.move(0, 1000)
            self.type_and_hard_ur_label.setText(f"{self.ur_type} уравнения. Уровень {self.ur_hard.upper()}. Задание {self.task}")
            pixmap = QPixmap(f"ur/{self.type}_ur_{self.ur_hard}{self.task}.png")
            pic_size = pixmap.size() / 4
            self.image.resize(pic_size)
            self.image.move(250, 255 - int(str(pic_size)[19:-1].split(', ')[1])//2)
            self.image.setPixmap(pixmap)
            self.r_ur_label.setText('Найдите корни уравнения:')
            self.r_ur_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
            self.answer_label.setText('Запишите корни уравнеия через " ; ".')
            self.answer_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
            self.input_answer.move(250, 390)
            self.input_answer.resize(285, 21)
            self.to_answer_button.move(540, 388)
            self.to_answer_button.resize(75, 24)
            self.next_button.move(250, 425)
            self.next_button.resize(170, 24)
            if self.ur_hard == "b":
                self.input_answer2.setText("")
                pixmap2 = QPixmap(f"ur/{self.type}_ur_{self.ur_hard}{self.task}_b.png")
                pic_size2 = pixmap2.size() / 5
                self.image2.resize(pic_size2)
                self.image2.move(250, 500 - int(str(pic_size2)[19:-1].split(', ')[1]) // 2)
                self.image2.setPixmap(pixmap2)
                self.next_button.move(250, 625)
                self.info_label.move(430, 624)
                self.r_ur_label2.setText("Найдите все корни принадлежащие промежутку:")
                self.r_ur_label2.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
                self.answer_label2.setText('Запишите через " ; " корни принадлежащие этому промежутку.')
                self.answer_label2.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
                self.input_answer2.move(250, 590)
                self.input_answer2.resize(285, 21)
                self.to_answer_button.move(540, 588)
        else:
            self.type_and_hard_ur_label.setText(f"{self.ur_type} уравнения. Уровень {self.ur_hard.upper()}. Вы решили все уравнения этого типа. Так держать!")
            self.time_label.move(1500, 1500)
            self.next_button.move(1200, 2000)
            self.to_answer_button.move(1100, 2000)
            self.answer_label.setText('')
            self.r_ur_label.setText("")
            self.input_answer.move(1000, 2000)
            self.image.move(1000, 2000)
            self.image2.move(1300, 2400)
            self.input_answer2.move(1000, 2000)
            self.r_ur_label2.setText("")
            self.answer_label2.setText('')

        if not self.task_is_completed:
            self.start_timer()

    def check_answer(self):
        self.attempts += 1
        str_user_answer = self.input_answer.text()
        str_right_answer = self.ans.return_answer(self.type, self.ur_hard, int(self.task))
        user_answer = ""
        right_answer = ""

        for i in str_user_answer:
            if i != ' ':
                if i == ".":
                    user_answer += ','
                else:
                    user_answer += i

        for i in str_right_answer:
            if i != ' ':
                right_answer += i

        if self.ur_hard == "b":
            str_user_answer2 = self.input_answer2.text()
            str_right_answer2 = self.ans.return_answer(self.type, self.ur_hard, f"{self.task}_b")
            user_answer2 = ""
            right_answer2 = ""

            for i in str_user_answer2:
                if i != ' ':
                    if i == ".":
                        user_answer2 += ','
                    else:
                        user_answer2 += i

            for i in str_right_answer2:
                if i != ' ':
                    right_answer2 += i
            right_answer2 = set(right_answer2.split(";"))
            user_answer2 = set(user_answer2.split(";"))

        right_answer = set(right_answer.split(";"))
        user_answer = set(user_answer.split(";"))
        right_answer_for_label = f"Задача решена. Корни уравнения: {' ; '.join(right_answer)}"

        if (user_answer == right_answer and not self.task_is_completed and self.ur_hard != "b") or (self.ur_hard == "b" and user_answer == right_answer and user_answer2 == right_answer2 and not self.task_is_completed):
            self.info_label.setText(right_answer_for_label)
            self.task_is_completed = True
            rating_change = int(1000 / (self.time_elapsed / 60 * self.attempts) * self.database.hard_to_int(self.ur_hard) / 3)
            t_id = self.database.id_tasks((self.type + '_ur'), self.ur_hard, int(self.task))
            us_id = self.database.id_user(self.username)
            self.database.up_mmr(rating_change, self.username)
            self.database.add_resolve_task(t_id, us_id, self.time_label.text(), self.attempts)
            self.nick_label.setText(f"{self.username}  Рейтинг : {self.database.return_mmr(self.username)}")
            self.timer.stop()

        elif self.info_label.text() != right_answer_for_label:
            self.info_label.setText("Пока что неверно")

        self.info_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")

    def next_task(self):
        if self.task_is_completed:
            self.task_is_completed = False
            self.time_elapsed = 0
            self.attempts = 0
            self.input_answer.setText('')
            self.info_label.setText("")
            self.task = self.database.select_not_resolved_task(self.type + '_ur', self.ur_hard, self.username)
            if self.task != 'None':
                self.type_and_hard_ur_label.setText(f"{self.ur_type} уравнения. Уровень {self.ur_hard.upper()}. Задание {self.task}")
                pixmap = QPixmap(f"ur/{self.type}_ur_{self.ur_hard}{self.task}.png")
                pic_size = pixmap.size() / 4
                self.image.resize(pic_size)
                self.image.move(250, 255 - int(str(pic_size)[19:-1].split(', ')[1])//2)
                self.image.setPixmap(pixmap)
                if self.ur_hard == "b":
                    pixmap2 = QPixmap(f"ur/{self.type}_ur_{self.ur_hard}{self.task}_b.png")
                    pic_size2 = pixmap2.size() / 5
                    self.image2.resize(pic_size2)
                    self.image2.move(250, 500 - int(str(pic_size2)[19:-1].split(', ')[1]) // 2)
                    self.image2.setPixmap(pixmap2)
                    self.input_answer2.setText("")
            else:
                self.type_and_hard_ur_label.setText(f"{self.ur_type} уравнения. Уровень {self.ur_hard.upper()}. Вы решили все уравнения этого типа. Так держать!")
                self.time_label.move(1500, 1500)
                self.next_button.move(1200, 2000)
                self.to_answer_button.move(1100, 2000)
                self.answer_label.setText('')
                self.r_ur_label.setText("")
                self.input_answer.move(1000, 2000)
                self.image.move(1000, 2000)
                self.image2.move(1300, 2400)
                self.input_answer2.move(1000, 2000)
                self.r_ur_label2.setText("")
                self.answer_label2.setText('')
        else:
            self.info_label.setText("Вы не можете этого сделать пока не решите задание.")
            self.info_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
        if not self.task_is_completed:
            self.start_timer()

    def out_theory(self):
        self.theory.show()


    def out_profile(self):
        self.prof.show()

    def exit_func(self):
        QApplication.closeAllWindows()
        self.open_enter_window = SignInWindow()
        self.open_enter_window.show()

    def closeEvent(self, event):
        QApplication.closeAllWindows()
        self.database.close_connection()


class Profile(QWidget, Ui_Profile):
    def __init__(self, username):
        super().__init__()
        self.setupUi(self)
        self.db = OpenTableDB()

        self.username = username
        self.nick_label.setText(self.username)
        self.nick_label.setStyleSheet("color: white;  font-weight:600;  font-size:12pt;")
        self.rac_label.setText(f"Рациональные: Решено({self.db.count_resolved_tasks('rac', self.username)}/56)")
        self.irr_label.setText(f"Иррациональные: Решено({self.db.count_resolved_tasks('irr', self.username)}/15)")
        self.mod_label.setText(f"Модульные: Решено({self.db.count_resolved_tasks('mod', self.username)}/15)")
        self.poc_label.setText(f"Показательные: Решено({self.db.count_resolved_tasks('poc', self.username)}/15)")
        self.log_label.setText(f"Логарифмические: Решено({self.db.count_resolved_tasks('log', self.username)}/15)")
        self.trg_label.setText(f"Тригонометрические: Решено({self.db.count_resolved_tasks('trg', self.username)}/15)")
        self.rac_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
        self.irr_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
        self.mod_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
        self.poc_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
        self.log_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
        self.trg_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")

        k = 0
        x = ['Рац.', 'Иррац.', 'Мод.', 'Показ.', 'Лог.', 'Тригоном.']
        y = []
        for i in ['rac', 'irr', 'mod', 'poc', 'log', 'trg']:
            y.append(self.db.sum_mmr(i, self.username))
        plt.bar(x, y, label='mmr')
        plt.xlabel('Типы уравнений')
        plt.ylabel('Полученный рейтинг')
        plt.title('Полученный рейтинг в разных типах уравнений')
        plt.legend()
        plt.savefig('mmr_chart.png')
        plt.close()

        self.image_label.setScaledContents(True)
        pixmap = QPixmap("mmr_chart.png")
        self.image_label.resize(pixmap.size())
        self.image_label.move(7, 80)
        self.image_label.setPixmap(pixmap)

        self.updateButton.clicked.connect(self.update)

    def update(self):
        self.db.close_connection()
        self.db = OpenTableDB()
        self.rac_label.setText(f"Рациональные: Решено({self.db.count_resolved_tasks('rac', self.username)}/56)")
        self.irr_label.setText(f"Иррациональные: Решено({self.db.count_resolved_tasks('irr', self.username)}/15)")
        self.mod_label.setText(f"Модульные: Решено({self.db.count_resolved_tasks('mod', self.username)}/15)")
        self.poc_label.setText(f"Показательные: Решено({self.db.count_resolved_tasks('poc', self.username)}/15)")
        self.log_label.setText(f"Логарифмические: Решено({self.db.count_resolved_tasks('log', self.username)}/15)")
        self.trg_label.setText(f"Тригонометрические: Решено({self.db.count_resolved_tasks('trg', self.username)}/15)")
        self.rac_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
        self.irr_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
        self.mod_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
        self.poc_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
        self.log_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")
        self.trg_label.setStyleSheet("color: black;  font-weight:600;  font-size:12pt;")

        k = 0
        x = ['Рац.', 'Иррац.', 'Мод.', 'Показ.', 'Лог.', 'Тригоном.']
        y = []
        for i in ['rac', 'irr', 'mod', 'poc', 'log', 'trg']:
            y.append(self.db.sum_mmr(i, self.username))
        plt.bar(x, y, label='mmr')
        plt.xlabel('Типы уравнений')
        plt.ylabel('Полученный рейтинг')
        plt.title('Полученный рейтинг в разных типах уравнений')
        plt.legend()
        plt.savefig('mmr_chart.png')
        plt.close()

        self.image_label.setScaledContents(True)
        pixmap = QPixmap("mmr_chart.png")
        self.image_label.resize(pixmap.size())
        self.image_label.move(7, 80)
        self.image_label.setPixmap(pixmap)

    def closeEvent(self, event):
        self.db.close_connection()


class Theory(QWidget, Ui_Theory):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SignInWindow()
    ex.show()
    sys.exit(app.exec())
