username = input("Please enter a username: ")
password = input("Please enter a password: ")

passlist = []
passlist.append(password)

reset = input("Would you like to reset your password? (Y/N) ")
try:
     if reset.lower() == "y":
          loop = 0
except:
     print("Thanks for using my program!")

while loop == 0:
    try:

        if reset.lower() == "y":
            newpass = input("Please enter a password: ")
            if newpass in passlist:
                print("That password has been used before!")
            else:
                passlist.append(newpass)
        else:
            loop += 1
        if len(passlist) == 4:
            passlist.pop(0)
        print(passlist)
    except:
        pass