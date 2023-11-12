import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

from quizData import questions, options

class Home_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_UI()

    def setup_UI(self, parent=None):
        '''Text on the Main Window'''
        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        
        self.label = QLabel("Take the quiz and find out which makeup style best suits you")
        self.label.setFont(QFont('Arial', 20))

        self.button = QPushButton("Take Quiz")
        self.button.setFont(QFont('Arial', 15))
        self.button.setStyleSheet("background-color: #ffd6d8;") # fix color of "take quiz" button
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.button.setStyleSheet("padding: 5px 20px 5px 20px;")
        self.button.clicked.connect(parent.start_Quiz_UI)

        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 1, 0, QtCore.Qt.AlignCenter)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(self.layout)

class Questionnaire_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_UI()

    def setup_UI(self, parent=None):
        self.layout = QGridLayout()

        self.label = QLabel("Quiz Screen")
        self.label.setFont(QFont('Arial', 20))

        self.layout.addWidget(self.label,0,0)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__()

        # self.setWindowTitle("Makeup Recommendation")
        self.setWindowIcon(QIcon('icon.png'))

        grid = QGridLayout()
        self.setLayout(grid)
        self.setGeometry(300, 300, 600, 600)

        '''centering the window'''
        win_info = self.frameGeometry()
        monitor_info = QDesktopWidget().availableGeometry().center()
        win_info.moveCenter(monitor_info)
        self.move(win_info.topLeft())

        self.questions = questions
        self.options = options

        self.start_Home_UI()

    def start_Home_UI(self):
        self.Home = Home_UI()
        self.setWindowTitle("Makeup Recommendation")
        self.setCentralWidget(self.Home)
        self.show()

    def start_Quiz_UI(self):
        self.Questionnaire = Questionnaire_UI()
        self.setCentralWidget(self.Questionnaire)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())