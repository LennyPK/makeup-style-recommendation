'''
Sample Code of how basic quiz is meant to work
Collects all the responses and prints the responses in the terminal
'''

from quizData import questions, options

user_responses = []

def get_user_choice(prompt, valid_choices):
    # user input validation
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid choice. Please select a valid option.")

for i in range(15):
    # cycles through questions
    print(questions[i])
    for j, option in enumerate(options[i]):
        # cycles through all options for this question[i]
        print(f"{chr(65 + j)}) {option}")
    user_input = get_user_choice("Your answer (A/B/C/D/E/F/G/H): ", valid_choices=list("ABCDEFGH"))
    user_responses.append(user_input)

print("\nYour responses:")
for i in range(15):
    print(f"\n{questions[i]}")
    print(f"Your response: {options[i][ord(user_responses[i]) - ord('A')]}")
    
print("\n")
print(user_responses)