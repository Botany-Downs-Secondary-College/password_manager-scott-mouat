#password1_lucas.py
#create and display passwords for users
#Lucas Pryce, Feb 2021

usernames = []
passwords = []
user_data = []

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
                        print("Incorrect password \n")
                        stay = input("Would you like to exit? Y/N: ").capitalize()
                        if stay == "Y":
                            print("Goodbye")
                            exit()                        
            else:
                print("That account does not exist \n")
                stay = input("Would you like to exit? Y/N: ").capitalize()
                if stay == "Y":
                    print("Goodbye")
                    exit()
    
        
def create():
    while True: 
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
    
def menu():
    while True:
        mode = input("Please choose a mode \n 1: Add passwords \n 2: View passwords \n 3: Exit \n Mode: ")
    
        if mode == "1":
            persistent = True
            while persistent == True:
                newpass = input("\nAdd a password: ")
                user_data.append(newpass)
                repeat = input("Would you like to add another password? Y/N: ").capitalize()
                if repeat == "N":
                    persistent == False
                    break
                elif repeat == "Y":
                    persistent == True
                else:
                    print("That is not a valid answer")
                    
                
                
            
        elif mode == "2":
            i = 0
            if i < len(user_data):
                print("\n{}\n".format(user_data))
                i += 1
            else:
                print("No passwords stored \n")
                
        elif mode == "3":
            print("\nThank you for using Password Manager \nGoodbye")
            exit()
            
        else:
            print("That was not a valid mode, please try again \n")



age()
account()