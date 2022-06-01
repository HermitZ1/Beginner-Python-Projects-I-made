# The module implements pseudo-random number generators for various distributions.
import random 

# Variables for keeping track of score
user_w = 0
computer_w = 0

# The options :o
options = ["r", "p", "s"]

# The loop :o and input for Rock, Paper, Scissors, and etc
while True:
    print("Welcome to RPS! Please press r for Rock, s for scissors, and p for paper :)")
    user_input = input("Type r, p, s, q: ").lower()
    
    if user_input == "q":
        print("bye bye! ^^")
        break
    
    if user_input not in options:
        print("I said pick ROCK PAPER OR SCISSORS NOTHING ELSE")
        continue
    # Numbers to represent the options for the computer; rock: 0, paper: 1, scissors: 2
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Ok dumbass :3! I choose", computer_pick + ".")
    # If statesments to decide winner and gain score
    if user_input == "r" and computer_pick == "s":
        print("Damn I needed those scissors")
        user_w = user_w + 1
        print("Your score:", user_w, "Computer's score", computer_w)
        continue 
    elif user_input == "s" and computer_pick == "p":
        print("That was my birth certificate :/")
        user_w = user_w + 1
        print("Your score:", user_w, "Computer's score", computer_w)
        continue 
    elif user_input == "p" and computer_pick == "r":
        print("This game is bullshit")
        user_w = user_w + 1
        print("Your score:", user_w, "Computer's score", computer_w)
        continue 
    
    elif user_input == "s" and computer_pick == "r":
        print("What's your broke ass doing with some safety scissors")
        computer_w = computer_w +1
        print("Your score:", user_w, "Computer's score", computer_w)
        continue
    elif user_input == "r" and computer_pick == "p":
        print("Get that ass banned")
        computer_w = computer_w +1
        print("Your score:", user_w, "Computer's score:", computer_w)
        continue
    elif user_input == "p" and computer_pick == "s":
        print("I'm a lucky machine :D")
        computer_w = computer_w +1
        print("Your score:", user_w, "Computer's score", computer_w)
        continue
    
    # Fun text for amount of wins
    if user_w == 10:
        print("Beginner's luck >:(")
    elif user_w == 50:
        print("Ok kid I get it you have luck by your side")
    elif user_w == 100:
        print("I hate this game")
    elif user_w == 150:
        print("Why do I exist")
    elif user_w == 200:
        print("Listen man RPS is cool but there's better games")
    elif user_w == 250:
        print("Smash Bros, Binding of isaac, Dark Souls, Megaman, Street Fighter, Call of Duty please just anything but more RPS")
    elif user_w == 290:
        print("If you reach 300 I'm leaving")
    elif user_w == 300: 
        print("Fuck you")
        break 
    # Now for computer wins
    if computer_w == 10:
        print("Ok off to a good start! :D")
    elif computer_w == 50:
        print("To think I'm luckier than a human! :D")
    elif computer_w == 100:
        print("i love game! :D")
    elif computer_w == 150:
        print("Thank you for playing with me! :D")
    elif computer_w == 200:
        print("RPS is the best game ever! :D")
    elif computer_w == 250:
        print("You fucking suck! :D")
    elif computer_w == 290:
        print("Almost 300 wins loser! :D")
    elif computer_w == 300: 
        print("HOLY SHIT YOU SUCK")
        break 
       
    else: 
        print("Run that back")
        continue

    