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

jokesp1 = ["What do you call a boomerang that won’t come back?",
           "What does a cloud wear under his raincoat?",
           "Two pickles fell out of a jar onto the floor. What did one say to the other?",
           "What time is it when the clock strikes 13?",
           "How does a cucumber become a pickle?",
           "What did one toilet say to the other?",
           "What do you think of that new diner on the moon?",
           "Why did the dinosaur cross the road?",
           "Why can’t Elsa from Frozen have a balloon?",
           "What musical instrument is found in the bathroom?"]

jokesp2 = ["A stick.",
           "Thunderwear.",
           "Dill with it.",
           "Time to get a new clock.",
           "It goes through a jarring experience.",
           "You look a bit flushed.",
           "Food was good, but there really wasn’t much atmosphere.",
           "Because the chicken wasn’t born yet.",
           "Because she will 'let it go, let it go.'",
           "A tuba toothpaste."]

def tellJoke():
    index = random.randint(0, len(jokesp1) - 1)
    print(jokesp1[index] + "\n")
    time.sleep(1)
    print(jokesp2[index] + "\n")

def tellTime():
    now = datetime.now()
    print("Here's the date and time as of now: " + now.strftime("%m/%d/%Y %H:%M:%S\n"))

def checkIn(name):
    answer = input("How's your day going? (good/bad)\n")

    if (answer == "good"):
        print("Good to hear!")
    elif (answer == "bad"):
        print("Sorry to hear that " + name + ". :(")
        if (input("Would you like to hear a joke to cheer you up? (yes/no)\n" ) == "yes"):
            tellJoke()
    else:
        print("I don't understand. Please try again.")
        checkIn()

def numberGame():
    number = random.randint(0, 100)
    guess = None
    while (guess != number):
        guess = int(input("Please enter a number from 0 to 100: "))
        if (guess > 100 or guess < 0):
            print("Out of range!")
            continue
        if (guess < number):
            print("Nope! Try a bigger number.")
        elif (guess > number):
            print("Nope! Try a smaller number.")

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
        checkIn(name)

    if (choice == 4):
        numberGame()

