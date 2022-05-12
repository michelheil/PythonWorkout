# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def guessing_game():
    # Exercise 1
    # Number guessing game

    # create random integer between 0 and 100
    rand_int = random.randint(0, 100)

    # compare guessed integer with random integer
    while True:

        # ask user to guess what number has been chosen
        guessed_int = int(input('Enter your guess: '))

        if guessed_int < rand_int:
            print('Too low')

        if guessed_int > rand_int:
            print('Too high')

        if guessed_int == rand_int:
            print('Just right')
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    guessing_game()
