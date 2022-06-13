# Functions to store blocks of code and make things more organized.
# .rstrip() removes the \n
# .split can be used to split words whenever the assigned character is mentioned (in this example it's "-")
def view():
    with open('password.txt', 'r') as f: 
        for line in f.readlines():
            data = line.rstrip()
            website, name, pwd = data.split("-")
            print("Site:", website, "Username:", name, "Password:", pwd)

def add():
    website = input('Site name: ')
    name = input('Username: ')
    pwd = input('Password: ')
# Open a text file for passwords. The with command will close the file automatically.
# There are different modes: 'w' create a new file or override an existing file, 'r' is read only, and 'a' allows you to add to a file or create one if said file doesn't exist.
    with open('password.txt', 'a') as f:
        f.write(website + "-" + name + "-" + pwd + "\n")

#The loop :o
while True:
# Ask user to add a new password or view an existing one?
        mode = input("Add a new password or view the password bank (view, add, q to quit)? ").lower()

        if mode == "q":
            break
        elif mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid input")
            continue