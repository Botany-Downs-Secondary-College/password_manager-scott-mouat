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
            
            

    
    
      
    
existing_u = ["Trisanman", "Scottman"]
existing_p = ["Coolguy123", "Coolerguy123"]
passwords_stored = []
name = input("Hello, what is your name? ")
age = int(input("How old are you? "))
check(name, age)