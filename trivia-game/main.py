#
# Jordan Williford
# 2/15/2025
# Trivia Game Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 
class Question:

    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):

        self.question = question

        self.answer1 = answer1

        self.answer2 = answer2

        self.answer3 = answer3

        self.answer4 = answer4

        self.correct_answer = correct_answer

    def display_question(self):

        print(self.question)

        print("1. " + self.answer1)

        print("2. " + self.answer2)

        print("3. " + self.answer3)

        print("4. " + self.answer4)
# Sample trivia questions

questions = [

    Question("What is the capital of France?", "London", "Berlin", "Paris", "Rome", 3),

    Question("Who painted the Mona Lisa?", "Michelangelo", "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", 2),

    # Add more questions here...
]
def play_trivia():
    player1_score = 0
    player2_score = 0

    print("Welcome to Trivia Game!")



    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}:")
        question.display_question()

        if (i % 2) == 0:  # Player 1's turn
            player = "Player 1"
        else:  # Player 2's turn
            player = "Player 2"
        answer = input(f"{player}, enter your answer (1-4): ")

        

        if int(answer) == question.correct_answer:
            print(f"{player} - Correct!\n")

            if player == "Player 1":
                player1_score += 1

            else:
                player2_score += 1

        else:
            print(f"{player} - Incorrect!\n")

    print("\nFinal Scores:")

    print(f"Player 1: {player1_score}")

    print(f"Player 2: {player2_score}")

    if player1_score > player2_score:
        print("Player 1 wins!") 
    elif player2_score > player1_score:
        print("Player 2 wins!") 
    else:
        print("It's a tie!") 
if __name__ == "__main__":

    play_trivia() 
