import json

def countQuestions(d):
    count = 0
    for key, value in d.items():
        count += 1
        if isinstance(value, dict):
            count += countQuestions(value)
    return count

quizFile = ''

print("Welcome to roboman's python quiz engine!")

while quizFile == '':
    quizFile = input('Enter the name of your quiz library JSON file: ')

try:
    with open(quizFile, "r") as f:
        print(f'accessing {quizFile}')
        quiz = json.load(f)
except FileNotFoundError:
    print(f'Cannot find ./{quizFile}')

try:
    totalQuestions = int(countQuestions(quiz)/2)
    for q in range (0, totalQuestions):
        try:
            qRef = quiz["questions"][str(q+1)]
            aRef = quiz["answers"][str(q+1)]
        except KeyError:
            print('End of Quiz!')
            break
        answer = ''
        while (answer == '') and (aRef != ''):
            answer = input(f'Question {q + 1}: {qRef} ').lower()
            if answer != aRef:
                answer = ''
                print('Sorry, try again\n')
            else:
                print('Correct!\n')
except NameError:
    print('Ending script!')
