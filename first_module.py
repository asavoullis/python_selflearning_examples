# This file is most like gonna be imported by second_module.py

# This is always run - when executed or when imported
print("hello there!")
# print("First Module's Name: {}".format(__name__))

# Recursion + Memorisation


# lru_cache = Least Recently Used Cache
from functools import lru_cache
import math

#   Type of input arguments in functions:
# Keyword (has an equal sign) - default argument
# Required (doesn't not have an equal sign)

# always first non default arguments!
# y is the required argument , x is the default argument or keyword
def g1(y, x=0):
    return x + y


def build_quadratic_function(a, b, c):
    """ Returns the function f(x) = ax^2 + bx + c """
    return lambda x: a*x**2 + b*x + c

def volume_of_sphere(r):
    # Docstring
    """ Returns the volume of a sphere with radius r. """
    v = (4.0/3.0) * math.pi * r**3
    return v


def area_of_triangle(b, h):
    """ Returns the area of the triangle with base b and height h. """
    return 0.5 * b * h


# assigning default value of 0 to both feet and inches
def cm(feet=0, inches=0):
    """ Converts a length from feet and inches to centimeters. """
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm, feet_to_cm

fibonacci_cache = {}
# Recursive functions:
def fibonacciv1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacciv2(n):
    # if we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

# Memorisation
@lru_cache(maxsize=1000)
def fibonacci(n):
    # Lets check that the first input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive integer. ")
    if n < 1:
        raise ValueError("n must be a positive integer. ")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)





# This is run when this file is directly executed
def main():
    print("First Module's Main Method")

    #   Lambda expressions - Anonymous Functions

    g = lambda x: 3 * x + 1
    print(g(2))

    fullname = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
    print(fullname("   leonard", "EULER   "))

    what_is_my_purpose = lambda : "What is my purpose?"
    print(what_is_my_purpose())

    scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke", "Frank Herbert",
                     "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]

    # to see how to use sort:
    # notice that key=None
    help(scifi_authors.sort)
    # sorting the list depending on their last name
    scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
    print(scifi_authors, "\n")

    # using build_quadratic_function function a = 2, b = 3, c = -5
    f = build_quadratic_function(2, 3, -5)
    print(f(0))
    print(f(1))
    print(f(2))
    # 3x^2 + 1 , evaluated for x = 2
    print(build_quadratic_function(3, 0, 1)(2), "\n")

    # range function does not include the last number so its 1 to 10 in this case
    for n in range(1, 10):
        print(n, ":", fibonacci(n))
    print("\n")

    # compute the ratio between consecutive terms
    for n in range(1, 10):
        # its going to be 1.61803398874989
        print(fibonacci(n+1) / fibonacci(n))

    print("\n")

    # prints the names of the functions in the current document
    print(dir())
    print("\n")
    import datetime
    print(dir(datetime))
    print("\n")

    print(volume_of_sphere(2))
    print("\n")

    print(area_of_triangle(3, 6))
    print("\n")

    print(cm(feet=5))
    print(cm(inches=70))
    print(cm(feet=5, inches=8))
    print(cm(inches=8, feet=5))
    print("\n")

    # sets y =5, x is optional and is set by default to 0
    print(g1(5))
    print(g1(5, 2))
    print(g1(5, x=3))
    print("\n")

    example = set()
    # to see
    print(dir(example))









# This is run when this file is directly executed
if __name__ == '__main__':
    # first main is executed
    main()

    print("first_module is run directly")

# This is run when this file is imported from another file
else:
    print("first_module is imported")