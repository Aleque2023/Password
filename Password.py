start = 0
loopOne = 0
loopTwo = 0
redoOne = 0
redoTwo = 0
password = ""
passlist = []
#Note for future: Will save username and password into a dictionary. Update value (password) associated with key (username)

import time,sys,os
from time import sleep
welcome = [" ---------------------------------------------------------------------",
           "|             _______        ______  _______                _______   |",
           "| \        / |        |     |       |       |   /\    /\   |          |",
           "|  \  /\  /  |------- |     |       |       |  /  \  /  \  |-------   |",
           "|   \/  \/   |_______ |____  ______ |_______| /    \/    \ |_______   |",
           "|                                                                     |",
           " --------------------------------------------------------------------- "]

for char in welcome[0]:
    sys.stdout.write(char[0])
    sys.stdout.flush()
    time.sleep(.01)
for msg in welcome[1:5]:
    sys.stdout.write(f"\n{msg}")
    sys.stdout.flush()
    time.sleep(.5)
print("")    
for char in welcome[6]:
    sys.stdout.write(char[0])
    sys.stdout.flush()
    time.sleep(.01)

special = ["!", "@", "#", "$", "%", "&"]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9","0"] #Will add a number requirement as well.

def requirements(x,y):
    while x == 0:
        y = input("\nPlease enter a password with the following requirements: \n8 characters or more\nContains a special character\n\n")
        for spec in special:
            if spec in y and len(y) >= 8:
                if y not in passlist:
                    x == 1
                    passlist.append(y)
                    return y
                else:
                    print("\nThat password has been used before!\n")
                    x = 0
                

while start == 0:

    start = input("\n\nDo you have an account? (Y/N) ")

    while loopOne == 0:
        try:
            if start.lower() == "n":
                username = input("\nPlease enter a username: ")
                requirements(redoOne,password)
                loopOne += 1
                redoOne += 1
            else:
                loopOne += 1
        except:
            pass

    reset = input("\nWould you like to reset your password? (Y/N) ")

    while loopTwo == 0:
        try:
            if reset.lower() == "y":
                requirements(redoTwo,password)
                loopTwo += 1
            elif reset.lower() == "n":
                loopTwo += 1
            else:
                loopTwo = 0
            if len(passlist) == 3:
                passlist.pop(0)
        except:
            pass
    question = input("\nWould you like to run this program again? (Y/N) ")
    try:
        if question.lower() == "y":
            print("\n"*100)
            start = 0
            loopTwo = 0
            loopOne = 0
            redoOne = 0
            redoTwo = 0
        else:
            start += 1
    except:
        pass
print(f"Passwords associated with {username}:{passlist}\nThe current password is {passlist[-1]}")
print("\nThanks for using my program!\n")