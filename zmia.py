import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt, QTimer
import sqlite3
import winsound
from threading import Thread
from PyQt5.QtWidgets import QInputDialog

"""
made by mkoost228

python 3.7.2

libs I use:
    PyQt5
    sqlite3
    winsound
    threading
    random
    sys

release: 03.11.2019

v 1.0.0
"""

def sou1():
    winsound.PlaySound('sounds/button-20.wav', winsound.SND_FILENAME)

def sou2():
    winsound.PlaySound('sounds/beep-03.wav', winsound.SND_FILENAME)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.scores = [QLabel(self),
                       QLabel(self),
                       QLabel(self),
                       QLabel(self),
                       QLabel(self),
                       QLabel(self),
                       QLabel(self),
                       QLabel(self),
                       QLabel(self),
                       QLabel(self)]

        for i in range(1, 11):
            self.scores[i - 1].setText(str(i) + ":")
            self.scores[i - 1].move(5, 20 + i * 25)
            self.scores[i - 1].setStyleSheet("color: rgb(255, 255, 255); font: 10pt 'MS Serif';")
            self.scores[i - 1].close()
        self.skin = ["background-color: rgb(0, 255, 0);",
                     "background-color: rgb(0, 0, 255);",
                     "background-color: rgb(255, 0, 0);",
                     "background-color: rgb(255, 255, 255);"]

        self.scoresShowed = False
        self.numSkin = 0
        self.alive = False
        self.fl = True
        self.mach = 3
        self.a = 10
        self.b = 0
        self.xt = 0
        self.yt = 0
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setFixedSize(300, 300)
        self.setWindowTitle('Msnake')

        self.dotSn = QPushButton(self)
        self.dotSn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.dotSn.resize(10, 10)
        self.dotSn.close()

        self.scoreLb = QLabel(self)
        self.scoreLb.move(10, 250)
        self.scoreLb.setText("0000")
        self.scoreLb.setStyleSheet("color: rgb(255, 255, 255); font: 10pt 'MS Serif';")
        self.scoreLb.resize(100, 14)
        self.scoreLb.show()

        self.label = QLabel(self)
        self.label.move(10, 230)
        self.label.setText("Your score:")
        self.label.setStyleSheet("color: rgb(255, 255, 255); font: 10pt 'MS Serif';")
        self.label.resize(100, 14)
        self.label.show()

        self.start_btn = QPushButton(self)
        self.start_btn.move(110, 90)
        self.start_btn.resize(65, 25)
        self.start_btn.setStyleSheet("color: rgb(255, 255, 255); font: 10pt 'MS Serif';")
        self.start_btn.setText("start")

        self.btn = []

        self.lftBtn = QPushButton(self)

        self.lftBtn.move(200, 230)
        self.lftBtn.setText("<")
        self.lftBtn.setStyleSheet("color: rgb(255, 255, 255); font: 10pt 'MS Serif'; background-color: rgb(0, 0, 0);")
        self.lftBtn.resize(20, 20)
        self.lftBtn.clicked.connect(self.lftSkinBtn)
        self.skinBtn = QPushButton(self)

        self.skinBtn.move(225, 230)
        self.skinBtn.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.skinBtn.resize(20, 20)

        self.rgtBtn = QPushButton(self)

        self.rgtBtn.move(250, 230)
        self.rgtBtn.setText(">")
        self.rgtBtn.setStyleSheet("color: rgb(255, 255, 255); font: 10pt 'MS Serif'; background-color: rgb(0, 0, 0);")
        self.rgtBtn.resize(20, 20)
        self.rgtBtn.clicked.connect(self.rgtSkinBtn)

        self.name = QLineEdit(self)
        self.name.move(205, 260)
        self.name.setStyleSheet("color: rgb(255, 255, 255); font: 10pt 'MS Serif'; background-color: rgb(0, 0, 0);")
        self.name.resize(60, 25)
        self.name.textChanged.connect(self.nameChange)

        self.tp5 = QPushButton(self)
        self.tp5.move(5, 10)
        self.tp5.setText("All Scores")
        self.tp5.setStyleSheet("color: rgb(255, 255, 255); font: 10pt 'MS Serif';")
        self.tp5.resize(100, 20)
        self.tp5.clicked.connect(self.showScores)

        self.clearHistory = QPushButton(self)
        self.clearHistory.move(180, 10)
        self.clearHistory.setText("Clear History")
        self.clearHistory.setStyleSheet("color: rgb(255, 255, 255); font: 10pt 'MS Serif';")
        self.clearHistory.resize(110, 20)
        self.clearHistory.clicked.connect(self.clearHistorySc)

        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.start_btn.clicked.connect(self.timerST)


        self.show()


    def timerST(self):
        if self.name.text() == "":
            self.name.setText("name")
        for i in self.btn:
            i.close()
            i.destroy()
        self.btn = []

        for i in range(4):
            self.btn.append(QPushButton(self))
            self.btn[i].resize(10, 10)
            self.btn[i].move(10 * i, 10)
            self.btn[i].setStyleSheet(self.skinBtn.styleSheet())
            self.btn[i].show()

        self.tmr = QTimer(self)
        self.tmr.setInterval(100)
        self.tmr.timeout.connect(self.j)

        self.closeLeb()

        self.tmr.start()
        self.alive = True

    def closeLeb(self):
        self.start_btn.close()
        self.label.close()
        self.scoreLb.close()
        self.lftBtn.close()
        self.rgtBtn.close()
        self.skinBtn.close()
        self.tp5.close()
        self.name.close()
        self.clearHistory.close()
        self.dotSn.show()

    def openLeb(self):
        self.start_btn.show()
        self.label.show()
        self.scoreLb.show()
        self.lftBtn.show()
        self.rgtBtn.show()
        self.skinBtn.show()
        self.tp5.show()
        self.name.show()
        self.clearHistory.show()
        self.dotSn.close()
        self.scoreLb.setText("0" * (4 - len(str(len(self.btn)))) + str(len(self.btn)))

    def j(self):
        self.allDo()
        if self.fl:
            self.dot_rand()

        elif self.btn[-1].x() == self.xt and self.btn[-1].y() == self.yt:
            self.snake_plus()

        if not self.alive:
            sou2()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.b = 0
            if self.a == 0:
                self.a = 10
        if event.key() == Qt.Key_Left:
            self.b = 0
            if self.a == 0:
                self.a = -10
        if event.key() == Qt.Key_Up:
            self.a = 0
            if self.b == 0:
                self.b = -10
        if event.key() == Qt.Key_Down:
            self.a = 0
            if self.b == 0:
                self.b = 10

    def move_snake(self):
        for i in range(len(self.btn) - 1):
            self.is_dead(i)
            self.btn[i].move(self.btn[i + 1].x(), self.btn[i + 1].y())
            self.btn[i].show()

    def is_dead(self, i):
        if self.btn[-1].x() == self.btn[i].x() and self.btn[-1].y() == self.btn[i].y() or not self.alive:
            self.openLeb()
            self.tmr.stop()
            self.a = 10
            self.b = 0
            self.saveScore()
            self.alive = False

    def allDo(self):
        self.stream1 = Thread(target=self.move_snake())
        self.stream2 = Thread(target=self.l1teleport())

        self.stream1.start()
        self.stream2.start()

        self.stream1.join()
        self.stream2.join()

    def l1teleport(self):
        if self.btn[-1].x() + self.a > 299:
            self.openLeb()
            self.tmr.stop()
            self.a = 10
            self.b = 0
            self.saveScore()
            self.alive = False
        if self.btn[-1].y() + self.b > 299:
            self.openLeb()
            self.tmr.stop()
            self.a = 10
            self.b = 0
            self.saveScore()
            self.alive = False
        if self.btn[-1].x() + self.a < 0:
            self.openLeb()
            self.tmr.stop()
            self.a = 10
            self.b = 0
            self.saveScore()
            self.alive = False
        if self.btn[-1].y() + self.b < 0:
            self.openLeb()
            self.tmr.stop()
            self.a = 10
            self.b = 0
            self.saveScore()
            self.alive = False
        else:
            self.btn[-1].move(self.btn[-1].x() + self.a, self.btn[-1].y() + self.b)

    def dot_rand(self):
        self.xt = random.randint(0, 29) * 10
        self.yt = random.randint(0, 29) * 10
        self.dotSn.move(self.xt, self.yt)
        self.fl = not self.fl

    def snake_plus(self):
        self.btn.insert(0, QPushButton(self))
        self.btn[0].resize(10, 10)
        self.btn[0].setStyleSheet(self.skinBtn.styleSheet())
        self.fl = not self.fl

    def lftSkinBtn(self):
        self.numSkin -= 1
        if self.numSkin < -1:
            self.numSkin += 4
        self.skinBtn.setStyleSheet(self.skin[self.numSkin])
        sou1()

    def rgtSkinBtn(self):
        self.numSkin += 1
        self.numSkin %= 4
        self.skinBtn.setStyleSheet(self.skin[self.numSkin])
        sou1()

    def nameChange(self):
        a = self.name.text()
        self.name.setText(a.lower())
        if len(self.name.text()) > 4 and self.name.text() != "mkoost228":
            self.name.setText(a[:4])

    def showScores(self):
        if self.scoresShowed:
            self.scoresShowed = not self.scoresShowed
            self.start_btn.show()
            self.label.show()
            self.scoreLb.show()
            self.lftBtn.show()
            self.rgtBtn.show()
            self.skinBtn.show()
            self.tp5.show()
            self.name.show()
            self.closeSC()
        else:
            self.scoresShowed = not self.scoresShowed
            self.start_btn.close()
            self.label.close()
            self.scoreLb.close()
            self.lftBtn.close()
            self.rgtBtn.close()
            self.skinBtn.close()
            self.name.close()
            self.showSC()
    def saveScore(self):
        g = True
        con = sqlite3.connect("scoreBD.sqlite3")
        cur = con.cursor()
        a = list(cur.execute(f"""SELECT * FROM scores"""))
        for i in a:
            if i[1] == self.name.text():
                g = False
                break

        if g:
            cur.execute(f"""INSERT INTO scores(player, score) VALUES("{self.name.text()}", {int(self.scoreLb.text())})""")
        else:
            cur.execute(f"""UPDATE scores SET
                        score = {int(self.scoreLb.text())}
                        WHERE (player == '{self.name.text()}') AND (score < {int(self.scoreLb.text())}) """)
        g = True
        for i in a:
            if i[1] == "mkoost228":
                cur.execute(f"""UPDATE scores SET
                                score = 9999
                                WHERE (player == 'mkoost228')""")
                g = False
                break
        if g:
            cur.execute(
                f"""INSERT INTO scores(player, score) VALUES("mkoost228", 9999)""")

        con.commit()
        con.close()

    def showSC(self):
        for i in self.btn:
            i.close()
            i.destroy()
        self.btn = []
        con = sqlite3.connect("scoreBD.sqlite3")
        cur = con.cursor()
        a = cur.execute(f"""SELECT * FROM scores""")
        a = sorted(a, key=lambda j: j[2], reverse=True)
        for i in range(len(a)):
            if i == 10:
                break
            some = str(i + 1) + ": " + "0" * (4 - len(str(a[i][2]))) + str(a[i][2]) + "  |  " + a[i][1]
            self.scores[i].setText(some)
        con.close()
        for i in range(10):
            self.scores[i].show()

    def closeSC(self):
        for i in self.scores:
            i.close()

    def clearHistorySc(self):
            con = sqlite3.connect("scoreBD.sqlite3")
            cur = con.cursor()
            cur.execute("""DELETE from scores
                        WHERE (id > -1
                        )""")
            con.commit()
            con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
