#Passwork Manager.py
#23/02 2021
#Trisan Huynh

import os
import time
import random
import string

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
    entered_username = input("If at anytime you wish to exit, enter 'escape' as the username. Please enter your username: ").strip()
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
    elif entered_username == "escape":
        cls()
        signin()
    elif entered_username not in existing_users:
        print("That username does not exist. Please try again.")
        time.sleep(1)
        cls()
        account_login()

def intro():
    print("Hello. This program is used to securely store and retreive passwords.")
    time.sleep(1)
    cls()
    while True:
        try:
            age = float(input("What is your age?: "))
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
            mode = int(input("""Choose a mode by entering a number:
1: View passwords
2: Edit/add passwords
3: Sign out and exit
4: Sign out
Number : """))
            break
        except ValueError:
            print("That is not a valid choice. Please try again.")
    
    if mode == 1:
        view_passwords()
    elif mode == 2:
        edit_passwords()
    elif mode == 3:
        print("You have been signed out.")
        print("Thanks for using this tool.")
        time.sleep(2)
        exit()
    elif mode == 4:
        print("You have been signed out.")
        cls()
        signin()
    else:
        print("That is not a valid choice. Please try again.")
        cls()
        menu()

def edit_passwords():
    while True:
        password_title = input("What is the use of this login (e.g. Google): ").strip().title()
        password_username = input("What is the username/email for the login?: ").strip()
        password_password = input("What is the password for the login?: ").strip()
        cls()
        login_set = "=" + "Site: {} - Username/email: {} - Password: {}".format(password_title, password_username, password_password)
        with open ("Documents/school/Year 12/2DIP/Password Manager/secure/usernames_passwords.txt", "a+") as usernames_passwords_txt:
            usernames_passwords_txt.write(login_set)
        continue_edit_passwords = input("Do you want to add another password (Y/N)?: ").strip().lower()
        if continue_edit_passwords == "y":
            cls()
            edit_passwords()
        elif continue_edit_passwords == "n":
            cls()
            menu()
        else: 
            print("What does {} mean? Sending you to the main menu.".format(continue_edit_passwords))
            time.sleep(1)
            cls()
            menu()
   
def view_passwords():
    with open ("Documents/school/Year 12/2DIP/Password Manager/secure/usernames_passwords.txt", "r") as usernames_passwords_txt:
        usernames_passwords_list = usernames_passwords_txt.read()
        usernames_passwords_list = usernames_passwords_list.split("=")
        for another_login in usernames_passwords_list:
            print("• " + another_login)
    
    idk_nothing_important = input("Press ENTER key to return to the menu.")
    if idk_nothing_important != "8397219317293871238":
        cls()
        menu()
    elif idk_nothing_important == "8397219317293871238":
        print("Wow what a good guess!!")
        time.sleep(2)
        exit()

def new_account():
    print("Please enter a username for your account.")
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
    new_user_password_check_1 = input("Enter your password. Passwords are case sensitive. It must contain more than 8 characters: ").strip()
    if len(new_user_password_check_1) <= 7:
        print("Please enter a password that is at least 8 characters.")
        time.sleep(2)
        cls()
        new_account()
    new_user_password_check_2 = input("Please confirm your password: ").strip()

    if new_user_password_check_2 != new_user_password_check_1:
        print("Sorry, but the passwords did not match. Please try again.")
        time.sleep(1)
        new_account()
        cls()
    
    existing_users_passwords.append(new_user_password_check_2)
    cls()
    account_login()

cls()
intro()