from workout_strings import *
from workout_numeric import *
from caching import *
from timeit import Timer

if __name__ == '__main__':
    # guessing_game()
    # print(mysum(1, 2, 3))
    # print(mysum(*[4, 5, 6]))
    # run_timing()
    # print(pig_latin("Hello"))
    # print(pig_latin("Anton"))
    # print(pig_latin("Football"))
    timer1 = Timer("fak(200000)", globals={"fak": fak})
    print('Erster Aufruf: ' + str(timer1.timeit(1)) + ' sec')
    timer2 = Timer("fak(200000)", globals={"fak": fak})
    print('Zweiter Aufruf: ' + str(timer2.timeit(1)) + ' sec')
