start = 0
loopOne = 0
loopTwo = 0
redoOne = 0
redoTwo = 0
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

while start == 0:

    start = input("\n\nDo you have an account? (Y/N) ")

    while loopOne == 0:
        try:
            if start.lower() == "n":
                username = input("\nPlease enter a username: ")
                while redoOne == 0:
                    password = input("\nPlease enter a password with the following requirements: \n8 characters or more\nContains a special character\n\n")
                    for spec in special:
                        if spec in password:
                            if len(password) >= 8:
                                output = True
                                redoOne += 1
                                loopOne += 1
                            else:
                                redoOne = 0
                        elif spec not in password or len(password) < 8:
                            output = False
                if output == True:
                    redoOne += 1
                    loopOne += 1
                else:
                    redoOne = 0
            else:
                loopOne += 1
        except:
            pass

    passlist = []
    passlist.append(password)

    reset = input("\nWould you like to reset your password? (Y/N) ")

    while loopTwo == 0:
        try:
            if reset.lower() == "y":
                newpass = input("\nPlease enter a password that's 8 characters or more: ")
                if len(newpass) < 8:
                    redoTwo = 0
                    while redoTwo == 0:
                        print("\nThe password does the meet the length requirements!")
                        newpass = input("\nPlease enter a password that meets the requirements: ")
                        try:
                            if len(newpass) < 8:
                                redoTwo == 0
                            elif len(newpass) > 7:
                                if newpass in passlist:
                                    print("\nThat password has been used before!")
                                    redoTwo = 0
                                else:
                                    passlist.append(newpass)
                                    redoTwo += 1
                                    loopTwo += 1
                        except:
                            pass
                elif len(newpass) > 7 and newpass not in passlist:
                    loopTwo += 1
                elif newpass in passlist:
                    print("\nThat password has been used before!")
                    loopTwo = 0
            else:
                loopTwo += 1
            if len(passlist) == 4:
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
        elif question.lower() == "n":
            start += 1
    except:
        pass

print("\nThanks for using my program!\n")