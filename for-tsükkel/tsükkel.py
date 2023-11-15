"""Loop exercises."""


def sum_between(start: int, end: int) -> int:
    """
    Return sum of integers between start and end (both included).

    print(sum_between(3, 5)) => 3 + 4 + 5 = 12
    print(sum_between(5, 5)) => 5
    """
    numbers = list(range(start, end + 1))
    total = 0
    for nr in numbers:
        total = total + nr
    return total

    print(sum_between(3, 5))
    print(sum_between(5, 5))
    # Your code goes here


def sum_of_even_numbers(n: int) -> int:
    """
    Return sum of even numbers from 0 up to n (included).

    print(sum_of_even_numbers(5)) => 0 + 2 + 4 = 6
    print(sum_of_even_numbers(0)) => 0
    """
    result = 0
    for num in range(n + 1):
        if num % 2 == 0:
            result += num
    return result
    # Your code goes here


def sum_of_multiples(n: int, end: int) -> int:
    """
    Return sum of numbers which are multiples of n between 0 and end (included).

    print(sum_of_multiples(3, 10)) => 3 + 6 + 9 = 18
    print(sum_of_multiples(7, 10)) => 7
    print(sum_of_multiples(11, 10)) => 0
    """
    result = 0
    for num in range(n, end + 1):
        if num % n == 0:
            result += num
    return result
    # Your code goes here


def cross_sum(numbers: str) -> int:
    """
    Return cross sum of numbers.

    print(cross_sum("1234")) => 1 + 2 + 3 + 4 = 10
    print(cross_sum("0")) => 0
    print(cross_sum("4129458")) => 33
    """
    total = 0
    for digit_char in numbers:
        digit = int(digit_char)
        total += digit
    return total
  
    # Your code goes here


def multiply_between(start: int, end: int) -> int:
    """
    Multiply all numbers between start and end (both included).

    print(multiply_between(1, 3)) => 1 * 2 * 3 = 6
    print(multiply_between(4, 14)) => 14529715200
    print(multiply_between(0, 7)) => 0
    """
    result = 1
    for num in range(start, end + 1):
        result *= num
    return result
    # Your code goes here


def make_hola_string(count: int) -> str:
    """
    Make hola string.

    print(make_hola_string(3)) => "holaholahola"
    print(make_hola_string(0)) => ""
    """
    return "hola" * count
    # Your code goes here


def compound_interest(amount: int, years: int, rate: int) -> float:
    """
    Calculate compound interest.

    print(compound_interest(100, 2, 2)) => 104.04
    print(compound_interest(2000, 6, 8)) => 3173.748645888
    """
    for _ in range(years):
        amount += amount * (rate/100)
    return amount
    # Your code goes here


def remove_vowels(original_string: str) -> str:
    """
    Return the given string without vowels.

    print(remove_vowels("tere-tere")) => tr-tr
    print(remove_vowels("hklmn")) => hklmn
    print(remove_vowels("aauuiii")) => ""
    """
    vowels = "AEIOUÕÄÖÜaeiouõäöü"
    result = ""
    for char in original_string:
        if char not in vowels:
            result += char
    return result
    # Your code goes here


if __name__ == '__main__':
    print(sum_between(3, 5))  # => 3 + 4 + 5 = 12
    print(sum_between(5, 5))  # => 5

    print(sum_of_even_numbers(5))  # => 0 + 2 + 4 = 6
    print(sum_of_even_numbers(0))  # => 0

    print(sum_of_multiples(3, 10))  # => 3 + 6 + 9 = 18
    print(sum_of_multiples(7, 10))  # => 7
    print(sum_of_multiples(11, 10))  # => 0

    print(cross_sum("1234"))  # => 1 + 2 + 3 + 4 = 10
    print(cross_sum("0"))  # => 0
    print(cross_sum("4129458"))  # => 33

    print(multiply_between(1, 3))  # => 1 * 2 * 3 = 6
    print(multiply_between(4, 14))  # => 14529715200
    print(multiply_between(0, 7))  # => 0

    print(make_hola_string(3))  # => "holaholahola"
    print(make_hola_string(0))  # => ""

    print(compound_interest(100, 2, 2))  # => 104.04
    print(compound_interest(2000, 6, 8))  # => 3173.748645888

    print(remove_vowels("tere-tere"))  # => tr-tr
    print(remove_vowels("hklmn"))  # => hklmn
    print(remove_vowels("aauuiii"))  # => ""