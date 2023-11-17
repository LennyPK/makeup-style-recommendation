import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from collections import Counter

from quizData import *
from AdditionalClasses import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__()

        self.setWindowTitle("The Makeup Guide")
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(300, 300, 800, 800)
        self.setFixedSize(800,800)

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
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.button.setFixedWidth(200)
        self.button.setStyleSheet("padding: 5px 20px 5px 20px;")
        self.button.clicked.connect(self.start_Quiz_UI)

        # Progress of quiz
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, len(self.questions))
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setFixedWidth(550)

        self.layout.addWidget(icon_label, 0, 0, QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.label, 1, 0)
        self.layout.addWidget(self.button, 2, 0, QtCore.Qt.AlignCenter)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        
    def start_Quiz_UI(self):
        # Remove the existing widgets from the layout
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        # Display Question Image
        question_image = QLabel()
        question_pixmap = QPixmap(f'QuestionImages/q{self.current_question_index + 1}.jpg')
        question_scaled_pixmap = question_pixmap.scaledToHeight(250)
        question_image.setPixmap(question_scaled_pixmap)
        question_image.setAlignment(QtCore.Qt.AlignCenter)  

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
            
        self.layout.addWidget(question_image, 0, 0, QtCore.Qt.AlignCenter)
        self.layout.addWidget(question_label, 1, 0, QtCore.Qt.AlignCenter)
        self.layout.addWidget(options_container, 2, 0, QtCore.Qt.AlignCenter)
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
            self.display_Answers_UI() # Display results when the user has finished the quiz

    def display_Answers_UI(self):
        # Remove the existing widgets from the layout
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

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

        # Your Results Label
        your_answers_label = QLabel("Your Answers!")
        your_answers_label.setFont(QFont('Segoe UI', 20, 50, italic=True))
        your_answers_label.setAlignment(QtCore.Qt.AlignCenter)

        # Display Results button for quiz
        results_button = QPushButton("View My Results")
        results_button.setFont(QFont('Segoe UI', 15))
        results_button.setFixedWidth(300)
        results_button.setStyleSheet("padding: 5px 20px 5px 20px;")
        results_button.clicked.connect(self.display_Category_UI)
        
        # Create a scroll area and set the answers container as its widget
        scroll_area = QScrollArea()
        scroll_area.setWidget(answers_container)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(600)
        scroll_area.setFixedWidth(550)
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")

        minimal_vertical_scroll_bar = MinimalScrollBar(QtCore.Qt.Vertical, scroll_area)
        scroll_area.setVerticalScrollBar(minimal_vertical_scroll_bar)

        minimal_horizontal_scroll_bar = MinimalScrollBar(QtCore.Qt.Horizontal, scroll_area)
        scroll_area.setHorizontalScrollBar(minimal_horizontal_scroll_bar)
        minimal_vertical_scroll_bar.setSingleStep(7)

        # Connect the hover events to show or hide the scroll bars
        scroll_area.enterEvent = lambda event: scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll_area.leaveEvent = lambda event: scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.layout.addWidget(your_answers_label, 0, 0, QtCore.Qt.AlignCenter)
        self.layout.addWidget(scroll_area, 1, 0, QtCore.Qt.AlignCenter)
        self.layout.addWidget(results_button, 2, 0, QtCore.Qt.AlignCenter)

    def display_Category_UI(self):
        # Remove the existing widgets from the layout
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

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

        # Display Category Images
        category_img_layout = QHBoxLayout()

        category_img_one = QLabel()
        cat_img_one_pixmap = CircularImageCutter(f'CategoryImages/{default_category}1.jpg', 200)
        scaled_img_one_pixmap = cat_img_one_pixmap.create_circular_pixmap()
        category_img_one.setPixmap(scaled_img_one_pixmap)
        category_img_one.setAlignment(QtCore.Qt.AlignRight) 

        category_img_two = QLabel()
        cat_img_two_pixmap = CircularImageCutter(f'CategoryImages/{default_category}2.jpg', 200)
        scaled_img_two_pixmap = cat_img_two_pixmap.create_circular_pixmap()
        category_img_two.setPixmap(scaled_img_two_pixmap)
        category_img_two.setAlignment(QtCore.Qt.AlignLeft)

        # Add the images to the horizontal layout
        category_img_layout.addWidget(category_img_one)
        category_img_layout.addWidget(category_img_two)

        # Create a container widget for the horizontal layout
        category_img_container = QWidget()
        category_img_container.setLayout(category_img_layout)

        # Display category description
        description_label = QLabel(descriptions.get(default_category, "No description available."))
        description_label.setFont(QFont('Segoe UI', 12, italic=True))
        description_label.setWordWrap(True)
        description_label.setAlignment(QtCore.Qt.AlignCenter)

        # Display Category Archetypes
        archetype_image = QLabel()
        archetype_pixmap = QPixmap(f'CategoryArchetypes/{default_category}.png')
        scaled_archetype_pixmap = archetype_pixmap.scaledToHeight(350)
        archetype_image.setPixmap(scaled_archetype_pixmap)
        archetype_image.setAlignment(QtCore.Qt.AlignCenter)      

        # Push button to start quiz
        retake_button = QPushButton("Retake Quiz")
        retake_button.setFont(QFont('Segoe UI', 15))
        retake_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        retake_button.setFixedWidth(200)
        retake_button.setStyleSheet("padding: 5px 20px 5px 20px;")
        retake_button.clicked.connect(self.start_Quiz_UI)

        self.user_responses = []
 
        self.layout.addWidget(category_label, 0, 0, QtCore.Qt.AlignCenter)
        self.layout.addWidget(category_img_container, 1, 0, QtCore.Qt.AlignCenter)
        self.layout.addWidget(description_label, 2, 0, QtCore.Qt.AlignCenter)
        self.layout.addWidget(archetype_image, 3, 0, QtCore.Qt.AlignCenter)
        self.layout.addWidget(retake_button, 4, 0, QtCore.Qt.AlignCenter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())