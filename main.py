from pathlib import Path
from quizz import load_questions

questions_folder = Path(__file__).parent / "questions"
geography_file = questions_folder / "geography.txt"

quiz = load_questions(geography_file)

def run_quiz(quiz):
    score = 0

    for question in quiz:
        print(question["QUESTION"])
        print("A)", question["A"])
        print("B)", question["B"])
        print("C)", question["C"])
        print("D)", question["D"])

        user_answer = input("Your answer: ").upper().strip()
        while user_answer not in ["A", "B", "C", "D"]:
            print("Invalid input. Please enter A, B, C, or D.")
            user_answer = input(f"{question['QUESTION']} (A/B/C/D): ").upper().strip()
        if user_answer == question["ANSWER"]:
            print("Correct! 🎉")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", question["ANSWER"])        

    return score
final_score = run_quiz(quiz)
print(f"Your score is: {final_score}/{len(quiz)}")