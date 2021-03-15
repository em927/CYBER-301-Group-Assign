'''
Author: Naresh Adhikari, Sru
This is a skeletal program that students need to implement the declared
and defined functions under @TODO annotation, according to the logic/functional requirements stated in assigment-2.pdf.

Students are not expected to modify main().
'''

import hashlib
import csv
def secure_hashed_passwd(username, passwd):
    import hashlib, uuid
    import os

    '''
    @TODO: Students are required to implement this function.
    using salt+paper+sha3-224 algorithm
    :param username: string repr of username
    :param passwd: a plain text password
    :return: True if given values are stored successfully in outfile var; else returns False
    '''

    


    #use salt and pepper to hash 'hpasswd' using sha-3-224 algorithm
    # Add salt

    # add pepper

    #return salt,pepper,saltpepperdigest

# verify_hashed_passwd() is written by Emma Buckner
def verify_hashed_passwd(username, passwd):
    '''
    @TODO: Students are required to implement this function.
    Server side verifies login credentials username and password
    :param username: used to look for a match in hlogins.dat
    :param passwd: user passwd in plaintext
    :return: if username is found in hlogin.dat then checks the hashed password with tempo_hash and returns either true
    or false, otherwise verify_hashed_passwd() returns false
    '''
    #stores file
    infile = "hlogins.dat"

    #opens the file to read
    fd = open(infile, mode='r')

    # used to read file
    for file_line in csv.reader(fd):
        for i in file_line: #stores entries in list
            if username in file_line: #searches list for username
                tempo_hash = hashlib.sha3_224(passwd) #makes temp hash of passwd
                if tempo_hash in file_line: #compares actual hash in file to temp hash
                    print('Authentication successful')
                    return True
                else:
                    print('Authentication unsuccessful')
                    return False
        else:
            print('Authentication unsuccessful')
            return False
        
   #closes file    
   fd.close()   
  
#main()
def main():
    '''Do not modify this function.'''

    import hashlib, uuid
    import os

    lusername=["shyamal@gmail.com",
                "brutforce@yahoo.com",
                "lifegivesalot@protonmail.com",
                "rainbow@sru.edu",
                "ghana@makai.com",
                "david@inst.edu",
                "buttlerbusiness@sru.edu",
                "myChurch45@state.edu"]
    lpasswd=["pass$1290Red",
            "fail$567Blue",
            "rainB0w159$",
            "lglot$$$Tatoo",
            "ghana456$$909",
            "DavI0234$09",
            "IsBulltop345",
            "xCrosTop24"]

    # open file outfile in write mode.
    outfile="hlogins.dat"
    fd = open(outfile, "w+")
    #@server: call method for each usernames, passwords.
    for i in range(0,len(lusername)):
        username=lusername[i]
        passwd=lpasswd[i]
        salt,pepper,saltpepperdigest=secure_hashed_passwd(username,passwd)
        if i in [3,7,1]:continue
        fd.write(username + "," + str(salt) + "," + str(pepper) + "," + saltpepperdigest+","+"$\n")
    fd.close()

    for j in range(0,len(lusername)):
        uname=lusername[j]
        passwd=lpasswd[j]
        result=verify_hashed_passwd(uname,passwd)
        if not result:
            print("<!> Login failed for user ",uname)
        else:
            print("Login succesful for user ",uname)

if __name__ == "__main__":
    main()
