loop = 0
secloop = 0
#Note for future: Will save username and password into a dictionary. Update value (password) associated with key (username)
while secloop == 0:
    start = input("Do you have an account? (Y/N) ")
    try:
        if start.lower() == "n":
            username = input("Please enter a username: ")
            password = input("Please enter a password: ")
    except:
        pass


#username = input("Please enter a username: ")
#password = input("Please enter a password: ")

passlist = []
passlist.append(password)

while loop == 0:
    try:
        reset = input("Would you like to reset your password? (Y/N) ")

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