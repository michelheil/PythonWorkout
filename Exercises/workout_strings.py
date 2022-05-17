# Python Workout

def pig_latin(in_string: str):
    """
    . If the word begins with a vowel, add "way" to the end of the word
    . If the words begins with any other letter, then the first letter moves to the end of the word, and we add "ay".

    :param in_string:
    :return:
    """

    # to lower case
    in_string_low = in_string.lower()

    if in_string_low[0] in 'aeiou':
        out_string = in_string_low + 'way'
    else:
        out_string = in_string_low[1:] + in_string_low[0] + 'ay'

    return out_string


def ubbi_dubbi(in_str: str):
    """
    For this exercise, you’ll write a function (called ubbi_dubbi ) that takes a single
    word (string) as an argument. It returns a string, the word’s translation into Ubbi
    Dubbi. So if the function is called with octopus, the function will return the string
    uboctubopubus. And if the user passes the argument elephant, you’ll output
    ubelubephubant. soap will become suboubap.

    :return:
    """
    res = []

    for letter in in_str:
        if letter in 'aeiou':
            res.append("ub" + letter)
        else:
            res.append(letter)

    return ''.join(res)
