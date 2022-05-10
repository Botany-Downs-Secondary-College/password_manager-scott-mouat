import time
usernames_passwords = []
existing_usernames = ["Ravi"]
existing_passwords = ["ok"]

    

def menu():
    while True:
        try:
            mode = int(input("""
1: Add Passwords
2: View Passwords
3: Exit
Enter : """))
            break
        # Print an error message if there is any error
        except ValueError:
            print("Please enter a number, from 1 to 3.")
            
    # if statements which go with relevant numbers and functions
    if mode == 1:
        add_Passwords()
    
    elif mode == 2:
        view_Passwords()
        
    elif mode== 3:
        print("goodbye")
        time.sleep(1)
        # exit the code if chosen
        exit()    

def welcome():
    name = input("What is your name? : ")    
    while True:
        try:
            age = float(input("What is your age?: "))
            break
        except ValueError:                                 
            ("Please enter a number")


    if age < 13:
        print("You do not meet the age requirement to acesss this program")
        time.sleep(1)
        exit()
        




print("Hi Welcome to Password Manager")
print("You are able to store username and password details if you are 13 years or older")

welcome()
menu()
