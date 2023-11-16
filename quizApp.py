import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from collections import Counter

from quizData import questions, options
from modifiedScroll import MinimalScrollBar

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__()

        self.setWindowTitle("The Makeup Guide")
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(300, 300, 600, 600)

        '''Center the window'''
        win_info = self.frameGeometry()
        monitor_info = QDesktopWidget().availableGeometry().center()
        win_info.moveCenter(monitor_info)
        self.move(win_info.topLeft())

        self.questions = questions
        self.options = options
        self.current_question_index = 0  # Initialize current question index

        self.user_responses = []

        # Define a dictionary to map user responses to fashion categories and weights
        self.category_weights = {
            'A': ('Ingenue', 13),
            'B': ('Elegant', 13),
            'C': ('Romantic', 13),
            'D': ('Gamine', 13),
            'E': ('Natural', 13),
            'F': ('Modern', 13),
            'G': ('Classic', 13),
            'H': ('Dramatic', 13)
        }
        
        '''set central widget'''
        central_widget = QWidget()
        self.setCentralWidget(central_widget)        

        '''Text on the Main Window'''
        self.layout = QGridLayout(central_widget)
        self.layout.setSpacing(10)
        
        # Add an image (icon) above the label
        icon_label = QLabel()
        original_pixmap = QPixmap('icon.png')
        scaled_pixmap = original_pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)  # Shrink image while maintaining aspect ratio
        icon_label.setPixmap(scaled_pixmap)
        icon_label.setFixedSize(300, 300)  # Set size dimensions
        icon_label.setAlignment(QtCore.Qt.AlignCenter)

        # Description of quiz
        self.label = QLabel("Take the quiz and find out which makeup style best suits you")
        self.label.setFont(QFont('Segoe UI', 17))

        # Push button to start quiz
        self.button = QPushButton("Take Quiz")
        self.button.setFont(QFont('Segoe UI', 15))
        self.button.setStyleSheet("background-color: red")  # Change the background color to red and text color to white
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.button.setFixedWidth(200)
        self.button.setStyleSheet("padding: 5px 20px 5px 20px;")
        self.button.clicked.connect(self.start_Quiz_UI)

        # Progress of quiz
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, len(self.questions))
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)

        self.layout.addWidget(icon_label, 0, 0, QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.label, 1, 0)
        self.layout.addWidget(self.button, 2, 0, QtCore.Qt.AlignCenter)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        
    def start_Quiz_UI(self):
        # Remove the existing widgets from the layout
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        # Display current question
        question_label = QLabel(self.questions[self.current_question_index])
        question_label.setFont(QFont('Segoe UI', 14))

        # Create a container widget to hold the options layout
        options_container = QWidget()
        options_layout = QVBoxLayout(options_container)

        # Display options
        for j, option in enumerate(self.options[self.current_question_index]):
            option_button = QPushButton(option)
            option_button.setFont(QFont('Segoe UI', 12))
            option_button.clicked.connect(lambda _, j=j: self.handle_option_click(j))
            option_button.setFixedWidth(500)  # Set fixed width
            options_layout.addWidget(option_button)
            
        self.layout.addWidget(question_label, 0, 0, alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(options_container, 1, 0, alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.progress_bar)

    def handle_option_click(self, option_index):
        print(f"Question {self.current_question_index + 1}, Option {chr(65 + option_index)} clicked.")
        self.current_question_index += 1  # Move to the next question
        self.user_responses.append(chr(65 + option_index))
        self.progress_bar.setValue(self.current_question_index)

        if self.current_question_index < len(self.questions):
            self.start_Quiz_UI()  # Display the next question
        else:
            print("Quiz completed.")
            print(self.user_responses)
            self.current_question_index = 0
            self.progress_bar.setValue(0)
            self.display_Results_UI() # Display results when the user has finished the quiz

    def display_Results_UI(self):
        # Remove the existing widgets from the layout
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        '''image of style'''


        '''Calculate Style'''
        # Count user responses
        response_counts = Counter(self.user_responses)
        majority_response, majority_count = response_counts.most_common(1)[0]

        # Determine the default response
        if len(response_counts) == 4:
            # If the user picked an even distribution of letters, default to the second to last letter
            default_response = sorted(response_counts.keys())[-2]
        else:
            # If the user picked a random distribution of letters, default to the majority letter
            default_response = majority_response

        default_category, default_weight = self.category_weights[default_response]

        '''Display Styles'''
        category_label = QLabel(default_category)
        category_label.setFont(QFont('Segoe UI', 20, 75))

        # Create a container widget to hold the questions and answers layout
        answers_container = QWidget()
        answers_layout = QVBoxLayout(answers_container)

        # Display current question
        for i in range(15):
            question = self.questions[i]
            user_response = self.user_responses[i]

            # Create a new widget to hold the QnA_layout for each question
            QnA_widget = QWidget()
            QnA_layout = QVBoxLayout(QnA_widget)

            question_label = QLabel(str(i+1) + ") " + question)
            question_label.setFont(QFont('Segoe UI', 11))

            answer_label = QLabel(self.options[i][ord(user_response) - ord('A')])
            answer_label.setFont(QFont('Segoe UI', 10, QFont.Bold))

            QnA_layout.addWidget(question_label)
            QnA_layout.addWidget(answer_label)
            QnA_layout.setSpacing(0)

            # Add the QnA_widget to answers_layout
            answers_layout.addWidget(QnA_widget)
            answers_layout.setSpacing(0)

        # Display retake button for quiz
        retake_button = QPushButton("Retake Quiz")
        retake_button.setFont(QFont('Segoe UI', 15))
        retake_button.setFixedWidth(200)
        retake_button.setStyleSheet("padding: 5px 20px 5px 20px;")
        retake_button.clicked.connect(self.start_Quiz_UI)
        
        # Create a scroll area and set the answers container as its widget
        scroll_area = QScrollArea()
        scroll_area.setWidget(answers_container)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(450)
        scroll_area.setFixedWidth(550)
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")

        # Enable smooth scrolling using QScroller
        # scroller = QScroller.scroller(scroll_area.viewport())
        # scroller.setScrollerProperties(QScrollerProperties(QScroller.ScrollMode(QScroller.ScrollMode.Smooth)))

        minimal_vertical_scroll_bar = MinimalScrollBar(QtCore.Qt.Vertical, scroll_area)
        scroll_area.setVerticalScrollBar(minimal_vertical_scroll_bar)

        minimal_horizontal_scroll_bar = MinimalScrollBar(QtCore.Qt.Horizontal, scroll_area)
        scroll_area.setHorizontalScrollBar(minimal_horizontal_scroll_bar)
        minimal_vertical_scroll_bar.setSingleStep(7)

        # Connect the hover events to show or hide the scroll bars
        scroll_area.enterEvent = lambda event: scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll_area.leaveEvent = lambda event: scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.layout.addWidget(category_label, 0, 0, QtCore.Qt.AlignCenter)
        self.layout.addWidget(scroll_area, 1, 0, QtCore.Qt.AlignCenter)
        self.layout.addWidget(retake_button, 2, 0, QtCore.Qt.AlignCenter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())