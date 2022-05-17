from Exercises.workout_strings import strsort


def test_cba():
    in_str = "cba"
    out_str = strsort(in_str)
    expected_str = "abc"

    assert out_str == expected_str

def test_greshtt():
    in_str = "greshtt"
    out_str = strsort(in_str)
    expected_str = "eghrstt"

    assert out_str == expected_str
