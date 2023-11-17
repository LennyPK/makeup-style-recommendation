'''
Main logic of quiz
Prints to terminal of user's best style
Weights are assigned to categories to weigh user's style based on user responses
'''

from quizData import questions, options
from collections import Counter

user_responses = []

# Define a dictionary to map user responses to fashion categories and weights
category_weights = {
    'A': ('Ingenue', 13),
    'B': ('Elegant', 13),
    'C': ('Romantic', 13),
    'D': ('Gamine', 13),
    'E': ('Natural', 13),
    'F': ('Modern', 13),
    'G': ('Classic', 13),
    'H': ('Dramatic', 13)
}

# User input validation
def get_user_choice(prompt, valid_choices):
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid choice. Please select a valid option.")

# Collect user responses
for i in range(15):
    print(questions[i])
    for j, option in enumerate(options[i]):
        print(f"{chr(65 + j)}) {option}")
    user_input = get_user_choice("Your answer (A/B/C/D/E/F/G/H): ", valid_choices=list("ABCDEFGH"))
    user_responses.append(user_input)

# Count user responses
response_counts = Counter(user_responses)
majority_response, majority_count = response_counts.most_common(1)[0]

# Determine the default response
if len(response_counts) == 4 and all(count == 3 for count in response_counts.values()):
    # If the user picked an even distribution of letters, default to the second to last letter
    default_response = sorted(response_counts.keys())[-2]
else:
    # If the user picked a random distribution of letters, default to the majority letter
    default_response = majority_response

print("\nYour responses:")
for i in range(15):
    question = questions[i]
    user_response = user_responses[i]
    category, weight = category_weights[user_response]
    
    print(f"\n{question}")
    print(f"Your response: {options[i][ord(user_response) - ord('A')]}")
    print(f"Category: {category}")
    print(f"Weight: {weight}")

# Display the default category based on user response
default_category, default_weight = category_weights[default_response]
print("\nDefault Response (Based on Distribution):")
print(f"Category: {default_category}")
print(f"Weight: {default_weight}")

print(user_responses)