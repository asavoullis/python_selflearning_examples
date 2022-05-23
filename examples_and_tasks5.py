# Python practise examples and tasks 5

from functools import reduce
from decimal import *

"""
6 Python Tips and Tricks YOU Should Know
https://www.youtube.com/watch?v=qEr9iRX4K0o
"""


class Astrobody:
    description = 'Natural entity in the observable universe.'


class Star(Astrobody):
    pass


"""Task1: Passing a variable number of arguments to a function using special symbols. """
def make_dict(**kwargs):
    """
    Passing a variable number of arguments to a function using special symbols:

    *args to pass Non Keyword Arguments:
    passes variable number of non-keyworded arguments and on which operation of the tuple can be performed.

    **kwargs to pass Keyword Arguments:
    passes variable number of keyword arguments dictionary to function
    on which operation of a dictionary can be performed.

    We made the function flexible in this case.

    Makes a dictionary in this case
    """
    return kwargs


"""Task2: Explore with open -file. """
def func_file():
    """ """
    with open('hello.txt', 'w') as file:
        file.write("hello!")

    print(file.closed)
    file.close()


"""Task3: Swap variables in a single line. """
def swap_variables(a, b):
    """ Swaps the values of a and b in a single line - without the need for a 3rd variable """
    a, b = b, a
    return a, b


"""Task4: find the max and the min values of a list using functions. """
def max_min_of_list(input_list):
    largest = max(input_list)
    smallest = min(input_list)
    return largest, smallest


"""Task5: List comprehension. """
def list_comprehension():
    """
    List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

    instead of using a for loop like this
    evens = []
    for x in range(20):
        if x%2 ==0:
            evens.append(x)
    print(evens)
    """
    # range(start, end, step) using this instead
    evens = [x for x in range(20) if x % 2 == 0]
    odds = [x for x in range(1, 20, 2)]
    return odds, evens


"""Task6: Experimenting with functions - map, filter, reduce. """
def square(n):
    return n ** 2


def even(n):
    """ Returns true if n is an even number"""
    return n % 2 == 0


def even2(n):
    return n if n % 2 == 0 else 'no'


def multiply(x, y):
    return x * y


def myfunc(a, b):
    """ adds the numbers or the characters or the strings """
    return a + b


def string_to_list(string):
    """ Splits every character and adds it to the list """
    newlist = list(string)
    return newlist


"""Task7: String Formatting. """
def what_is_a():
    a = 5
    if a > 0:
        a = 6
    return 'a is {}'.format(a)


"""Task8: Find the problem with this function. """
def find_the_problem(a):
    # The problem is that else: will never be executed because the elif condition is always true,
    # the 'else' block will never get executed.
    if a > 5:
        print('a')
    elif True:
        print('b')
    else:
        print('c')


"""Task9: What will be the output of this function? """
def find_output():
    a = 1/3
    b = 3/1
    return a * b


"""Task10: What will be the output of this function? """
def find_output2():
    a = '2'
    b = '2'
    return a + b


"""Task11: Exploring dictionaries - keys and values. """
def dictionary_exploration():
    x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    x['three'] = 42
    for keys, values in x.items():
        print('k: {}, v: {}'.format(keys, values))
    return '\n'


"""Task12: List from range. """
def range_list():
    x = list(range(5))
    x[3] = 43
    for i in x:
        print('i is {}'.format(i))
    return '\n'


"""Task13: Exploring Isinstance. """
def task_isinstance():
    # you can use the IS operator if you want to know if 2 objects are the same object
    # if you want to know if a particular object is of what type use isinstance if you want to print it use type
    x = (1, 'two', 3.0, [4, 'four'], 5)
    print('x is of type:', type(x))
    if isinstance(x, tuple):
        return True
    else:
        return False


def main():
    sun = Star()
    print(sun.description, '\n')

    print('Example00: More List Comprehension Examples. ')
    vals = [25, 30, 33, 35]
    new_vals = [val + 32 for val in vals]
    print(new_vals, '\n')

    print([i * 3 for i in range(5)], '\n')
    print([i for i in range(5) if i > 2], '\n')

    print('Example01: String Slicing. ')
    strng = "hellotherecat"
    for i in range(len(strng) - 2):
        print(strng[i:i])
        print(strng[i:i + 2], '\n')

    print('Example02: Enumerate Example. ')
    letters = ['a', 'b', 'c']
    for index, value in enumerate(letters):
        print(index, ':', value)
    print('\n')

    print("Example03: Dictionary Example. ")
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
    print(d['two'], '\n')

    print('Example04: String Formatting. ')
    x = 'seven {} {}'.format(8, 9)
    print('x is {1} {0}'.format(8, 9))

    # adds 8 spaces to the right of 9 - 9 digits in total
    z = 'seven "{1:<9}" "{0}"'.format(8, 9)
    print(z, '\n')

    # adds 8 spaces to the right of 9 and 6 spaces to the left of 8 - 9 digits and 7 digits each
    y = 'seven "{1:<9}" "{0:>7}"'.format(8, 9)
    print(y, '\n')

    # adds 8 zeros to the right of 9 and 6 zeros to the left of 8
    u = 'seven "{1:<09}" "{0:>07}"'.format(8, 9)
    print(u, '\n')

    # adds 8 zeros to the right of 9 and 6 zeros to the left of 8
    x2 = 'seven "{1:<09}" "{0:>07}"'.format(8, 123456)
    print(x2, '\n')

    a = 8
    b = 9
    x = f'seven {a} {b}'
    print('x is {}'.format(x))

    print('Example05: Python Types - Int and Float. ')
    # you get an int
    z1 = 7 // 3
    print(z1)

    # you get a float
    z2 = 7 / 3
    print(z2)

    # you get remainder - int
    z3 = 7 % 3
    print()

    # when working with money you want to use the decimals library of python
    # when numbers need to be treated as accurate decimals
    # The Decimal type is useful for accurate arithmetic calculation (e.g., when money is involved)

    a = Decimal('.10')
    b = Decimal('.30')
    x = a + a + a - b
    print('x is {}'.format(x))
    print(type(x))

    c = .10
    d = .30
    y = c + c + c - d
    print('x is {}'.format(y))
    print(type(y))

    # it's the Decimal from the decimal libray
    # <class 'decimal.Decimal'>

    print('Task1: Passing a variable number of arguments to a function using special symbols. ')
    print(make_dict(a=1, b=2), '\n')

    print('Task2: Explore with open -file. ')
    # func_file()

    print('Task3: Swap variables in a single line. ')
    a = 10
    b = 20
    print(swap_variables(a, b), '\n')

    print("Task4: find the max and the min values of a list using functions. ")
    list1 = [6, 12, 125, -25, 54, 23, 66, 77, 88, -12]
    print('largest, smallest numbers of list:', max_min_of_list(list1), '\n')

    print('Task5: List comprehension. ')
    print("odds:", list_comprehension()[0], '\nevens:', list_comprehension()[1], '\n')

    print('Task6: Experimenting with functions - map, filter, reduce and lambda functions. ')
    '''
    The map() function executes a specified function for each item in an iterable.
    The item is sent to the function as a parameter.
    Map allows us to pass in a separate function to apply to each element in our list.
    Rather than iterating through the list with the for loop, we can use map to concisely call this function
    for each item in numbers
    map(function, iterables)
    '''
    squares = list(map(square, list1))
    print(squares)

    print("In this case each element of the first list was added to the corresponding element in the 2nd list:")
    x = list(map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple')))
    print(x, '\n')

    print('In this case we filtered the list using the function even')
    even_nums = list(filter(even, list1))
    print(even_nums, '\n')

    a = "Hello There"
    print(string_to_list(a), '\n')

    print(even(2))
    print(even2(3))
    print(even2(24), '\n')

    ''' Reduce uses aggregate functions that actually reduce the size of the output '''
    product = reduce(multiply, list1)
    print(product, '\n')

    ''' Lambda functions
    One line statements that outline a generic operation to be performed
    '''

    squares2 = (lambda x: x ** 2)
    print('squares2L:', squares2(2))

    add3 = lambda d, e, f: d + e + f
    print("add3L:", add3(5, 7, 8))

    squares3 = list(map(lambda x: x ** 2, list1))
    print(squares3)

    even3 = list(filter(lambda x: x % 2 == 0, list1))
    print(even3)

    product2 = reduce(lambda x, y: x * y, list1)
    print(product2, '\n')

    print('Task7: String formatting. ')
    print(what_is_a(), '\n')

    print("Task8: Find the problem with this function. ")
    print(find_the_problem(6), '\n')

    print('Task9: What will be the output of this function? ')
    print(find_output(), '\n')

    print('Task10: What will be the output of this function? ')
    print(find_output2(), '\n')

    print('Task11: Exploring dictionaries - keys and values')
    print(dictionary_exploration())

    print("Task12: List from range. ")
    print(range_list())

    print("Task13: Isinstance. ")
    print(task_isinstance(), '\n')

    print()
    print()


if __name__ == '__main__':
    main()


# Which of the following code fragments is equivalent to np.recfromcsv(filename)?
# np.loadtxt(filename, delimiter=',')

# nrows = number of rows of the file to read
# titanic_data = pd.read_csv('titanic_csv', nrows =2, header =0)

# file = open('filename.txt', del='\t')
# file.close()


"""
file = open('filename.txt', mode ='r')
file.close()

        the code is the SAME AS:
with open('filename.txt', 'r') as file:

"""

"""
when the file has no header
s = pd.read_csv(file, header = None)
"""


# Which line is an expression but NOT a statement?
# True - This expression is not a stand-alone line of code.
# Incorrect x=x+1 This is a valid line of code, and is therefore both an expression and a statement.

# Which loop type will always complete at least one iteration?
# none of these answers (for while)
# In all Python loop types, the evaluation is done before the loop starts.

# if the function doesn't have a print or a return then:
# The function will return a value of none.
# When a return value is not specified explicitly, a function returns a None.

# Expressions and NOT statements: True False.

# Remember python will evaluate True the value of '0' because it is a non-empty string but,
# It will evaluate as false: 0, '', None, False, (), [], {}.

# The ID function returns a unique identifier for each Object.

# Accuracy is the true value of calculation.
# Precision is how close measure values are to each other.

