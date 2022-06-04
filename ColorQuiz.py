# The main function in Python acts as the point of execution for any program.
from tkinter.messagebox import askquestion


def main():
    score = 0
    print("This is main")
    answerKey = {'apple':'red','clouds':'white','water':'blue','lemon':'yellow'}

    for a, b in answerKey.items():
        print('')
        score = askQuestion(a, b, score)

    print("Correct! you got" + str(score) + "points!")

def askQuestion(question, answer, i):
        player_answer = input(question + "\n")
        if player_answer.lower() == answer: 
            print("Correct!")
            return i + 1
        else:
            print(f'No stupid! the correct answer was: "{answer}"')
            return 0
if __name__ == "__main__": 
    main()
   