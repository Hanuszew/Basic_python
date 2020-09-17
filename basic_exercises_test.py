import pytest

from basic_exercises import *


@pytest.mark.simple_fb
@pytest.mark.parametrize("a,b", (
        (0, []),
        (15, [1, 2, "Buzz", 4, "Fizz", "Buzz", 7, 8, "Buzz", "Fizz", 11, "Buzz", 13, 14, 'FizzBuzz']),
))
def test_fizz_buzz(a, b):
    assert fizz_buzz(a) == b
    assert len(fizz_buzz(60)) == 60
    assert fizz_buzz(1000)[599] == "FizzBuzz"


@pytest.mark.parametrize("a, b", (
        (4, 3),
        (5, 5),
        (1, 1),
        (0, 0),
))
def test_fibonacci(a, b):
    assert fibonacci(a) == b


@pytest.mark.skip
@pytest.mark.parametrize("a, b", (
        (4, 3),
        (5, 5),
        (1, 1),
        (0, 0),
))
def test_fibonacci_for(a, b):
    assert fibonacci_for(a) == b


@pytest.mark.parametrize("a, b", (
        ('kajak', True),
        ('Devil lived', True),
         ('jajko', False),
        ('Kamak', True)
))
def test_check_palindrom(a, b):
    assert check_palindrom(a) == b


@pytest.mark.parametrize('n, b', (
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (11, True),
        (12, False),
        (13, True),
))
def test_is_prime(n, b):
    assert is_prime(n) == b


@pytest.mark.parametrize('n, b', (
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (11, True),
        (12, False),
        (13, True),
))
def test_is_prime(n, b):
    assert is_prime_2(n) == b


@pytest.mark.parametrize("a, b", (
        (20, {'5zl': 4, '2zl': 0, '1zl': 0}),
        (1, {'5zl': 0, '2zl': 0, '1zl': 1}),
        (19, {'5zl': 3, '2zl': 2, '1zl': 0}),
        (20, {'5zl': 4, '2zl': 0, '1zl': 0}),
))
def test_money_quiz(a, b):
    assert money_quiz(a) == b


@pytest.mark.parametrize("a, b", (
        ([9, 8, 7, 6], ([6, 7, 8, 9])),
        ([1, 9, 9, 7, 6], ([1, 6, 7, 9, 9])),
        ([0], ([0])),
))
def test_bubble_sort(a, b):
    assert bubble_sort(a) == b


@pytest.mark.xfail
def test_xfail():
    li = ['test']
    assert li[0] == 'fail'


