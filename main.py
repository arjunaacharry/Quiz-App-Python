def ask_question(question, options, correct_answer):
    for attempt in range(3):
        print(f"{question}")
        for option in options:
            print(option)

        user_answer = input(f"Your answer (Attempt {attempt + 1}, enter the letter corresponding to your choice): ").upper()

        if user_answer == correct_answer:
            print("Correct! You earned 1 mark.")
            return 1

        print("Incorrect. Try again.")

    print(f"Sorry, you've used all 3 attempts. The correct answer is {correct_answer}.")
    return 0

def quiz_game():
    total_marks = 0

    # Question 1
    total_marks += ask_question("What is the capital of France?", ["A. Berlin", "B. Paris", "C. Rome", "D. Madrid"], "B")

    # Question 2
    total_marks += ask_question("What is the largest mammal?", ["A. Elephant", "B. Giraffe", "C. Blue Whale", "D. Lion"], "C")

    # Question 3
    total_marks += ask_question("Which planet is known as the Red Planet?", ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"], "A")

    print(f"\nYour total score: {total_marks} out of 3.")

if __name__ == "__main__":
    quiz_game()
