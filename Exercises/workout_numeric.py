import random


def guessing_game():
    """
    Exercise 1
    Number guessing game
    :return:
    """

    # create random integer between 0 and 100
    rand_int = random.randint(0, 100)

    # compare guessed integer with random integer
    while True:

        # ask user to guess what number has been chosen
        guessed_int = int(input('Enter your guess: '))

        if guessed_int < rand_int:
            print('Too low')

        elif guessed_int > rand_int:
            print('Too high')

        else:
            print('Just right')
            break


def mysum(*numbers):
    """
    Exercise 2
    Summing numbers
    :param numbers:
    :return:
    """

    # initiate result
    result = 0

    for number in numbers:
        result += number

    return result


def run_timing():
    """

    :return:
    """
    number_of_runs = 0
    total_time = 0

    while True:
        user_input = input("Enter 10 km run time: ")

        if not user_input:
            break

        else:
            try:
                run_time_as_float = float(user_input)
                number_of_runs += 1
                total_time += run_time_as_float
            except ValueError as e:
                print("Hey! That`s not a valid number!")
                print(e)

        try:
            average_time = total_time / number_of_runs
            print(f'Average of {average_time:.2f}, over {number_of_runs} runs')
        except ZeroDivisionError as e:
            print('Keine gültige Zeitangabe')
            print(e)
