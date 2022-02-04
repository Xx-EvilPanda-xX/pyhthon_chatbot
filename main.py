import random
import time
from datetime import datetime

def ask(question):
    return input(question + "\n")

def init():
    print("Hello, my name is Sandy. I'm an virtual chat bot programmed in Python.")
    name = input("What's your name?\n")
    print("Nice to meet you " + name + "!")
    return name

def getChoice():
    print("\n\nPlease enter an option:")
    print("1) Tell a joke")
    print("2) Tell the time")
    print("3) Check in")
    print("0) Quit")
    return int(input(""))

jokesp1 = ["Do you know Joe?", "Why'd the chicken cross the road?"]
jokesp2 = ["Joe mama!", "To get to the other side!"]

def tellJoke():
    index = random.randint(0, len(jokesp1) - 1)
    print(jokesp1[index] + "\n")
    time.sleep(2)
    print(jokesp2[index] + "\n")

def tellTime():
    now = datetime.now()
    print("Here's the date and time as of now: " + now.strftime("%d/%m/%Y %H:%M:%S"))

def checkIn():
    pass

name = init()

while (True):
    choice = getChoice();
    if (choice == 0):
        print("See ya!")
        break

    if (choice == 1):
        tellJoke()

    if (choice == 2):
        tellTime()

    if (choice == 3):
        checkIn()