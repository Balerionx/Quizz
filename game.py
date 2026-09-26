import random

def run_quiz(quiz):
    
    random.shuffle(quiz)
    
    score = 0

    for question in quiz:
        correct_answer = question[question["ANSWER"]]
        answers = [question["A"], question["B"], question["C"], question["D"]]
        random.shuffle(answers)
        question["A"] = answers[0]
        question["B"] = answers[1]
        question["C"] = answers[2]
        question["D"] = answers[3]

        letters = ["A", "B", "C", "D"]

        for index, letter in enumerate(letters):
            question[letter] = answers[index]

        print(question["QUESTION"])
        print("A)", question["A"])
        print("B)", question["B"])
        print("C)", question["C"])
        print("D)", question["D"])  

        user_answer = input("Your answer: ").upper().strip()
        while user_answer not in ["A", "B", "C", "D"]:
            print("Invalid input. Please enter A, B, C, or D.")
            user_answer = input(f"{question['QUESTION']} (A/B/C/D): ").upper().strip()
        if question[user_answer] == correct_answer:
            print("Correct! 🎉")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", correct_answer)        

    return score


