# This code is for assignment 2 of CYBR 301 written by Emma Buckner and Kunj Champaneri
import re  # Package for using regular expressions
from Crypto.Cipher import AES
from secrets import token_bytes

'''
#Notes from Instructor:
Hey Team, I recommend following changes in your getusername_passwd() function
1. separate the logic(s) to validate username and password; that you can write a function
to validate a username, and another function to validate the password.
2. Here, use of regular expression is correct. Just try to simplify when to continue looping for invalid password.
ex.
i=True
password=input(..)
while i==False:
if re.search(regex,password):
   i=True
else:
    password=input(..)
    

The point here is simplify your logic by separating logics to validate username and password. That way, it becomes easy
to test the function..
'''


# Emma Buckner wrote the getusername_passwd()
def getusername_passwd():
    # Variables used to user get login information and validate it
    username = ""
    password = ""
    i = False  # Boolean variable uses to fire the while loop until the user enters valid login information
    username_validation = False  # username_validation stores if the entered username is valid
    password_para = ""  # Stores the match object of the re
    password_validation = False  # Stores if the entered password is valid

    while i == False:
        # Asks user to enter username and checks that it is a valid email address
        username = input("Enter a username or email address: ")
        username_validation = "@" and "." in username
        if username_validation:
            i = True
            print("You have entered a valid username.")
        else:
            print("The username you have entered is invalid. Enter a valid username or email address:")

    i = False  # Resets i to false for the loop to iterate
    while i == False:
        # Asks user to enter password and checks if it meets all the printed parameters
        print("User passwords must contain at least:")
        print("* 8 characters \n* 1 uppercase letter \n* 1 lowercase letter \n* 1 number \n* 1 special character")
        password = input("Enter your password: ")

        # checks if the password requirements are met
        password_regex = r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*?_])"
        match_regex = re.compile(password_regex)
        password_para = re.search(match_regex, password)
        if password_para != None and len(password) > 7:
            password_validation = True
            i = True
        else:
            password_validation = False
            print("The password entered is invalid. Enter a valid password.")

     # Checks that the username and password are valid before returning to main()
     if username_validation == True and password_validation == True:
         return username, password
     # If one or both are invalid then the loop iterates and the user must enter a valid username and password
     else:
         return None, None
      
      
#secure_store() function is written by Kunj Champaneri

def secure_store(username, password): #The secure_store function
    key = token_bytes(16) #Assigning the key
    cipher = AES.new(key, AES.MODE_EAX) #Assigning the cipher
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(username.encode('ascii')) #Encrypting the username 
    ciphertext1, tag = cipher.encrypt_and_digest(password.encode('ascii')) #Encrypting the password 
    
    file = open("credential.dat", "w") #Opening the file
    file.write(username) #Writing to the file
    file.write(password) #Writing to the file 

def main():
    vusername, vpassword = getusername_passwd()  # Returns and stores values from getusername_passwd()
    # If else statements to verify that the username and password have been stored and call secure_store()
   secure_store(username, password) #Calling the function 


# Invoke main()
main()
