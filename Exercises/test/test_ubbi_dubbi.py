from Exercises.workout_strings import ubbi_dubbi


def test_octopus():
    in_str = "octopus"
    out_str = ubbi_dubbi(in_str)
    expected_str = "uboctubopubus"

    assert out_str == expected_str

def test_elephant():
    in_str = "elephant"
    out_str = ubbi_dubbi(in_str)
    expected_str = "ubelubephubant"

    assert out_str == expected_str

def test_soap():
    in_str = "soap"
    out_str = ubbi_dubbi(in_str)
    expected_str = "suboubap"

    assert out_str == expected_str