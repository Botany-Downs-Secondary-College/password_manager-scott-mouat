#password1_lucas.py
#create and display passwords for users
#Lucas Pryce, Feb 2021

print("Welcome to Password Manager!")

name = input("What is your name? ")
print("Hi {}!".format(name))



def age():
    while True:
        try:
            age= int(input("How old are you? "))
            if age <13:
                print("You must be 13 or older to create an account")
                exit()
            else:
                print("You are eligible to use Password Manager!")
                break
        except ValueError:
            print("That is not a valid age")
    
age()

def account():
    while True:
        state = input("Please enter (L) to login, (C) to create an account or (exit) to close PasswordManager: ").capitalize()
        if state == "L":
            login()
        elif state == "C":
            create()
        elif state == "exit":
            exit()
        else:
           print("That is not a valid input")
         
account()
    