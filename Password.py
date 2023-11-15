start = 0
loopOne = 0
loopTwo = 0
loopThree = 0
qLoop = 0
redoOne = 0
redoTwo = 0
password = ""
userName = ""
passList = []
special = ["!", "@", "#", "$", "%", "&"]
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9","0"]
#Note for future: Will save username and password into a dictionary. Update value (password) associated with key (username)


import time,sys,os
from time import sleep
welcome = [" --------------------------------------------------------------------- ",
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


def requirements(x,y):
    while x == 0:
        y = input("\nPlease enter a password with the following requirements: \n• 8 characters or more\n• Contains a special character\n• Contains a number\n\n")
        for spec in special:
            if spec in y and len(y) >= 8:
                for num in number:
                    if num in y:
                        if y not in passList:
                            x == 1
                            passList.append(y)
                            return x, y
                        else:
                            print("\nThat password has been used before!\n")
                            x = 0
                

while start == 0:
    while qLoop == 0:
        start = input("\n\nDo you have an account? (Y/N) ")
        try:
            if start.lower() == "y":
                qLoop += 1
                start += 1
            elif start.lower() == "n":
                qLoop += 1
        except:
            pass
            

    while loopOne == 0:
        try:
            if start.lower() == "n":
                userName = input("\nPlease enter a username: ")
                requirements(redoOne,password)
                loopOne += 1
            else:
                loopOne += 1
        except:
            pass


    while loopTwo == 0:
        reset = input("\nWould you like to reset your password? (Y/N) ")
        try:
            if reset.lower() == "y":
                requirements(redoTwo,password)
                loopTwo += 1
            elif reset.lower() == "n":
                loopTwo += 1
            else:
                loopTwo = 0
            if len(passList) == 3:
                passList.pop(0)
        except:
            pass
        
        
    while loopThree == 0:
        question = input("\nWould you like to run this program again? (Y/N) ")
        try:
            if question.lower() == "y":
                print("\n"*100)
                start = 0
                loopThree = 0
                loopTwo = 0
                loopOne = 0
                redoOne = 0
                redoTwo = 0
            elif question.lower() == "n":
                loopThree += 1
                start += 1
        except:
            pass
    
    
try:
    if userName == "":
        userName = "N/A"
    if len(passList) > 1:
        print(f"\nPassword associated with {userName} : {passList[-1]}")
    else:
        print(f"\nPassword associated with {userName} : {passList[0]}")
except:
    pass


print("\nThanks for using my program!\n")