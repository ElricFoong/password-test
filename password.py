password = "a123456"
chance = 3
while True:
    passwd = input("Pleas input password. ")
    if passwd == password:
        print("login successful ")
        break
    else:
        print("Wrong password, you still have ", chance, "chance. ")
        chance -= 1
        if chance < 0:
            print("Failed. ")
            break