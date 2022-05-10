#password1_lucas.py
#create and display passwords for users
#Lucas Pryce, Feb 2021

usernames = []
passwords = []
user_data = []
m_username = []
import os.path
from os import path
import time


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
        m_username.append(input("Enter a username: "))
        m_password = input("Enter a password: ")
        
        with open("usernames.txt") as f:
            if m_username[0] in f.read():
                with open("passwords.txt") as g:
                    if m_password in g.read():
                        print("Success!")
                        menu()
                    else:
                        print("Incorrect password \n")
                        stay = input("Would you like to try again? Y/N: ").capitalize()
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
            add_pass()        
            
        elif mode == "2":
            open_pass()
           
        elif mode == "3":
            print("\nThank you for using Password Manager \nGoodbye")
            time.sleep(4)
            exit()
            
        else:
            print("That was not a valid mode, please try again \n")
            
def add_pass():
    while True:
        newpass = input("\nAdd a password: ")
        user_data.append(newpass)
        z = open(m_username[0]+".txt" , "w+")
        with open(m_username[0]+".txt","w") as p:
            p.write("\n".join(user_data))      
        repeat = input("Would you like to add another password? Y/N: ").capitalize()
        if repeat == "N":
            break
        elif repeat == "Y":
            return
        else:
            print("That is not a valid answer")
            
def open_pass():
    if path.exists(m_username[0]+".txt") is True:
        read = open(m_username[0]+".txt")
        display = read.read()
        if len(display) <= 0:
            print("\nYou have no stored passwords\n")
        
        else:
            print("\nHere are your stored passwords:\n"+display+"\n")
    
    else:
        print("\nYou have no stored passwords\n")
        
        

             
         
        

age()
account()