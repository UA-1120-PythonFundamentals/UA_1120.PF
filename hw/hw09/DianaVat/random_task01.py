import random

comp = random.randint(1,100)
print("Hello! It is game. You need guess number from 1 to 100. You have 10 tries. Good luck! ")
trys = 0
while trys < 10:
    user = int(input())
    if user == comp:
        print("Congration! You guess!")
        break
    elif user < comp:
        print("more")
        trys+=1
    else:
        print("less")   
        trys+=1   
else:
    print("You lost.... :(")