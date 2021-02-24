#password_manager.py
#Create and display passwords
#Scott Mouat, 22 Feb


def check(name):
    print("Hello, {}".format(name))
    while True:
        try:
            age = int(input("How old are you? "))
            if age < 13:
                print("You are not eligible to create an account")
                exit()
            elif age > 120:
                print("That is not a valid age")
            else:   
                print("You are eligible to enter")
                login()
        except ValueError:
            print("Please enter a valid number")
        
def login():
    while True:
        current = input("Are you an existing member(E) or do you need a new account(N) or do you want to exit(Exit)? ")
        current = current.capitalize()
        if current == "E":
            existing()
        elif current == "N":
            new_person()
        elif current == "Exit":
            print("You have successfully exited the program")
            exit()
        else:
            print("That is not a valid membership answer")
            print("Please make sure to print E or N")
            
            
def existing():
    try_again = "Y"
    while try_again == "Y":
        username_e = input("What is your username?")
        password_e = input("What is your password?")
        if username_e in existing_u and password_e in existing_p:
            print("You have logged in as {}".format(username_e))
            x = menu()
            choose_mode(x)
        else:
            print("That is incorrect")
            try_again = input("Woukd you like to try again? (Y/N) ")
            
def new_person():
    username_n = input("What would you like your username to be?")
    existing_u.append(username_n)
    password_n = input("What would you like your password (8 characters, at least 1 number) to be? ")
    existing_p.append(password_n)
    print("Signup successful")
    x = menu()
    choose_mode(x)
    
            
def menu():
    print("1: Add a new password")
    print("2: View Passwords")
    print("3: Logout")
    print("4: Logout and Exit")
    while True:
        try:
            mode = int(input("What would you like to do? "))
            if mode > 4 or mode < 0:
                ValueError
            elif mode == 4:
                print("You have exited the program")
                exit()
            
            else:
                return mode
        except ValueError:
            print("Please enter a valid number corresponding to a mode")
            
    
def mode_one():
    more_passwords = "Y" 
    while more_passwords == "Y" or more_passwords == "y":
        new_password = input("What new password and source would you like to add? Or would you like to exit? ")
        new_password = new_password.capitalize()
        if new_password == "Exit":
            x = menu()
            choose_mode(x)            
        else:
            passwords_stored.append(new_password)
            more_passwords = input("Would you like to add more passwords?(Y/N) ")
            
    x = menu()
    choose_mode(x)

            
def mode_two():
    print("Here are your passwords")
    print(*passwords_stored, sep = "\n")
    x = menu()
    choose_mode(x)
    
def mode_three():
    passwords_stored.clear()
    print("You have successfully logged out")
    login()
    
    
    

def choose_mode(x):
    if x == 1:
        mode_one()
    elif x == 2:
        mode_two()
    else:
        mode_three()


            
    
    
      
    
existing_u = ["Trisanman", "Scottman"]
existing_p = ["Coolguy123", "Coolerguy123"]
passwords_stored = []
name = input("Hello, what is your name? ")
check(name)