import json
import time

def countQuestions(d):
    count = 0
    for key, value in d.items():
        count += 1
        if isinstance(value, dict):
            count += countQuestions(value)
    return count

def addQuestion():
    quiz["questions"][qCount+1] = input('Enter your new question: ')
    quiz["answers"][qCount+1] = input('Enter the answer for your new question')
    
def editQuestion():
    question = input('Enter the question you want to change: ')
    qInput = input('Enter your new replacement question: ')
    quiz.update({"questions": {question: qInput}})
    
    answer = input('Enter the answer to your new question: ')
    quiz.update({"answers": {question: answer}})
    
def deleteQuestion():
    question = input('Enter the question you wish to delete: ')
    
    del quiz[question]

quizName = ''
action = ''
question = ''
questionContents = ''

print("Welcome to roboman's python quiz editor!")

while action == '':
    action = input('Load File or Create New? [Load/Create]: ').lower()

if action == 'load':
    action = ''
    while quizName == '':
        quizName = input('Enter file name: ')

    try:
        with open(f"{quizName}", "r") as f:
            print(f'Accessing {quizName}')
            quiz = json.load(f)
            qCount = int(countQuestions(quiz)/2-1)
            print(f'{qCount} questions found!')
    except FileNotFoundError:
        print(f'Cannot find ./{quizName}')
        time.sleep(3)
        exit()

    print(quiz)

    while action == '':
        action = input('Would you like to add a new question, edit an existing question, or remove a question? [Add/Edit/Delete]:').lower()
    if action == 'add':
        action = ''

        addQuestion()

        action = input('Add another question? [y/N]:').lower()

        while action == 'y':
            addQuestion()
            action = action = input('Add another question? [y/N]:').lower()
        else:
            jsonContent = json.dumps(quiz, indent=4)
            with open(quizName, "w") as f:
                f.write(jsonContent)

    elif action == 'edit':
        action = ''
        
        editQuestion()
        
        action = input('Edit another question? [y/N]:').lower()
        
        while action == 'y':
            addQuestion()
            action = input('Edit another question? [y/N]:').lower()
        else:
            jsonContent = json.dumps(quiz, indent=4)
            with open(quizName, "w") as f:
                f.write(jsonContent)

    elif action == 'delete':
        action = ''
        
        deleteQuestion()
        
        action = input('Delete another question? [y/N]: ')
        
        while action == 'y':
            deleteQuestion()
            action = input('Delete another question? [y/N]: ')
        else:
            jsonContent = json.dumps(quiz, indent=4)
            with open(quizName, "w") as f:
                f.write(jsonContent)
