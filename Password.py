start = 0
loop = 0
secloop = 0
redo = 0
redo2 = 0
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

while start == 0:

    start = input("\n\nDo you have an account? (Y/N) ")

    while secloop == 0:
        try:
            if start.lower() == "n":
                username = input("Please enter a username: ")
                password = input("Please enter a password that's 8 characters or more: ")
                if len(password) < 8:
                    while redo == 0:
                        print("The password does not meet the length requirements!")
                        password = input("Please enter a password that meets the requirements: ")
                        try:
                            if len(password) < 8:
                                redo == 0
                            elif len(password) > 7:
                                redo += 1
                                secloop += 1
                        except:
                            pass
                else:
                    secloop += 1
        except:
            pass

    passlist = []
    passlist.append(password)

    reset = input("Would you like to reset your password? (Y/N) ")

    while loop == 0:
        try:
            if reset.lower() == "y":
                newpass = input("Please enter a password that's 8 characters or more: ")
                if len(newpass) < 8:
                    redo2 = 0
                    while redo2 == 0:
                        print("The password does the meet the length requirments!")
                        newpass = input("Please enter a password that meets the requirements: ")
                        try:
                            if len(newpass) < 8:
                                redo2 == 0
                            elif len(newpass) > 7:
                                if newpass in passlist:
                                    print("That password has been used before!")
                                    redo2 = 0
                                else:
                                    passlist.append(newpass)
                                    redo2 += 1
                                    loop += 1
                        except:
                            pass
                elif len(newpass) > 7 and newpass not in passlist:
                    loop += 1
                elif newpass in passlist:
                    print("That pasword has been used before!")
                    loop = 0
            else:
                loop += 1
            if len(passlist) == 4:
                passlist.pop(0)
        except:
            pass
    question = input("Would you like to run this program again? (Y/N) ")
    try:
        if question.lower() == "y":
            print("\n"*100)
            start = 0
        elif question.lower() == "n":
            start += 1
    except:
        pass

print("Thanks for using my program!")