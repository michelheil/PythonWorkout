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
