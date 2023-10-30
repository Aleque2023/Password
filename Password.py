loop = True

username = input("Please enter a username: ")
password = input("Please enter a password: ")

passlist = []
passlist.append(password)

while loop == True:
    reset = input("Would you like to reset your password? (Y/N) ")

    if reset.lower == "y":
        password = input("Please enter a password: ")
        passlist.append(password)
    elif reset.lower == "n":
        loop == False