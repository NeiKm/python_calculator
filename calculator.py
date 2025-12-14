from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont


"""
--------------------------------------------------KOREAN doc--------------------------------------------------
🧮 슈퍼 계산기 3000™ (거의 완성됨)

⏰ 시간: 또 밤
🧠 뇌 상태: “조금만 더 하고 잘까…”
☕ 커피: 예전에 있었음
💻 GitHub: 아직도 나를 판단하는 중

이 계산기는 이렇게 탄생했습니다:
— 심심해서
— PyQt5 연습하려고
— GitHub가 너무 비어 보였기 때문에
— 그리고 “금방 끝나겠지”라는 거짓말 때문에

🛠 프로젝트 상태:
✔ 기본 기능 — 작동함
✔ UI — 클릭 가능
❌ 에러 처리 — 나중에 추가 예정
❓ 언제? 귀찮지 않을 때
📅 날짜: 미정
📍 확률: 0은 아님

⚠️ 주의:
이상한 값을 입력하면
계산기가:
— 생각에 잠기거나
— 삐치거나
— 그냥 죽을 수도 있습니다

하지만 걱정 마세요 😌  
언젠가는:
— 프로젝트를 완성하고
— 제대로 된 에러 처리를 만들고
— “이제 완벽하다”라고 말할 겁니다

그때까지는:
🚀 즐기세요
🐛 버그는 기능입니다
😎 이 프로젝트는 경험입니다
--------------------------------------------------------------------------------------------------------------------------




--------------------------------------------------ENGCLISH doc--------------------------------------------------
🧮 SUPER CALCULATOR 3000™ (almost finished)

⏰ Time: way too late at night
🧠 Brain: “just a little more…”
☕ Coffee: existed at some point
💻 GitHub: silently judging me

This calculator was created:
— out of boredom
— to practice PyQt5
— because GitHub should not be empty
— and because “this won’t take long” (it did)

🛠 Project status:
✔ Core features — working
✔ UI — clickable
❌ Error handling — coming soon™
❓ When? When I’m not lazy
📅 Date: unknown
📍 Probability: not zero

⚠️ WARNING:
If you enter something weird,
the calculator might:
— start thinking
— get offended
— or simply crash

But don’t worry 😌  
One day I will:
— finish this project
— add proper error handling
— and say: “now it’s perfect”

Until then:
🚀 enjoy
🐛 bugs are features
😎 this project is experience
--------------------------------------------------------------------------------------------------------------------------



--------------------------------------------------RUSSIAN doc--------------------------------------------------
🧮 СУПЕР-КАЛЬКУЛЯТОР 3000™ (почти готов)

⏰ Время: снова ночь
🧠 Мозг: «ещё чуть-чуть и спать»
☕ Кофе: когда-то был
💻 GitHub: всё ещё смотрит с осуждением

Этот калькулятор был создан:
— из скуки
— ради PyQt5
— чтобы GitHub не выглядел заброшенным
— и потому что «ну осталось чуть-чуть»

🛠 Статус проекта:
✔ Основной функционал — работает
✔ Интерфейс — кликается
❌ Обработчик ошибок — будет добавлен
❓ Когда? Когда будет не лень
📅 Дата: неизвестна
📍 Вероятность: ненулевая

⚠️ ВНИМАНИЕ:
Если ввести что-то странное —
калькулятор может:
— задуматься
— обидеться
— или просто упасть

Но не переживай 😌  
Когда-нибудь я:
— доделаю проект
— сделаю нормальный обработчик ошибок
— и скажу: «ну вот, теперь идеально»

А пока:
🚀 enjoy
🐛 баги — это фичи
😎 проект — это опыт
--------------------------------------------------------------------------------------------------------------------------
"""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(311, 552)
        MainWindow.setFixedSize(311, 552)
        MainWindow.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 50, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label.setStyleSheet("padding: 20px;")
        self.label.setObjectName("label")
        self.button_procent = QtWidgets.QPushButton(self.centralwidget)
        self.button_procent.setGeometry(QtCore.QRect(10, 160, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_procent.setFont(font)
        self.button_procent.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_procent.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.button_procent.setObjectName("button_procent")
        self.button_drop = QtWidgets.QPushButton(self.centralwidget)
        self.button_drop.setGeometry(QtCore.QRect(80, 160, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_drop.setFont(font)
        self.button_drop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_drop.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.button_drop.setObjectName("button_drop")
        self.button_x = QtWidgets.QPushButton(self.centralwidget)
        self.button_x.setGeometry(QtCore.QRect(150, 160, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_x.setFont(QFont("blood", 24))
        self.button_x.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_x.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.button_x.setObjectName("button_x")
        self.button_remove = QtWidgets.QPushButton(self.centralwidget)
        self.button_remove.setGeometry(QtCore.QRect(230, 160, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_remove.setFont(font)
        self.button_remove.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.button_remove.setObjectName("button_remove")
        self.button_open = QtWidgets.QPushButton(self.centralwidget)
        self.button_open.setGeometry(QtCore.QRect(10, 220, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_open.setFont(font)
        self.button_open.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_open.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.button_open.setObjectName("button_open")
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(80, 220, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_close.setFont(font)
        self.button_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_close.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.button_close.setObjectName("button_close")
        self.button_coren = QtWidgets.QPushButton(self.centralwidget)
        self.button_coren.setGeometry(QtCore.QRect(150, 220, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_coren.setFont(font)
        self.button_coren.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_coren.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.button_coren.setObjectName("button_coren")
        self.button_rezdelit = QtWidgets.QPushButton(self.centralwidget)
        self.button_rezdelit.setGeometry(QtCore.QRect(230, 220, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_rezdelit.setFont(font)
        self.button_rezdelit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_rezdelit.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.button_rezdelit.setObjectName("button_rezdelit")
        self.button_umnogit = QtWidgets.QPushButton(self.centralwidget)
        self.button_umnogit.setGeometry(QtCore.QRect(230, 280, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_umnogit.setFont(font)
        self.button_umnogit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_umnogit.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.button_umnogit.setObjectName("button_umnogit")
        self.button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.button_minus.setGeometry(QtCore.QRect(230, 340, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_minus.setFont(font)
        self.button_minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_minus.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.button_minus.setObjectName("button_minus")
        self.button_plus = QtWidgets.QPushButton(self.centralwidget)
        self.button_plus.setGeometry(QtCore.QRect(230, 400, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_plus.setFont(font)
        self.button_plus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_plus.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.button_plus.setObjectName("button_plus")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(10, 280, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_7.setFont(font)
        self.button_7.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_7.setObjectName("button_7")
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(80, 280, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_8.setFont(font)
        self.button_8.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_8.setObjectName("button_8")
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(150, 280, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_9.setFont(font)
        self.button_9.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_9.setObjectName("button_9")
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(10, 340, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_4.setFont(font)
        self.button_4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_4.setObjectName("button_4")
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(80, 340, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_5.setFont(font)
        self.button_5.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_5.setObjectName("button_5")
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(150, 340, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_6.setFont(font)
        self.button_6.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_6.setObjectName("button_6")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(10, 400, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_1.setFont(font)
        self.button_1.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(80, 400, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_2.setFont(font)
        self.button_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(150, 400, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_3.setFont(font)
        self.button_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_3.setObjectName("button_3")
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(80, 460, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_0.setFont(font)
        self.button_0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_0.setObjectName("button_0")
        self.button_tochka = QtWidgets.QPushButton(self.centralwidget)
        self.button_tochka.setGeometry(QtCore.QRect(150, 460, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_tochka.setFont(font)
        self.button_tochka.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_tochka.setObjectName("button_tochka")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setGeometry(QtCore.QRect(10, 460, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_back.setFont(font)
        self.button_back.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_back.setObjectName("button_back")
        self.button_send = QtWidgets.QPushButton(self.centralwidget)
        self.button_send.setGeometry(QtCore.QRect(220, 460, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_send.setFont(font)
        self.button_send.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.button_send.setStyleSheet("background-color: rgb(110, 168, 255);")
        self.button_send.setObjectName("button_send")
        self.button_mode = QtWidgets.QPushButton(self.centralwidget)
        self.button_mode.setGeometry(QtCore.QRect(0, 0, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_mode.setFont(font)
        self.button_mode.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_mode.setObjectName("button_mode")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(6)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(166, 166, 166);\n"
"background-color: rgb(255, 255, 255);\n"
"padding: 10px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 133, 311, 21))
        self.label_3.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.button_procent.raise_()
        self.button_drop.raise_()
        self.button_x.raise_()
        self.button_remove.raise_()
        self.button_open.raise_()
        self.button_close.raise_()
        self.button_coren.raise_()
        self.button_rezdelit.raise_()
        self.button_umnogit.raise_()
        self.button_minus.raise_()
        self.button_plus.raise_()
        self.button_7.raise_()
        self.button_8.raise_()
        self.button_9.raise_()
        self.button_4.raise_()
        self.button_5.raise_()
        self.button_6.raise_()
        self.button_1.raise_()
        self.button_2.raise_()
        self.button_3.raise_()
        self.button_0.raise_()
        self.button_tochka.raise_()
        self.button_back.raise_()
        self.button_send.raise_()
        self.label_2.raise_()
        self.button_mode.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_functions()

        self.write = ""
        self.history = ""
        self.rem = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">0</span></p></body></html>"))
        self.button_procent.setText(_translate("MainWindow", "%"))
        self.button_drop.setText(_translate("MainWindow", "x/x"))
        self.button_x.setText(_translate("MainWindow", "x"))
        self.button_remove.setText(_translate("MainWindow", "remove"))
        self.button_open.setText(_translate("MainWindow", "("))
        self.button_close.setText(_translate("MainWindow", ")"))
        self.button_coren.setText(_translate("MainWindow", "√ "))
        self.button_rezdelit.setText(_translate("MainWindow", "÷"))
        self.button_umnogit.setText(_translate("MainWindow", "x"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_tochka.setText(_translate("MainWindow", ","))
        self.button_back.setText(_translate("MainWindow", "back"))
        self.button_send.setText(_translate("MainWindow", "="))
        self.button_mode.setText(_translate("MainWindow", "MODE"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">&gt; standart</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))


    def add_functions(self):
        self.button_0.clicked.connect(lambda: self.write_number(self.button_0.text()))
        self.button_1.clicked.connect(lambda: self.write_number(self.button_1.text()))
        self.button_2.clicked.connect(lambda: self.write_number(self.button_2.text()))
        self.button_3.clicked.connect(lambda: self.write_number(self.button_3.text()))
        self.button_4.clicked.connect(lambda: self.write_number(self.button_4.text()))
        self.button_5.clicked.connect(lambda: self.write_number(self.button_5.text()))
        self.button_6.clicked.connect(lambda: self.write_number(self.button_6.text()))
        self.button_7.clicked.connect(lambda: self.write_number(self.button_7.text()))
        self.button_8.clicked.connect(lambda: self.write_number(self.button_8.text()))
        self.button_9.clicked.connect(lambda: self.write_number(self.button_9.text()))
        self.button_plus.clicked.connect(lambda: self.write_number(self.button_plus.text()))
        self.button_minus.clicked.connect(lambda: self.write_number(self.button_minus.text()))
        self.button_back.clicked.connect(lambda: self.write_number(self.button_back.text()))
        self.button_rezdelit.clicked.connect(lambda: self.write_number(self.button_rezdelit.text()))
        self.button_umnogit.clicked.connect(lambda: self.write_number(self.button_umnogit.text()))
        self.button_send.clicked.connect(lambda: self.write_number(self.button_send.text()))
        self.button_drop.clicked.connect(lambda: self.write_number(self.button_drop.text()))
        self.button_open.clicked.connect(lambda: self.write_number(self.button_open.text()))
        self.button_close.clicked.connect(lambda: self.write_number(self.button_close.text()))
        self.button_procent.clicked.connect(lambda: self.write_number(self.button_procent.text()))
        self.button_coren.clicked.connect(lambda: self.write_number(self.button_coren.text()))
        self.button_x.clicked.connect(lambda: self.write_number(self.button_x.text()))
        self.button_remove.clicked.connect(lambda: self.write_number(self.button_remove.text()))
        self.button_tochka.clicked.connect(lambda: self.write_number(self.button_tochka.text()))
        self.button_mode.clicked.connect(lambda: self.write_number(self.button_mode.text()))

    def write_number(self, button):
        if button != "remove":
            self.write = self.write + button
        else:
            self.write = self.write[:-1]

        if button == "=":
            removing_txt = self.write[:-1].replace("x", "*")
            removing_txt = removing_txt.replace("÷", "/")
            self.write = str(eval(removing_txt))
            self.rem = True
            self.history = self.write
        if self.rem:
            self.label.setFont(QFont("Arial", 24))
            self.label.setText(self.write)
            self.write = ""
            self.rem = False
        else:
            self.label.setFont(QFont("Arial", 24))
            self.label.setText(self.write)

            self.label_3.setText(self.history)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
