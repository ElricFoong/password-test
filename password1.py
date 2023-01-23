password = "a123456"
chance = 3

while chance > 0 :
    chance -= 1
    passwd = input("Pleas input password. ")
    if passwd == password:
        print("login successful ")
        break
    else:
        
        print("Wrong password")
        if chance > 0:
            print("You got ", chance , "chance. ")
