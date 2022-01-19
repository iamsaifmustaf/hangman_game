import hangman_words
import hangman_pics
from art import *
import random
import time
import os
import sys

word = ""
final_answer = []
hangman_steps = 0


def restart():
    os.system("cls")
    os.execv(sys.executable, ["python"] + sys.argv)


def check_input(char):
    if char in word:
        count = 0
        if char in final_answer:
            print(
                hangman_pics.pics[hangman_steps]
                + "\n\nYou already used this character, Try Again!\n\n"
            )
            globals()["hangman_steps"] += 1
        while count < len(final_answer):
            if char == word[count]:
                final_answer[count] = char
                count += 1
            else:
                count += 1
        print("".join(final_answer))

    else:
        print(hangman_pics.pics[hangman_steps] + "\n\nWrong Entry, Try Again!\n\n")
        globals()["hangman_steps"] += 1


tprint("Welcome   to   hangman  !")

category = int(
    input(
        "\n\nPlease Choose Your Category. Enter (1) for Animals, (2) for Car Brands: \n\n"
    )
)


if category == 1:
    word += hangman_words.animals[random.randint(0, len(hangman_words.animals) - 1)]
    final_answer = ["_"] * len(word)
if category == 2:
    word += hangman_words.car_brands[
        random.randint(0, len(hangman_words.car_brands) - 1)
    ]
    final_answer = ["_"] * len(word)

word = word.lower()

os.system("cls")

while hangman_steps < 7:
    time.sleep(1.5)
    os.system("cls")
    if "_" not in final_answer:
        print(f"\n\nThe word is {word}. Congrats, You won the game\n\n")
        time.sleep(1)
        restart()
    else:
        character = input("Please enter your character of choice: ")
        check_input(character)

print(f"\n\nThe word is {word}. Game Over, Better Luck Next Time!\n\n")
time.sleep(2)
restart()
