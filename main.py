from pathlib import Path
from quizz import load_questions
from game import run_quiz

questions_folder = Path(__file__).parent / "questions"
quiz_files = sorted(questions_folder.glob("*.txt"))
for number, file in enumerate(quiz_files, start=1):
    print(number, file.stem.capitalize())

while True:
    try:
        choice = int(input("Choose a subject: "))
        if not 1 <= choice <= len(quiz_files):
            raise ValueError()
        break
    except ValueError:
        print("Invalid choice. Please enter a number corresponding to the subjects listed.")

quiz = load_questions(quiz_files[choice - 1])

final_score = run_quiz(quiz)
print(f"Your score is: {final_score}/{len(quiz)}")