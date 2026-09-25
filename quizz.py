def load_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
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

    return quiz