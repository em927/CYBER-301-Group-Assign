# This code is for assignment 2 of CYBR 301 written by Emma Buckner and Kunj Champaneri
import re  # Package ftor using regular expressions

# Emma Buckner wrote the getusername()
def getusername_passwd() -> tuple:  # This function is used to get login information from the user check if it is valid
    # Variables used to user login information
    username = ""
    password = ""
    i = False  # Boolean variable uses to fire the while loop until the user enters valid login information
    username_validation = False  # username_validation stores if the entered username is valid
    password_para = ""  # Stores the match object of the re
    password_validation = False
    while i == False:
        username = input("Enter your username or email address: ")
        username_validation = "@" and "." in username
        print(
            "User passwords must contain at least: \n* eight characters \n* one uppercase letter \n* one lowercase letter \n* one number \n* one special character")
        password = input("Enter your password: ")
        password_para = re.search(r"(?=.+[\w])(?=.+[!@#$%^&*?_])[\w!@#$%^&*?_]{8,35}", password)
        if password_para != None and len(password) > 7:
            password_validation = True
        else:
            password_validation = False
        if username_validation == True and password_validation == True:
            i = True
            return username, password
        else:
            print(
                "The username and password you have enter do not follow the listed requirements. You will be prompted to reenter each.")


def main():
    vusername, vpassword = getusername_passwd() #retunes and stores values from getusername_passwd()
    #if else statments to verify that the username and password have been stored and call secure_store()

#invoke main()
main()