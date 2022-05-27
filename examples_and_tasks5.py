# Python practise examples and tasks 5

from functools import reduce
from decimal import *
import time

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


"""Task14: Conditional Assignments. """
def conditional_assignments():
    # 0 = False
    hungry = 0
    x = 'Feed the bear now!' if hungry else 'Do not feed the bear. '
    return x


"""Task15: Return the number of digits, assume number is between 0 and 999,999. """
def digits(x):
    d = 1
    if x >= 10:
        d = d+1
    if x >= 100:
        d = d+1
    if x >= 1000:
        d = d+1
    if x >= 10000:
        d = d+1
    return d


"""Task16: Bitwise Operators. & | ^ << >>. """
def bitwiseoperators():
    """ & and, | or, ^ xor, << shift left, >> shift right # these operators operate on bits (in numbers) """
    x = 0x0a
    y = 0x02
    # z = x | y or result 00001010
    z = x & y
    # 02x gives us a 2 character string and its in hexadecimal and has a leading 0
    # 0 leading, 2 characters wide, x is for hexadecimal display of an integer value
    print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
    # difference here is that the field is 8 characters wide, b is for binary representation of the value
    print(f'(bin) y is {x:08b}, y is {y:08b}, z is {z:08b}')
    # the first four zeros are the hexadecimal 0, next 4 digits are a which is 10 in decimal and 1010 in binary hex
    # x 00001010, y 00000010, z 00000010
    return '\n'


"""Task17: Additional controls - while, break, continue, if. """
def authorize_password(input):
    secret = 'password'
    pw = ''
    auth = False
    count = 0
    max_attempt = 5

    while pw != secret:
        count += 1
        if count > max_attempt:
            # stops the while loop
            break
        pw = input(f"{count}: What's the secret word? ")
        if count == 3:
            # skips the try and goes back to the start of the while loop
            continue
    else:
        auth = True
    return "Authorized" if auth else "calling the FBI... "


"""Task18: Function that takes multiple inputs. """
def kitten(*args):
    # *args means a variable length argument input

    # we check if the length is greater is zero, if there are inputs: len(args) = 1
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meow.')


"""Task19: Functions with keyword (named) arguments. """
def kitten2(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says'.format(k, kwargs[k]))
    else: print('Meow.')


"""Task20: Generator functions, inclusive range. """
def inclusive_range(*args):
    # A generator is a special type of function that is useful for creating a series of values
    # returns all the values from 0 to number stated - (not like range which returns 0 to n-1, we use yield
    numargs = len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        # yield is like return except, its for generators, it yields a value and function continues
        # doesn't stop the function like return
        yield i
        i += step


"""Task21: Wrappers. Function within a function. """
def f1(f):
    # we cannot call f2 directly because its scope is inside the function f1
    def f2():
        print('this is f2', 'this is before the function call')
        # these next 2 lines are for the decorators
        f()
        print('this is f2', 'this is after the function call')
    # this function runs f2 because the return value from f1 is the object f2
    return f2
    # we cannot call f2 directly! - we will get a syntax - name error
    # so f1 is a wrapper for f2


"""Task22: Decorators. """
# it takes function which is defined directly after it. syntax is decorator and below function definition
@f1
def f3():
    print('this is f3')


"""Task23: Decorators2. """
def elapsed_time(f):
    # wraps the passed function in this case big_sum() that we have inputted and prints the elapsed time
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper


# because it has this decorator, it's actually wrapped in the elapsed_time wrapper
@elapsed_time
def big_sum():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')


"""Task24: Decorators 3."""
def F1(f):
    print('A')
    def F2():
        print('B')
        f()
        print('C')
    print('D')
    return F2


@F1
def F3():
    print('E')


"""Task25: Generator functions 2. """
def generator(start,stop):
    # x will be passed by value - ie a copy of x will be passed and therefore when the parameter a is modified
    # in func, x will stay intact, x =0 and a = 1

    # whereas b will be passed as a reference - ie a pointer to that list so b will be a list with a value [0]
    # and therefore the function will edit the value of b and make it 1
    while start <= stop:
        yield start
        print(f'start={start}')
        start += 1


"""Task26: Find the output of the function. """
def Func(a, b):
    a = 1
    b[0] = 1


"""Task27: Exploring the input parameters of print. """
def print_params():
    # default separator#' ', which means between 2 set of quotes there is a space
    print('Hi', 'There', end='-')
    # default end='\n', which means between 2 set of quotes there is a new line
    print('Hi', 'There', sep='|')


"""Task28: List Slicing. """
def list_slicing():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    # start end step - starts from Paper and then jumps 2 places to Lizard
    print(game[1:5:2])
    # prints 2nd and 3rd
    print(game[1:3])


"""Task29: List manipulation. """
def list_manipulation():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock', 'Poker']
    # gets the index of the item Paper in the game list
    i = game.index('Paper')
    print('index: {}'.format(i))
    # adds the item Computer at the end of the list
    game.append('Computer')
    print('Appending computer in list:', game)
    # inserts the item TV at index 2 of the list
    game.insert(2, 'TV')
    print('Inserting at position 3 the item TV:', game)
    # removes the item Computer from the list
    game.remove('Computer')
    print('Removing the item computer from the list:', game)
    # removes an item from the end list - pop also returns the removed item
    game.pop()
    print('Removing the last item of the list:', game)
    # pop can also be used to remove an item at a particular index
    game.pop(2)
    print('Removing the item at position 3:', game)
    # you can also use del to delete an item in the list or a slice of the list
    del game[0:1]
    print('Delete slicing [0:1] from the list:', game)
    del game[1]
    print('deleting the 2nd item in list:', game)
    # prints out this list joined by comma space between the elements
    print(', '.join(game))
    print('length of list:', len(game))


"""Task30: Using Dictionary items and keys. """
def print_dict(dictionary):
    for x in dictionary: print(f'{x}: {dictionary[x]}')
    # changing value of a key in dict / or adding a new one
    dictionary['lion'] = 'I am a lion'


"""Task31: Dictionary. """
def print_dict2(dictionary):
    for k, v in dictionary.items(): print(f'{k}: {v}')

    # there is also .keys - where you can access the keys
    # for k in dictionary.keys(): print(f'key: {k}')

    # there is also .values - where you can access the items
    # for v in dictionary.values(): print(f'key: {v}')


"""Task32: Experimenting with sets. """
def sets_exp():
    a = set("We are gonna need a bigger boat. ")



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

    print('Task14: Conditional Assignments. ')
    print(task_isinstance())

    print("Task15: Return the number of digits, assume number is between 0 and 999,999. ")
    print(digits(9933))
    print(digits(99), '\n')

    print("Task16: Bitwise Operators. & | ^ << >>. ")
    print(bitwiseoperators())

    print("Task17: Additional controls - break !=. ")
    print(authorize_password(input))

    print("Task18: Function that takes multiple inputs. ")
    x = ['world', 'meow', 'grrr', 'purr']
    print(kitten(*x))
    print(kitten('meow', 'grrr', 'purr'), '\n')

    print("Task19: Functions with keyword (named) arguments. ")
    x_dict = dict(Buffy='meow', Zilla='girr', Angel='rawr')
    print('dictionary: {}'.format(x_dict))
    print(kitten2(Buffy='meow', Zilla='girr', Angel='rawr'))
    print(kitten2(**x_dict), '\n')

    print("Task20: Generator functions, inclusive range. ")
    for i in inclusive_range(25):
        print(i, end=' ')
    print('\n')

    print("Task21: Wrappers. Function within a function. ")
    # remove the input argument for f1, make it def f1():
    #x12 = f1()
    #x12()
    print('\n')

    print("Task22: Decorators. ")
    x13 = f1(f3)
    x13()
    print('\n')

    print("Task23: Decorators2. ")
    big_sum()
    print('\n')

    print("Task24: Decorators 3.")
    # F1 is called first, returns the reference to F2, and then F2 is started and calls F3 along the way.
    print(F3())
    print('\n')

    for counter in generator(3, 4):
        print(f'counter={counter}')
    print('\n')

    print("Task26: Find the output of the function. ")
    x = 0
    y = [0]
    Func(x, y)
    print(x, y)
    print('\n')

    print("Task27: Exploring the input parameters of print. ")
    print_params()
    print('\n')

    print("Task28: List Slicing. ")
    list_slicing()
    print('\n')

    print("Task29: List manipulation. ")
    list_manipulation()
    print('\n')

    print('Task30: Dictionary manipulation. ')
    animals = {'kitten': 'meow', 'puppy': 'puff', 'lion': 'rawr', 'dragon': 'kek', 'fly': 'zaga'}
    print_dict(animals)
    print('\n')

    print("Task31: Dictionary. ")
    # another way to make a dictionary - notice the difference in format!
    animals2 = dict(kitten='meow', puppy='puff', lion='rawr', dragon='kek', fly='zaga')
    print_dict2(animals2)
    print('lion says', animals2['lion'])
    # searching for a value in the dict - returns a boolean
    print('found!' if 'lion' in animals2 else 'nope!')
    # you can use the get method to return a value from a dictionary if you don't know if it exists
    # does not throw an error/exception like animals2['gozilla'] if it can't find the value
    print(animals2.get('gozilla'))
    print('\n')


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

# conditional operator that tests membership - in.
# The 'in' operator is used to test whether an item is a member of a collection.

# In which scenario does the convenience of the ternary conditional operator apply the most?
# A ternary operator specifies both sides of the condition in a single statement.
# When you want to run both 'if' and 'else' conditions in one line.

# When is a membership operator true?
# if a variable is a member of a collection.

# Arithmetic operators +,-,*,/,//,%,**,-,+ performed on ints

# Comparison operators <,>,<=,>=,==,=! compare a value of 2 operands

# Boolean operators: or,and,not,in,not in,is,is not  - test if a value is in or not in a set or identity of the objects

# A generator is a special case of function, that is useful for creating a series of values.

# A certain function func() is expecting an argument list.
# How would you call this function with a list of arguments specified in a tuple x?
# func(*x)

# When can an argument list be useful?
# When you need to call a function with a varying number of arguments.

