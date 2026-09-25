from pathlib import Path

questions_folder = Path(__file__).parent / "questions"
geography_file = questions_folder / "geography.txt"

with open(geography_file, "r", encoding="utf-8") as file:
    content = file.read()

questions = content.split("\n\n")  # split the content into individual questions based on double newlines

quiz = []

for question in questions:  # iterate through each question
    if not question.strip():
        continue

    data = {}

    for line in question.splitlines():
        if not line.strip():
            continue
        key = line.split(":", 1)[0]
        value = line.split(":", 1)[1].strip()
        data[key] = value

    quiz.append(data)

for question in quiz:
    print(question["QUESTION"])
    print("A)", question["A"])
    print("B)", question["B"])
    print("C)", question["C"])
    print("D)", question["D"])