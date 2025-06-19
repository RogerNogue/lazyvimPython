from fizzbuzz import FizzBuzzOf


def test_fizzBuzzOf1Is1():
    assert FizzBuzzOf(1) == 1


def test_fizzBuzzOf3IsFizz():
    assert FizzBuzzOf(3) == "Fizz"


def test_fizzBuzzOf5IsBuzz():
    assert FizzBuzzOf(5) == "Buzz"


def test_fizzBuzzOf15IsFizzBuzz():
    assert FizzBuzzOf(15) == "FizzBuzz"


def test_fizzBuzzOf6IsFizz():
    assert FizzBuzzOf(6) == "Fizz"
