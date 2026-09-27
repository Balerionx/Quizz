from pathlib import Path
from quizz import load_questions
from game import run_quiz

def main():
    print("Welcome to the Quiz Game!")
    print("Please select a subject from the list below:")

    questions_folder = Path(__file__).parent / "questions"
    quiz_files = sorted(questions_folder.glob("*.txt"))

    if not quiz_files:
        print("No quiz files found in the 'questions' folder.")
        return
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
    if not quiz:
        print("No questions found in this quiz.")
        return

    final_score = run_quiz(quiz)
    percentage = (final_score / len(quiz)) * 100
    print(f"Your score is: {final_score}/{len(quiz)} ({round(percentage)}%)")

if __name__ == "__main__":
    main()