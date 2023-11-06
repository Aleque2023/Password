loop = 0
secloop = 0
redo = 0
#Note for future: Will save username and password into a dictionary. Update value (password) associated with key (username)

import time,sys
from time import sleep
welcome = [" ---------------------------------------------------------------------",
           "|             _______        ______  _______                _______   |",
           "| \        / |        |     |       |       |   /\    /\   |          |",
           "|  \  /\  /  |------- |     |       |       |  /  \  /  \  |-------   |",
           "|   \/  \/   |_______ |____  ______ |_______| /    \/    \ |_______   |",
           "|_____________________________________________________________________|"]

for char in welcome.index[0]:
    sys.stdout.write(char[0])
    sys.stdout.flush()
    time.sleep(.08)
for msg in welcome[1:5]:
    sys.stdout.write(f"\n{msg}")
    sys.stdout.flush()
    time.sleep(.5)

start = input("\n\nDo you have an account? (Y/N) ")

while secloop == 0:
    try:
        if start.lower() == "n":
            username = input("Please enter a username: ")
            password = input("Please enter a password that's 8 characters or more: ")
            if len(password) < 8:
                while redo == 0:
                    print("The password does not meet the requirements!")
                    password = input("Please enter a password that meets the requirements: ")
                    try:
                        if len(password) < 8:
                            redo == 0
                        elif len(password) > 7:
                            redo += 1
                            secloop += 1
                    except:
                        pass
    except:
        pass

passlist = []
passlist.append(password)

reset = input("Would you like to reset your password? (Y/N) ")

while loop == 0:
    try:
        if reset.lower() == "y":
            newpass = input("Please enter a password: ")
            if newpass in passlist:
                print("That password has been used before!")
                pass
            else:
                passlist.append(newpass)
        else:
            loop += 1
        if len(passlist) == 4:
            passlist.pop(0)
    except:
        pass

print("Thanks for using my program!")