from Exercises.ExcercisesNumeric import *
from io import StringIO
import random

# monkeypatch = "mock"
# capsys = return a ``(out, err)`` namedtuple

def test_correct(monkeypatch, capsys):
    random.seed(0)  # first randint will be 49
    monkeypatch.setattr('sys.stdin', StringIO('49\n'))
    guessing_game()
    captured_out, captured_err = capsys.readouterr()

    assert captured_out.endswith('Just right\n')


def test_too_low_once(monkeypatch, capsys):
    random.seed(0)  # first randint will be 49
    monkeypatch.setattr('sys.stdin', StringIO('1\n49\n'))
    guessing_game()
    captured_out, captured_err = capsys.readouterr()

    assert 'Too low' in captured_out
    assert captured_out.endswith('Just right\n')


def test_too_high_once(monkeypatch, capsys):
    random.seed(0)  # first randint will be 49
    monkeypatch.setattr('sys.stdin', StringIO('100\n49\n'))
    guessing_game()
    captured_out, captured_err = capsys.readouterr()

    assert 'Too high' in captured_out
    assert captured_out.endswith('Just right\n')


def test_too_low_twice(monkeypatch, capsys):
    random.seed(0)  # first randint will be 49
    monkeypatch.setattr('sys.stdin', StringIO('1\n2\n49\n'))
    guessing_game()
    captured_out, captured_err = capsys.readouterr()

    assert 'Too low' in captured_out
    assert 'Too low' in captured_out
    assert captured_out.endswith('Just right\n')


def test_too_high_twice(monkeypatch, capsys):
    random.seed(0)  # first randint will be 49
    monkeypatch.setattr('sys.stdin', StringIO('100\n80\n49\n'))
    guessing_game()
    captured_out, captured_err = capsys.readouterr()

    assert 'Too high' in captured_out
    assert 'Too high' in captured_out
    assert captured_out.endswith('Just right\n')
