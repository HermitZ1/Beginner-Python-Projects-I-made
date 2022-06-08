# user gsts to choose their name
name = input("What is your name? ")
print("Welcome ", name," your legendary tale starts now!" )
# First part of the adventure :D
answer = input("A talking dog walks up to you and asks if you would like to hear a joke, do you hear his attempt at humor? ").lower()

# You hear the dog's joke (The right answer)
if answer == "yes":
    answer = input('The dog tells the joke: "Ok so why did the chicken cross the road?" and you respond... ').lower()
    
    if answer ==  'to eat them':
        print("'Yeah! Anyways let's go get some Taco Bell I'm hungry!'")
    elif answer == "I don't know": 
        print("'So I can eat em! Now buy me some Taco Bell I'm starving!'")
    else:
        print("The dog is angered and bites your foot. You scream.")

#You say no (Wrong answer)
elif answer == "no":
    print("You anger the dog, and he decides to bite your hand. You scream in pain and agony.")

# You say otherwise
else:
    print("Not a choice :(")

