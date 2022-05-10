#password1_lucas.py
#create and display passwords for users
#Lucas Pryce, Feb 2021
passwords = []

def menu():
    
    if age < 13:
        print("You must be at least 13 years of age to open an account")
        exit ()
    
    else:
        mode = input("Please choose a mode \n 1: Add passwords \n 2: View passwords \n 3: Exit \n Mode: ")
        return mode

print("Welcome to Password Manager!")

name = input("What is your name? ")
print("Hi", name)
age = int(input("How old are you? "))

while True:
    chosen = menu()

    if chosen == "1":
        newpass = input("Add a password: ")
        passwords.append(newpass)
        
    elif chosen == "2":
        i = 0
        if i < len(passwords):
            print("{}".format(passwords))
            i += 1
        else:
            print("No passwords stored")
            
    elif chosen == "3":
        print("Thank you for using Password Manager \n Goodbye")
        exit()