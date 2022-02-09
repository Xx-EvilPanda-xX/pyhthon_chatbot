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
    print("Please enter an option:")
    print("1) Tell a joke")
    print("2) Tell the time")
    print("3) Check in")
    print("4) Play a number game")
    print("0) Quit")
    return int(input(""))

jokesp1 = ["Do you know Joe?", "Why'd the chicken cross the road?"]
jokesp2 = ["When the", "Joe mama!"]

def tellJoke():
    index = random.randint(0, len(jokesp1) - 1)
    print(jokesp1[index] + "\n")
    time.sleep(1)
    print(jokesp2[index] + "\n")

def tellTime():
    now = datetime.now()
    print("Here's the date and time as of now: " + now.strftime("%d/%m/%Y %H:%M:%S\n"))

def checkIn():
    answer = input("How's your day going? (good/bad)\n")

    if (answer == "good"):
        print("Good to hear!")
    elif (answer == "bad"):
        print("Sorry to hear that. :(")
        if (input("Would you like to hear a joke to cheer you up? (yes/no)\n" ) == "yes"):
            tellJoke()
    else:
        print("I don't understand. Please try again.")
        checkIn()

def numberGame():
    number = random.randint(0, 100)
    guess = int(input("Please enter a number from 0 to 100: "))
    while (guess != number):
        if (guess > 100 or guess < 0):
            print("Out of range!")
            continue
        if (guess < number):
            print("Nope! Try a bigger number.")
        elif (guess > number):
            print("Nope! Try a smaller number.")
        guess = int(input("Please enter a number from 0 to 100: "))

    print("Nice job! The number was " + str(number) + "\n")

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

    if (choice == 4):
        numberGame()