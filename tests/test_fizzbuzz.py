from fizzbuzz import FizzBuzzOf


def test_fizzBuzzOf1Is1():
    assert FizzBuzzOf(1) == 1


def test_fizzBuzzOf3IsFizz():
    assert FizzBuzzOf(3) == "Fizz"


def test_fizzBuzzOf5IsBuzz():
    assert FizzBuzzOf(5) == "Buzz"


def test_fizzBuzzof15IsFizzBuzz():
    assert FizzBuzzOf(15) == "FizzBuzz"
