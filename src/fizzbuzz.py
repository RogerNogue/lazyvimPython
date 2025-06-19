
def IsMultipleOf3(number):
    return number % 3 == 0

def IsMultipleOf5(number):
    return number % 5 == 0


def FizzBuzzOf(number):
    if IsMultipleOf3(number) and IsMultipleOf5(number):
        return "FizzBuzz"
    if IsMultipleOf3(number):
        return "Fizz"
    if IsMultipleOf5(number):
        return "Buzz"
    return number


print(FizzBuzzOf(1))
