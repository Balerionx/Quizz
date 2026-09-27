# Quizz

A simple command-line study quizzer written in Python.

I created this project as a Python learning exercise and as a study tool
for my kids.

## Features

- Automatically discovers quiz subjects from the `questions` folder
- Multiple-choice questions
- Randomizes question order
- Randomizes answer order
- Validates user input
- Tracks and displays the final score
- New subjects can be added without changing the Python code

## Project Structure
```
quizz/
├── main.py
├── game.py
├── quizz.py
└── questions/
    └── geography.txt
    └── biology.txt
    └── history.txt
```
## Running the Program

Run:

```bash
python main.py
