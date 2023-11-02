import io
import random
import string
import sys
import math

import pytest
import function_basic as t03

# ---------- print_hello() ------------
@pytest.mark.timeout(1.0)
@pytest.mark.dependency()
def test__print_hello_returns_none():
    assert t03.print_hello() is None


@pytest.mark.timeout(1.0)
@pytest.mark.dependency(depends=['test__print_hello_returns_none'])
def test__print_hello_prints_hello(capsys):
    t03.print_hello()
    captured = capsys.readouterr()
    assert "Hello" in captured.out, "Does the function \"print_hello\" print \"Hello\"? The letter should be a capital H."

# ---------- get_hello() -------------------

get_hello = None
if 'get_hello' in dir(t03):
    get_hello = t03.get_hello


@pytest.mark.timeout(1.0)
@pytest.mark.dependency(depends=['test__print_hello_prints_hello'])
def test__get_hello_exists():
    assert get_hello is not None, "Function \"get_hello\" should return string."


@pytest.mark.timeout(1.0)
@pytest.mark.dependency(depends=['test__print_hello_prints_hello'])
def test__get_hello_returns_hello():
    assert get_hello() == "Hello", "Does the function \"get_hello\" return \"Hello\"? The first letter should be a capital H"


# --------- ask_name_and_greet_user() ---------------

ask_name_and_greet_user = None
if 'ask_name_and_greet_user' in dir(t03):
    ask_name_and_greet_user = t03.ask_name_and_greet_user

names = (
    "john",
    "jOHN",
    "John",
    "kirill",
    "not kirill",
    "Hubert Blaine Wolfeschlegelsteinhausenbergerdorff"
)

thanos_name_cases = (
    "Thanos",
    "tHaNoS",
    "tHANOS",
    "thanos"
)

@pytest.mark.timeout(1.0)
@pytest.mark.dependency(depends=['test__get_hello_returns_hello'])
def test__ask_name_and_greet_user_exists():
    assert ask_name_and_greet_user is not None

@pytest.mark.timeout(1.0)
@pytest.mark.dependency(
    depends=['test__ask_name_and_greet_user_exists'],
    name='test__ask_name_and_greet_user_prints_correct_message'
)
@pytest.mark.parametrize(
    "name",
    names,
)
def test__ask_name_and_greet_user_prints_correct_message(name, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO(name))
    ask_name_and_greet_user()
    captured = capsys.readouterr()
    assert f'Hi, {name.capitalize()}. Would you like to have a Hamburger?' in captured.out
    assert 'Get out of here, Thanos! Nobody wants to play with you!' not in captured.out


@pytest.mark.timeout(1.0)
@pytest.mark.dependency(depends=['test__ask_name_and_greet_user_prints_correct_message'])
@pytest.mark.parametrize(
    "thanos_name",
    thanos_name_cases,
)
def test__ask_name_and_greet_user_prints_correct_message_for_thanos(thanos_name, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO(thanos_name))
    ask_name_and_greet_user()
    captured = capsys.readouterr()
    assert 'Get out of here, Thanos! Nobody wants to play with you!' in captured.out
    assert 'Hamburger' not in captured.out


@pytest.mark.timeout(1.0)
@pytest.mark.dependency(depends=['test__ask_name_and_greet_user_prints_correct_message'])
def test__ask_name_and_greet_user_returns_nothing(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO("ai"))
    assert ask_name_and_greet_user() is None


# ------ pythagoras -------------------

calculate_hypotenuse_length = None
if 'calculate_hypotenuse_length' in dir(t03):
    calculate_hypotenuse_length = t03.calculate_hypotenuse_length
calculate_cathetus_length = None
if 'calculate_cathetus_length' in dir(t03):
    calculate_cathetus_length = t03.calculate_cathetus_length

hypotenuse_test_data = ((3, 4),
                        (1, 2),
                        (94, 38),
                        (9, 55),
                        (32, 49),
                        (36, 91),
                        (84, 73),
                        (51, 59),
                        (3150420, 25511639), (39451534, 20351305), (17860712, 18201977), (30726784, 9773215))

cathetus_test_data = ((3, 5), (19, 50), (16, 71), (14, 15), (37, 44), (33, 43),
                      (19698872, 45672596), (6397696, 36481322),
                      (3326314, 19023438), (15717452, 40221436), (16445750, 34693076))

@pytest.mark.incgroupdepend("ask_name_and_greet_user")
@pytest.mark.incgroup("calculate_hypotenuse_length_exists")
def test__calculate_hypotenuse_lengthh_exists():
    assert calculate_hypotenuse_length is not None

@pytest.mark.incgroupdepend("ask_name_and_greet_user")
@pytest.mark.incgroup("calculate_cathetus_length_exists")
def test__calculate_cathetus_length_exists():
    assert calculate_cathetus_length is not None

def _calculate_hypotenuse_length_solution(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def _calculate_cathetus_length_solution(a, c):
    return math.sqrt(c ** 2 - a ** 2)

@pytest.mark.incgroupdepend("calculate_hypotenuse_length_exists")
@pytest.mark.incgroup("calculate_pythagoras")
@pytest.mark.timeout(1.0)
@pytest.mark.parametrize(
    "a,b",
    hypotenuse_test_data,
)
def test__hypotenuse_calculation_is_correct(a, b):
    assert calculate_hypotenuse_length(a, b) == _calculate_hypotenuse_length_solution(a, b)


@pytest.mark.incgroupdepend("calculate_cathetus_length_exists")
@pytest.mark.incgroup("calculate_pythagoras")
@pytest.mark.timeout(1.0)
@pytest.mark.parametrize(
    "a,c",
    cathetus_test_data,
)
def test__catchetus_calculation_is_correct(a, c):
    assert calculate_cathetus_length(a, c) == _calculate_cathetus_length_solution(a, c)
