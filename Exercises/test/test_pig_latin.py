from Exercises.workout_strings import pig_latin

def test_word_starting_with_vowel():
    in_str = "Atlas"
    out_str = pig_latin(in_str)
    expected_out_str = 'atlasway'

    assert out_str.__eq__(expected_out_str)

def test_word_starting_without_vowel():
    in_str = "Beeline"
    out_str = pig_latin(in_str)
    expected_out_str = 'eelinebay'

    assert out_str.__eq__(expected_out_str)

