"""

6 Python Tips and Tricks YOU Should Know
https://www.youtube.com/watch?v=qEr9iRX4K0o

"""

from functools import reduce


class Astrobody:
    description = 'Natural entity in the observable universe.'


class Star(Astrobody):
    pass


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

def func_file():
    """ """
    with open('hello.txt', 'w') as file:
        file.write("hello!")

    print(file.closed)

    #end of asssessment


def swap_variables(a, b):
    """ Swaps the values of a and b in a single line - without the need for a 3rd variable """
    a, b = b, a
    return a, b


def max_min_of_list(input_list):
    largest = max(input_list)
    smallest = min(input_list)
    return largest, smallest


def list_comprehension():
    """
    List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

    instead of using a for loop like
    evens = []
    for x in range(20):
        if x%2 ==0:
            evens.append(x)
    print(evens)

    range(start, end, step)


    """
    evens = [x for x in range(20) if x % 2 == 0]
    odds = [x for x in range(1, 20, 2)]
    return odds, evens


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


def main():
    a = 10
    b = 20
    print(swap_variables(a, b), '\n')

    list1 = [6, 12, 125, -25, 54, 23, 66, 77, 88, -12]
    print('largest, smallest numbers of list:', max_min_of_list(list1), '\n')

    print("odds:", list_comprehension()[0], '\nevens:', list_comprehension()[1], '\n')

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

    sun = Star()
    print(sun.description, '\n')

    vals = [25, 30, 33, 35]
    new_vals = [val + 32 for val in vals]
    print(new_vals, '\n')

    print([i * 3 for i in range(5)], '\n')

    letters = ['a', 'b', 'c']
    for index, value in enumerate(letters):
        print(index, ':', value)
    print('\n')

    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
    print(d['two'], '\n')

    print(make_dict(a=1, b=2), '\n')

    print([i for i in range(5) if i > 2], '\n')

    func_file()

if __name__ == '__main__':
    main()
