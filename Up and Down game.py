import random

num=random.randint(1,100)
10
while True:
        guess=int(input("Guess a number!:"))
        if guess>num:
                print("Down!")
        elif guess<num:
                print("Up!")
        else:
                print("You Got It!")
                break
