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
    qCount = int(countQuestions(quiz)/2-1)
    quiz["questions"][qCount+1] = input('Enter your new question: ')
    quiz["answers"][qCount+1] = input('Enter the answer for your new question: ').lower()
    
def editQuestion():
    question = int(input('Enter the question you want to change: '))
    qInput = input('Enter your new replacement question: ')
    del quiz["questions"][question]
    quiz["questions"][question] = qInput
    
    answer = input('Enter the answer to your new question: ').lower()
    del quiz["answers"][question]
    quiz["answers"][question] = answer
    
def deleteQuestion():
    question = input('Enter the question you wish to delete: ')
    
    del quiz["questions"][question]
    del quiz["answers"][question]

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
        with open(quizName, "r") as f:
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
        action = input('Would you like to add a new question, edit an existing question, or remove a question? [Add/Edit/Delete]: ').lower()
    if action == 'add':
        action = ''

        addQuestion()

        action = input('Add another question? [y/N]: ').lower()

        while action == 'y':
            addQuestion()
            action = action = input('Add another question? [y/N]: ').lower()
        else:
            jsonContent = json.dumps(quiz, indent=4)
            with open(quizName, "w") as f:
                f.write(jsonContent)

    elif action == 'edit':
        action = ''
        
        editQuestion()
        
        action = input('Edit another question? [y/N]: ').lower()
        
        while action == 'y':
            addQuestion()
            action = input('Edit another question? [y/N]: ').lower()
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

elif action == 'create':
    action = 'yes'

    quiz = {'questions': {}, 'answers': {}}

    while quizName == '':
        quizName = input('Enter the name of your new quiz: ')
    
    while action != 'n':
         addQuestion()
         action = input('Add another question? [Y/n]: ')

    else:
        action = ''

        while action == '':
            action = input('Would you like to add a new question, edit an existing question, remove a question, or none of the above? [Add/Edit/Delete/Quit]: ').lower()

        if action == 'add':
            action = ''

            addQuestion()

            action = input('Add another question? [y/N]: ').lower()

            while action == 'y':
                addQuestion()
                action = action = input('Add another question? [y/N]: ').lower()
            else:
                jsonContent = json.dumps(quiz, indent=4)
                with open(f"{quizName}.json", "w") as f:
                    f.write(jsonContent)

        elif action == 'edit':
            action = ''
            
            editQuestion()
            
            action = input('Edit another question? [y/N]: ').lower()
            
            while action == 'y':
                addQuestion()
                action = input('Edit another question? [y/N]: ').lower()
            else:
                jsonContent = json.dumps(quiz, indent=4)
                with open(f"{quizName}.json", "w") as f:
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
                with open(f"{quizName}.json", "w") as f:
                    f.write(jsonContent)

        else:
            jsonContent = json.dumps(quiz, indent=4)
            with open(f"{quizName}.json", "w") as f:
                f.write(jsonContent)
