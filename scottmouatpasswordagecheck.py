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
        

            
            

    
    
      
    
existing_u = ["Trisanman", "Scottman"]
existing_p = ["Coolguy123", "Coolerguy123"]
passwords_stored = []
name = input("Hello, what is your name? ")
age = int(input("How old are you? "))
check(name, age)