#password_manager.py
#Create and display passwords
#Scott Mouat, 22 Feb


def check(name, age):
    print("Hello, {}".format(name))
    if age < 13:
        print("You are not eligible to create an account")
        exit()
    else:
        login()
        
def login():
    while True:
        current = input("Are you an existing member(E) or do you need a new account(N)? ")
        if current == "E":
            existing()
        elif current == "N":
            new_person()
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
    
            


            
    
    
      
    
existing_u = ["Trisanman", "Scottman"]
existing_p = ["Coolguy123", "Coolerguy123"]
passwords_stored = []
name = input("Hello, what is your name? ")
age = int(input("How old are you? "))
check(name, age)