# Python practise examples and tasks 4

import datetime
import random
import time
# task28
import sys

# Why is UTF-8 a good choice for the default editor encoding?
# The Unicode character set in the editor should match the Unicode standard of Python 3.
# The character set of the editor should match Python's Unicode compliance.


"""Task 1: Assign multiple expressions together from right to left. """
def multiple_assignment_expression():
    # parenthesis are there because they have to be,
    # you are not allowed to assign multiple expressions together unless you put them in parenthesis
    (a := (b := (c := (d := 0))))
    # d:= 0 is going to return 0
    # := goes from right to left
    # normal = goes from left to right
    # we assign a, b, c, d to be 0
    return a, b, c, d


"""Task2: Explore string formatting. """
def equals_debugging():
    str_value = "other 😊"
    num_value = 1234
    print(f'the value is {str_value}')
    print(f'{str_value = }')  # for debugging
    print(f'{num_value % 2 = }')
    print("\n")


"""Task3: Explore string formatting 2. """
def conversions():
    str_value = "other 😊"
    print(f'{str_value!a}')  # converts non ascii characters to an ascii version
    print(f'{str_value!s}')  # string conversion used for formatting
    print(f'{str_value!r}')  # repr
    print("\n")


"""Task4: Explore string formatting using a class. """
# empty class
class MyClass:
    # all it does is define a format method which takes a format_spec and returns a string
    def __format__(self, format_spec) -> str:
        print(f'Myclass __format__ called with {format_spec=!r}')
        return "Myclass()"


"""Task5: Explore string formatting 3. """
def formatiing():
    num_value = 123.456
    now = datetime.datetime.utcnow()
    print(f'{now =: %Y-%m-%d}')  # format for datetimes
    print(f'{num_value:.2f}')  # 2 decimal places
    # blah blah %%MYFORMAT%% is a  passed as an argument, the format_spec argument
    print(f'{MyClass(): blah blah %%MYFORMAT%%}')
    nested_format = ".2f"
    print(f'{num_value:{nested_format}}')
    print("\n")

# in Python an assignment (d = 8) is not an expression, it's a statement
# in other languages assignments are also expressions and return d back to you.
# python expressions were added in 3.8


"""Task6: Explore  chained assignments - multiple equal signs. """
def multiple_assignment():
    c = d = e = f = []
    print(c, d, e, f)
    print("\n")


"""Task7: Tuple unpacking. """
def tuple_assignment():
    a, b = 1, 2
    print(a, b)
    print("\n")


"""Task8: More advanced unpacking. """
def tricky_assignments():
    # recursive cyclic structure   ... = cyclic reference
    # a becomes a member of its self b = []
    a, b = a[:] = [[]], []
    print(a, b)
    # tmp = [[]], []
    # a, b = tmp
    # Assigns the contents of a to [[]], []
    # a[:] = temp
    # we can confirm this using:
    # shows us that the first element of a is a, confirming that we have this cyclic reference
    print(a is a[0])
    print("\n")


"""Task9: More advanced unpacking 2. """
def tricky_assignemnt2():
    a, b = a[b] = a = [1, 2, 3], 2
    print(a, b)
    print("\n")


# dynamically adding values v1
class Person:
    pass


def useful_function(x):
    return x * x


class UsefulClass:
    def __init__(self, x):
        self.x = x


def do_it():
    for i in range(7):
        print(useful_function(i))


person = Person()

first_key = 'first'
first_val = 'Corey'

# setattr is able to use the value of a variable
# pass in the object that we want to set an attribute on
setattr(person, first_key, first_val)

# we want to get the first attribute here
first = getattr(person, first_key)


# v2
class Person2:
    pass


person2 = Person()

person_info = {'first': 'Corey', 'last': 'Schafer'}

# the keys will be equal to the keys and the values to the values eg corey for value
for key, value in person_info.items():
    setattr(person2, key, value)


"""Task10: List-2 > has22. Given an array of ints, return True if the array contains a 2 next to a 2 somewhere. """
def has22(nums):
    for x in range(len(nums) - 1):
        if (nums[x] == 2) and (nums[x + 1] == 2):
            return True
    return False


def has22_v2(nums):
    return any(x == y == 2 for x, y in zip(nums, nums[1:]))


"""Task11: List-2 > sum67. Return the sum of the numbers in the array, except ignore sections of numbers starting with 
a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers. """
def sum67(nums):
    result = 0
    startadding = True
    for val in nums:
        if val == 6:
            startadding = False
        if startadding:
            result += val
        if val == 7:
            startadding = True
    return result


"""Task12: List-2 > sum13. Return the sum of the numbers in the array, returning 0 for an empty array. Except the number
 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count. """
def sum13(nums):
    result = 0
    pause = False
    for num in nums:
        # if pause == False and num != 13:
        if not pause and num != 13:
            result += num
        if num == 13:
            pause = True
        else:
            pause = False
    return result


"""Task13: List-2 > centered_average. Return the "centered" average of an array of ints, which we'll say is the mean 
average of the values, except ignoring the largest and smallest values in the array. If there are multiple 
copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce 
the final average. You may assume that the array is length 3 or more. """
def centered_average(nums):
    sum1 = 0
    for element in nums:
        sum1 += element
    return (sum1 - min(nums) - max(nums)) / (len(nums)-2)


"""Task14: List-2 > big_diff. Given an array length 1 or more of ints, return the difference between the largest and 
smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or 
larger of two values. """
def big_diff(nums):
    return max(nums) - min(nums)


"""Task15: List-2 > count_evens. Return the number of even ints in the given array. Note: the % "mod" operator computes 
the remainder, e.g. 5 % 2 is 1."""
def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count


"""Task16: String-2 > xyz_there. Return True if the given string contains an appearance of "xyz" where the xyz is not 
directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not."""
def xyz_there(str1):
    for i in range(len(str1)):
        if str1[i] != '.' and str1[i+1:i+4] == 'xyz':
            return True
        if str1[0:3] == 'xyz':
            return True
    return False


"""Task17: String-2 > end_other. Given two strings, return True if either of the strings appears at the very end of the 
other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string. """
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return b.endswith(a) or a.endswith(b)


def end_other_v2(a, b):
    a = a.lower()
    b = b.lower()
    return a[-(len(b)):] == b or a == b[-(len(a)):]


"""Task18: Fortune Cookie. """
def fortune_cookie():
    # includes 1 to 100
    lucky_number = random.randint(1, 100)
    fortune_number = random.randint(1, 3)
    fortune_text = ''

    if fortune_number == 1:
        fortune_text = 'You will have a great day!'
    if fortune_number == 2:
        fortune_text = 'Today will be tough...but worth it'
    if fortune_number == 3:
        fortune_text = 'You will get married this year!'

    return f"{fortune_text} Your Lucky Number is {lucky_number}"


"""Task19: Lists: Add, insert, delete. """
def list_manipulation():
    fav_movies = ['Sandlot', 'The Lego Movie', 'Dune']
    print(fav_movies)
    # gets added to the back always
    fav_movies.append('Iron Man')
    print(fav_movies)
    # add an item in a specific place  - position 2
    fav_movies.insert(1, 'Batman')
    print(fav_movies)
    # deleting an item from list - remove 'The Lego Movie'
    del(fav_movies[2])
    return fav_movies


"""Task20: Exploring dictionaries. """
def exploring_dictionaries():
    cats = {"Jane": 6, "Tom": 14, "Sara": 8}
    # adding a key and value
    cats["Wilson"] = 1
    del(cats["Tom"])
    print(len(cats))
    return cats


"""Task21: String length counter. """
def str_analysis():
    text = """Four score and seven years ago our Fathers. -- , and seven seven ago seven and hi hi."""
    print(text.split())
    print("We have " + str(len(text.split())) + " words in our string.")

    # lets count how many times we have each word
    word_count = {}

    for word in text.lower().split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


"""Task22: Guess game. """
def guess_game():
    print("Hi! Welcome to the guessing game! Please guess a number between 1 and 100. ")
    time.sleep(2)
    guess = int(input("Pick your number... "))
    correct_number = random.randint(1, 100)
    counter = 1
    time.sleep(1)
    while guess != correct_number:
        time.sleep(1)
        counter += 1
        if guess > correct_number:
            guess = int(input("Too high! ,'\n' What is your next guess?: "))
        else:
            guess = int(input("Too low: ,'\n' What is your next guess?: "))
    # alternative
    return 'You got the right answer after {} tries! :) '.format(counter)
    #return f"You got the right answer after {counter} tries! :) "


"""Task23: String-2 > cat_dog. Return True if the string "cat" and "dog" appear the same number of times 
in the given string."""
def cat_dog_v1(strg):
    count_cat = 0
    count_dog = 0
    for i in range(len(strg) - 2):
        if strg[i:i + 3] == 'dog':
            count_dog += 1
        if strg[i:i + 3] == 'cat':
            count_cat += 1
    return count_cat == count_dog


def cat_dog_v2(strng):
    if strng.count('cat') == strng.count('dog'):
        return True
    else:
        return False


"""Task24: String-2 > count_hi. Return the number of times the string "hi" appears anywhere in the given string. """
def count_hi(strng):
    # can also be done as v1 of Task 23
    return strng.count('hi')


"""Task25: String-2 > double_char. 
Given a string, return a string where for every char in the original, there are two chars. """
def double_char(str):
    result = ''
    for char in str:
        result += char * 2
    return result


"""Task26: Fibonacci. """
def fibonacci():
    a, b = 0, 1
    while b < 1000:
        # end = ' ' makes the print function print in the same line
        # The flush() method in Python file handling clears the internal buffer of the file
        print(b, end=' ', flush=True)
        a, b = b, a + b
    return ''


"""Task27: Is prime?"""
def list_primes():
    for n in range(40):
        if isprime(n):
            print(n, end=' ', flush=True)
    return ''


def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True


"""Task28: Handling Exceptions. """
def exception_test(inpt):
    try:
        int(inpt)
    # this will be executed if the try fails - if it catches an exception
    except ValueError:
        # instead of getting that error we capture it and we can continue
        return'I caught a value error'
    except ZeroDivisionError:
        return'don\'t divide by zero'
    # unknown error - we can have a default exception
    except:
        # sys.exec_info() alone gives you info but adding a [1] gives you the actual error
        return f'unknown error: {sys.exc_info()[1]}'
    # if it succeeds - this is only executed if we don't get an error
    else:
        return'good job, {}'.format(inpt)
    return ''


"""Task29: Swap the case from the string. """
def string_swap_case():
    print('Hi {}'.format(42 * 7))
    return 'Hello, World'.swapcase()


"""Task30: String Formatting. """
def str_frmt():
    x = 42 * 747
    # adding commas for thousands separations
    print('the number is {:,}'.format(x).replace(',', '.'))
    # 3 decimal places
    print('the number is {:.3f}'.format(x))
    y = 42
    # hexadecimal: x, octal: o, binary: b
    print('the number is {:x}'.format(y))
    print(f'the number is {y:b}')
    return '\n'


"""Task31: String splitting and joining. """
def split_join_examples():
    s2 = """This is a        long
    string. """
    # splits on spaces and new lines by default - also puts them in a list
    print(s2.split())
    # splits them on i | i is gone - we get spaces and new lines
    print(s2.split('i'))

    s1 = "This is a    string"
    # remember we split it by spaces & we end up with a list
    l = s1.split()
    # we join the list l using -:- remember, join takes a list or a tuple as its argument
    s3 = '-:-'.join(l)
    print(s3)
    return '\n'


"""Task32: Opening files . """
def open_file_func():
    # it takes a file name and open that file & it returns a file object
    # the file object itself is an iterator, and so we can use a for loop and get 1 line at a time
    # without having to buffer the entire file in the memory
    # default mode = 'r' - read mode | 'w' - write mode
    f = open('lines.txt', 'r')
    # with write mode - it empties the file if the file is not empty, and it starts at the beginning and writes
    # over the file. If the file doesn't exist, it creates it.
    # 'a' is append mode, this is just like write, but if the file already has some content in it,
    # it starts at the end of the file + it does not empty the file + it does not create the file.
    # There's an optional plus, which you can use with any of these modes, which will allow you to both read and write.
    # And there's an optional letter B or T, which will specify binary or text mode.

    # stripping the new lines and white space at the end of each line
    for line in f:
        print(line.rstrip())


"""Task33: Opening files2 . """
def open_file_func2():
    # open in read and text mode - default mode
    infile = open('lines.txt', 'rt')
    # opening the output file in write and text mode - it will be created
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        # for each line in the infile file we strip the line ending from the line and output them to outfile
        print(line.rstrip(), file=outfile)
        # same as above
        # outfile.writelines()

        # we print a dot & we write on the same line | flush to flush the output the buffer on some OS its needed
        # prints on terminal - not on the file
        print('.', end='', flush=True)
    # close the file
    outfile.close()
    return '\n'


"""Task34: Opening binary files . """
def open_binary_files():
    # open the file using b - binary | if you try text we get error
    # because the very first byte of the file is not a valid unicode character
    # CR+LF character(s) are used by the Windows operating system to terminate a text line
    infile = open('berlin.jpg', 'rb')
    outfile = open('berlin-copy.jpg', 'wb')
    # the loop will run until we tell it to break
    while True:
        # we read a buffer of 10k bytes as the size of the buffer | size of chunks we read and write
        # A small buffer will fit into a smaller memory, but will require more iterations to process.
        buf = infile.read(10240)
        # if we have bytes - True | else false and break
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else:
            break
    outfile.close()
    return '\n'





def main():
    print(multiple_assignment_expression(), '\n')

    equals_debugging()

    conversions()

    formatiing()

    multiple_assignment()

    tuple_assignment()

    tricky_assignments()
    tricky_assignemnt2()

    print("v1:", person.first)

    print("v2:", person2.first)
    print("v2:", person2.last)

    for key in person_info.keys():
        print("v2 for loop:", getattr(person2, key))

    print('\n')
    print('Task10: Given an array of ints, return True if the array contains a 2 next to a 2 somewhere. ')
    print(has22([2, 1, 2]))  # False
    print(has22([1, 2, 1, 2]))  # False
    print(has22([]))  # False
    print(has22_v2([4, 2, 4, 2, 2, 5]), '\n')  # True

    print('Task11: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and '
          'extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.')
    print(sum67([1, 2, 2]))  # 5
    print(sum67([1, 2, 2, 6, 99, 99, 7]))  # 5
    print(sum67([1, 6, 7, 7]))  # 1+7=8
    print(sum67([6, 7, 1, 6, 7, 7]))  # 1+7=8
    print(sum67([6, 8, 1, 6, 7]))  # 0
    print(sum67([]), '\n')

    print('Task12: Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is '
          'very unlucky, so it does not count and numbers that come immediately after a 13 also do not count. ')
    print(sum13([13, 1, 2, 13, 2, 1, 13]))  # 2+1=3
    print(sum13([1, 2, 13, 2, 1, 13]))  # 1+2+1=4
    print(sum13([5, 13, 2]), '\n')  # 5

    print('Task13: List-2 > centered_average. ')
    print(centered_average([-10, -4, -2, -4, -2, 0]))  # 3
    print(centered_average([0, 2, 3, 4, 100]))  # 3
    print(centered_average([-10, -4, -2, -4, -2, 0]), '\n')  # -3

    print("Task14: List-2 > big_diff. ")
    print(big_diff([5, 1, 6, 1, 9, 9]))  # 8
    print(big_diff([7, 7, 6, 8, 5, 5, 6]))  # 3
    print(big_diff([10, 0]))  # 10
    print(big_diff([2, 2]), '\n')  # 0

    print("Task15: List-2 > count_evens. ")
    print(count_evens([2, 11, 9, 0]))  # 2
    print(count_evens([1, 3, 5]))  # 0
    print(count_evens([2, 5, 12]), '\n')  # 2

    print('Task16: String-2 > xyz_there. ')
    print(xyz_there('abc.xxyz'))  # True
    print(xyz_there('1.xyz.xyz2.xyz'))  # False
    print(xyz_there('abc.xyzxyz'))  # True
    print(xyz_there('abc.xyz'), '\n')  # False

    print('Task17: String-2 > end_other. ')
    print(end_other('abcXYZ', 'abcDEF'))  # False
    print(end_other('Z', '12xz'))  # True
    print(end_other_v2('Hiabcx', 'bc'))  # False
    print(end_other_v2('Hiabc', 'bc'))  # True
    print(end_other_v2('abc', 'abXabc'), '\n')  # True

    print("Task18: Fortune Cookie. ")
    print(fortune_cookie(), '\n')

    print('Task19: Lists: Add, insert, delete. ')
    print(list_manipulation(), '\n')

    print('Task20: Exploring dictionaries.')
    print(exploring_dictionaries(), '\n')

    print("Task21: String length counter. ")
    print(str_analysis(), '\n')

    print("Task22: Guess Game. ")
    # print(guess_game(), '\n')

    print("Task23: String-2 > cat_dog. ")
    print(cat_dog_v1('1cat1cadodog'))  # True
    print(cat_dog_v2('catcat'))  # False
    print(cat_dog_v1('c'))  # True
    print(cat_dog_v2('catxdogxdogxca'), '\n')  # False

    print("Task24: String-2 > count_hi. ")
    print(count_hi('Hi is no HI on ahI'))  # 0
    print(count_hi('ABChi hi'), '\n')  # 2

    print('Task25: String-2 > double_char. ')
    print(double_char('Hi-There'), '\n')  # HHii--TThheerree

    print('Task26: Fibonacci. ')
    print(fibonacci(), '\n')

    print('Task27: Is prime?. ')
    print(list_primes(), '\n')  # also returns None

    print("Task28: Handling Exceptions. ")
    c = 'foo'; z = 5/3
    print('foo:', exception_test(c))
    print('z:', exception_test(z), '\n')

    print("Task29: Swap the case from the string. ")
    print(string_swap_case(), '\n')

    print("Task30: String Formatting. ")
    print(str_frmt())

    print("Task31: String splitting and joining. ")
    print(split_join_examples())

    print("Task32: Opening files . ")
    # open_file_func()

    print("Task33: Opening files2 . ")
    # open_file_func2()

    print("Task34: Opening binary files . ")
    # open_binary_files()


# dunder == double underscore | allows you to check whether the file is being run as a script or not
# __main__ = script | if __name__ = '__main__' is used to signal that this file is a script and you can run it
# if your file doesn't contain it then assume the file is used as a library or you should import it.
if __name__ == '__main__':
    main()

# Triple quotes preserve the tabs, line breaks, and other white spaces in the defined string.
