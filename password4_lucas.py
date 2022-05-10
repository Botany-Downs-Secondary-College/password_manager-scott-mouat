#password1_lucas.py
#create and display passwords for users
#Lucas Pryce, Feb 2021

usernames = []
passwords = []

with open('usernames.txt','r') as f:
    usernames = f.readline()
    
with open('passwords.txt','r') as f:
    passwords = f.readline()    



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
         
    
def login():
    while True:
        m_username = input("Enter a username: ")
        m_password = input("Enter a password: ")
        
        with open("usernames.txt") as f:
            if m_username in f.read():
                with open("passwords.txt") as g:
                    if m_password in g.read():
                        print("Success!")
                        menu()
                    else:
                        print("Incorrect password")
            else:
                print("That account does not exist")
        
def create():
    c_username = input("Enter a username: ")
    c_password = input("Enter a password (Must have at least 8 characters and 1 number): ")
    b = open("usernames.txt", "a")
    b.write(c_username + " \n")
    b = open("usernames.txt", "r")
    b.close()
    d = open("passwords.txt", "a")
    d.write(c_password + " \n")
    d = open("passwords.txt", "r")
    d.close()    
    print("Account creation successful! Please reload PasswordManager to login")
    exit()
    
age()
account()