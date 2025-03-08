"""
1 = snake
-1 = water
0 = Gun

"""
import random
computer = computer = random.choice([1, -1, 0])
print("computer")
youstr = (input("enter your choice s/w/g: "))
yourdict ={'s': 1, 'w':-1,'g':0 }
Reversedict ={1: "snake", -1:"water",0:"gun" }
you = yourdict[youstr]

print(f"computer chose {Reversedict[computer]}")

if(computer == you):
    print("its a draw")

else:
    if (computer == -1 and you == 1):
        print("you win !")

    elif (computer == -1 and you == 0):
        print("you lose !")

    elif (computer == 1 and you == -1):
        print("you lose!")

    elif(computer ==1 and you == 0):
        print("you win!")

    elif(computer == 0 and you == 1):
        print("you lose!")

    elif(computer == 0 and you == -1):
        print("you win")

    else:
        print("something went wrong")