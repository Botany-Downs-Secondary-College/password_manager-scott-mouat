#Passwork Manager.py
#23/02 2021
#Trisan Huynh

import os
import time
import random
import string

usernames_passwords = []
existing_users = ["Trisan"]
existing_users_passwords = ["Password"]

def cls():
    os.system('cls')


def signin():
    desired_function = input("Would you like to sign in to an existing (e) account or create a new (n) account? Please enter 'e' or 'n': ").strip().lower()
    if desired_function == "e":
        account_login()
    elif desired_function == "n":
        cls()
        new_account()
    elif desired_function != "e" or "n":
        print("Please enter either 'e' or 'n'.")
        time.sleep(1)
        cls()
        signin()

def account_login():
    print("Welcome to the login portal.")
    time.sleep(1)
    entered_username = input("Please enter your username: ").strip()
    if entered_username in existing_users:
        print("Welcome, {}.".format(entered_username))
        while True:
            entered_password = input("Please enter your password: ").strip()
            if entered_password in existing_users_passwords:
                print("Login successful.")
                time.sleep(1)
                cls()
                menu()
            elif entered_password == "escape":
                cls()
                signin()
            else:
                print("Incorrect password. Passwords are case sensitive.")
                time.sleep(1)
                print("If you have forgotten your password and wish to exit, type 'escape' as the password.")
                time.sleep(2)
                cls()

    elif entered_username not in existing_users:
        print("That username does not exist. Please try again.")
        time.sleep(1)
        cls()
        account_login()

def intro():
    print("Hello. This program is used to securely store and retreive passwords.")
    time.sleep(1)
    cls()
    name = input("What is your name?: ").strip().capitalize()
    while True:
        try:
            age = float(input("What is your age, {}?: ".format(name)))
            break
        except ValueError:
            print("Please enter a number.")

    time.sleep(1)
    if age <= 13:
        cls()
        print("You do not possess the necessary number of years in order to utilise this software.")
        print("Please return when you are older than the age of 13.")
        time.sleep(4)
        exit()
    
    cls()
    signin()

def menu():
    cls()
    while True:
        try:
            mode = input("""Choose a mode by entering a number:
1: View passwords
2: Edit/add passwords
3: Sign out and exit
Number : """)
            break
        except ValueError:
            print("That is not a valid choice. Please try again.")
    
    if mode == "1":
        view_passwords()
    elif mode == "2":
        edit_passwords()
    elif mode == "3":
        usernames_passwords.clear()
        print("You have been signed out.")
        print("Thanks for using this tool.")
        time.sleep(2)
        exit()
        
def view_passwords():
    print("You currently have {} logins saved in your account.".format(len(usernames_passwords)))
    for another_login_set in usernames_passwords:
        print("• " + another_login_set)
    
    idk_nothing_important = input("Press any key to return to the menu.")
    if idk_nothing_important != 8397219317293871238:
        cls()
        menu()

def new_account():
    print("Please enter a username for your account. ")
    time.sleep(1)
    new_user_username = input("It can contain letters, numbers and/or symbols: ").strip()
    if new_user_username in existing_users:
        print("Sorry, but the username {} is already taken. Try adding numbers or symbols.".format(new_user_username))
        time.sleep(1)
        cls()
        new_account()
    
    existing_users.append(new_user_username)
    cls()

    print("Please enter a password for your account.")
    time.sleep(1)
    print("A strong password will contain a mixture of upper and lower case letters, numbers, and symbols, and should be something you can remember.")
    time.sleep(1)
    new_user_password_check_1 = input("Enter your password. Keep in mind that it is case sensitive: ").strip()
    new_user_password_check_2 = input("Please confirm your password: ").strip()

    if new_user_password_check_2 != new_user_password_check_1:
        print("Sorry, but the passwords did not match. Please try again.")
        time.sleep(1)
        new_account()
        cls()
    
    existing_users_passwords.append(new_user_password_check_2)
    cls()
    account_login()

intro()