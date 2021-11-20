# Python practise examples and tasks 2

import timeit
import numpy as np
import pandas as pd
import math
import statistics

"""Task1: Sum the numbers from 0 to n-1 in different ways. """
# although for and while loop are essentially doing the same, the while loop takes longer than the for loop to run
def while_loop(n=50_000_000):
    # when using large numbers we can use _ to make them easier to read
    i = 0
    s = 0  # sum
    # loop all numbers
    while i < n:
        s += 1
        i += 1
    return s


# python range doesnt create an array in memory - you can run it without any worries in memory constrains
def for_loop(n=50_000_000):
    s = 0  # sum
    # loop all numbers
    for i in range(n):
        s += 1
    return s


# built-in functions take even less time than loops
def sum_range(n=50_000_000):
    return sum(range(n))


# we use numpy functions instead of python functions because python is slow thus we use numpy which is writen in c,
def numpy_sum(n=50_000_000):
    return np.sum(np.arange(n))


# much faster because entire operation is written in c, this whole function is 1 c call,
# both the iteration and the adding itself is done in c.
# the downside is that arange creates a whole array in memory

# fastest way to calulate it is to use math knowledge - we are adding the first n-1 integers therefore: we can use this formula
def sum_math(n=50_000_000):
    return (n * (n - 1)) // 2


#   conclusion:
# the fastest way to loop in python is to:
# not to loop in python
# try to compute the answer mathematically ahead of time definitely do that
# loop in a c built in function such as numpy library
# call a c function that can do the looping
# use python builtin functions like sum or map
# use for loop
# use while loop


"""Task2: Multiple input arguments and parameters in funcs. """
# passing how ever many input parameters we want
def multiply(*numbers):
    total = 1
    for x in numbers:
        # same as total = total * x
        total *= x
    return total


# function with 2 input parameters, the second if not provided will be by default 1
# all optional parameters should come after the required parameters!!! *SOS*
def incriment(number, by=1):
    return number + by


# multiple variable input - we can pass multiple key value pairs or multiple keyword arguments to a function and
# python will automatically package them into a dictionary
def save_user(**user):
    # makes it a dictionary
    print(user)
    # you can also specify which key you want
    print(user["id"])
    return user


"""Task3: Scope - Global vs Local Variables. """
message = 'b'
# Scope - the region of the code where a variable is defined
def greet(name):
    # global message
    # avoid using the global inside the variable - easy to make mistakes and cause bugs

    # the scope of the variable message and name is the greet function, they are local variables inside the greet
    # function - they don't exist anywhere else
    message = "a"


"""Task4: Create a function that when passed an integer, will return Fizz if the int is divisible by 3,
Buzz if the int is divisible by 5, FizzBuzz if divisible by both 3 and 5 else the number. """
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


"""Task5: Concatenate 2 tuples. """
# create a function that concatenates 2 tuples
tup1 = (1, "a", True)
tup2 = (4, 5, 6, False)


def tupleconcat(tupl1, tupl2):
    # adds them in order first tup1 and then tup2 at its end
    return tupl1 + tupl2


"""Task6: Initialize a 5 by 5 numpy array with only zeros. """
def array5by5zeros():
    n1 = np.zeros((5, 5))
    return n1


"""Task7: Read a .csv file using Pandas. """
# def read_csv_file_pandas(file):
#     df = pd.read_csv(file)
#     return df


"""Task8: Create a Pandas Series from data. """
data = ["1", 2, "three", 4.0]
def createa_Pandas_Series(inputdata):
    series = pd.Series(inputdata)
    typeofseries = type(series)
    return series, typeofseries


"""Task9: Reverse a string. """
strng1 = "Hello"
strng2 = "My name is Johnas123"
def reverse_String(inputstrg):
    str_reverse = inputstrg[::-1]
    return str_reverse


"""Task10: Create a new column in pandas by using values from other column. """
a = [1, 2, 3]
b = [2, 3, 5]
d = {"col1": a, "col2": b}
def new_Column_Using_Values_ofOther_Columns(dict):
    df = pd.DataFrame(d)
    df["Sum"] = df["col1"] + df["col2"]
    df["Difference"] = df["col1"] - df["col2"]
    return df


"""Task11: Select columns in pandas and add them to a new dataframe. """
def add_Column_toNew_Dataframe(dataframe):
    # If there are two columns with the same name then both columns get copied to the new dataframe.
    print(dataframe.columns)
    newdataframe = dataframe[["col1"]]
    return newdataframe


"""Task12: Select columns in pandas and add them to a new dataframe. """
d2 = {"col1": [1, 2, 3], "col2": ["A", "B", "C"]}
def delete_Column_from_dataframe(inputdataframe):
    dataframe2 = pd.DataFrame(inputdataframe)
    # axis = 1 means columns, default - axis = 0 means rows
    dataframe2 = dataframe2.drop(["col1"], axis=1)
    return dataframe2


"""Task13: Warmup-1 > monkey_trouble. Return True if both smile or neither is smiling. """
def monkey_Trouble(a_smile, b_smile):
    if (a_smile and not b_smile) or (not a_smile and b_smile):
        return False
    else:
        return True


"""Task14: Given two int values, return their sum. Unless the two values are the same, then return double their sum. """
def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    else:
        return a + b


"""Task15: Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21. """
def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2


"""Task16: We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble. """
def parrot_Trouble(talking, hour):
    # or just return (talking and (hour < 7 or hour > 20))
    if (talking and hour < 7) or (talking and hour > 20):
        return True
    else:
        return False


"""Task17: Given a string, return a new string where the first and last chars have been exchanged. """
def str_Replace_Front_Back(str):
    if len(str) <= 1:
        return str

    mid = str[1:len(str) - 1]  # can be written as str[1:-1]

    # last + mid + first
    return str[len(str) - 1] + mid + str[0]


"""Task18: Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged. """
def not_String(str):
    if str[0:3] == "not":
        return str
    else:
        return "not " + str


"""Task19: Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive). """
def missing_char(str, n):
    newstr = str.replace(str[n], "")
    return newstr


"""Task20: Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front. """
def front3(str):
    str_new = 3 * str[0:3]
    return str_new


"""Task21: Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings. """
def string_match(a, b):
    # Figure which string is shorter.
    shorter = min(len(a), len(b))
    count = 0

    # Loop i over every substring starting spot.
    # Use length-1 here, so can use char str[i+1] in the loop
    # range(len(b)-1) or range(len(a)-1) also works
    for i in range(shorter - 1):
        a_sub = a[i:i + 2]
        b_sub = b[i:i + 2]
        if a_sub == b_sub:
            count = count + 1
    return count


"""Task22: Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere. """
def array123(nums):
    # Note: the range() of a negative value will not iterate and go on to return False immediately
    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False


"""Task23: Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4. """
def array_front9(nums):
    for i in range(0, len(nums)):
        if nums[i] == 9 and i < 4:
            return True
    return False


"""Task24: Write a function that computers the area of a circle with radius r. Using MAP function. """
def area(r):
    return math.pi * (r ** 2)


"""Task25: Write a function that converts the temperature from celsius to fahrenheit within a list. """
# note that the list has both location and temperature
temps = [('Berlin', 29), ('Cairo', 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Tokyo", 27), ("New York", 28),
         ("London", 22), ("Beijin", 32)]
def c_to_f1(data):
    c_to_f = lambda data: (data[0], (9 / 5) * data[1] + 32)
    return (list(map(c_to_f, temps)))


"""Task26: Find all data above the average. Use filter. """
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
def filter_data(input_data):
    return list(filter(lambda x: x > avg, input_data))


"""Task27: Remove missing data from list. """
countries = ["", "Argentina", "Brazil", "Chile", "", "Colombia", "", "Ecuador", "", "", "Venezuela"]
def rmv_msing_data(list1):
    # in this case filter filters the following data: "", 0, 0.0, 0j, [], (), {}, False, None
    # these are instances which signal they are empty
    return list(filter(None, list1))


"""Task28: Extract values from 2 lists at the same time using the ZIP function. """
x_list = [1, 2, 3]
y_list = [4, 5, 6]
def loop_over_2_lists(list1, list2):
    # zip takes 2 or more lists and zips them together in a tuple
    for z in zip(list1, list2):
        print(z)
    # this is the way to extract them from a tuple
    for x, y in zip(list1, list2):
        print(x, y)
    return "\n"


"""Task29: Switch over the values of 2 variables. """
def switch_variables(x, y):
    x, y = y, x
    return "After: x = %d, y = %d" % (x, y)


"""Task30: Try to get of find a value from dictionary. Use the GET function. """
ages = {'Mary': 31, 'Jonathan': 28}
ages2 = {'Mary': 31, 'Jonathan': 28, 'Dick': 51}
def find_value_in_dict(dict):
    age = dict.get('Dick', 'Unknown')
    return f'Dick is {age} years old.'


"""Task31: The correct way to open a file and print the output. Using the WITH function. """
def open_read_file(file):
    # with open(file) as f:
    with open(f'{file}') as f:
        for line in f:
            print(line)
    return "\n"


"""Task32: Build a function that converts the input to integer if possible. """
def int_conv(x):
    try:
        print(int(x))
    except:
        print('Conversion failed!')
    else:
        print('Conversion successful!')
    finally:
        # always executed
        print("Done")
    return ""

def main():
    print("Task1: Find the fastest way to compute the sum of the first 50 000 000 integers. ")
    # print('for pure loop\t\t', timeit.timeit(for_loop, number =1))
    # print('built in sum func\t\t', timeit.timeit(sum_range, number =1))
    # print('built in sum func\t\t', timeit.timeit(numpy_sum, number =1))
    # print('built in sum func\t\t', timeit.timeit(sum_math, number =1))
    # , formats the output number to have , and separate every 3 numbers
    print(f'{numpy_sum():,}')
    # print(sum_math())
    print("\n")

    print("Task2: Functions with many or a variable amount of input parameters *args and **args. ")
    print(multiply(2, 3, 4, 5))
    # function with 2 input parameters, the second if not provided will be by default 1
    print(incriment(2, 5))
    print(incriment(2))
    save_user(id=1, name="John", age=22)
    print("\n")

    print("Task3: Scope of variables. ")
    # for example we have a global variable
    greet("John")
    print(message, "\n")

    print("Task4: The fizz_buzz function. ")
    print(fizz_buzz(15), fizz_buzz(3), fizz_buzz(5), fizz_buzz(4), "\n")

    print("Task5: Concatenate 2 tuples together. ")
    print(tupleconcat(tup1, tup2), "\n")

    print("Task6: Initialize a 5 by 5 numpy array with only zeros. ")
    print(array5by5zeros(), "\n")

    print("Task7: Read a .csv file using pandas. ")
    # print(read_csv_file_pandas(file.csv))
    print("\n")

    print("Task8: Create a Pandas Series from data. ")
    print(createa_Pandas_Series(data), "\n")

    print("Task9: Reverse the string. ")
    print(reverse_String(strng1))
    print(reverse_String(strng2), "\n")

    print("Task10: Create a new column in pandas by using values from other column. ")
    print(new_Column_Using_Values_ofOther_Columns(d), "\n")

    print("Task11: Select columns in pandas and add them to a new dataframe. ")
    dfnew = (new_Column_Using_Values_ofOther_Columns(d))
    print(add_Column_toNew_Dataframe(dfnew), "\n")

    print("Task12: Select columns in pandas and add them to a new dataframe. ")
    print(delete_Column_from_dataframe(d2), "\n")

    print("Task13: Warmup-1 > monkey_trouble. Return True if both smile or neither is smiling. ")
    print(monkey_Trouble(True, True))
    print(monkey_Trouble(False, False))
    print(monkey_Trouble(False, True))
    print(monkey_Trouble(True, False), "\n")

    print("Task14: Given two int values, return their sum. Unless the two values are the same, then return double their sum. ")
    print(sum_double(2, 2))
    print(sum_double(1, 4), "\n")

    print("Task 15: Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21. ")
    print(diff21(5))
    print(diff21(0))
    print(diff21(25), "\n")

    print("Task16: We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble. ")
    print(parrot_Trouble(True, 6))
    print(parrot_Trouble(True, 20))
    print(parrot_Trouble(False, 14))
    print(parrot_Trouble(True, 15))
    print(parrot_Trouble(False, 3), "\n")

    print("Task17: Given a string, return a new string where the first and last chars have been exchanged. ")
    print(str_Replace_Front_Back("code"))
    print(str_Replace_Front_Back("a"))
    print(str_Replace_Front_Back("ba"), "\n")

    print("Task18: Given a string, return a new string where 'not' has been added to the front. However, if the string already begins with 'not', return the string unchanged. ")
    print(not_String('candy'))
    print(not_String('x'))
    print(not_String('not bad'), "\n")

    print("Task19: Given a non-empty string and an int n, return a new string where the char at index n has been removed. ")
    print(missing_char('kitten', 1))
    print(missing_char('chocolate', 8))
    print(missing_char('Hi', 0), "\n")

    print("Task20: Given a string, if the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.")
    print(front3('ab'))
    print(front3('a'))
    print(front3(''))
    print(front3('Chocolate'), "\n")

    print("Task21: Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. ")
    print(string_match('abc', 'abc'))
    print(string_match('abc', 'axc'))
    print(string_match('xxcaazz', 'xxbaaz'), "\n")

    print("Task22: Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere. ")
    print(array123([1, 1, 2, 3, 1]))
    print(array123([1, 1, 2, 4, 1]))
    print(array123([1, 1, 2, 1, 2, 3]))
    print(array123([1, 2]), "\n")

    print("Task23: Given an array of ints, return True if one of the first 4 elements in the array is a 9. ")
    print(array_front9([1, 2, 9, 3, 4]))
    print(array_front9([1, 2, 3, 4, 9]))
    print(array_front9([1, 2, 3, 4, 5]))
    print(array_front9([2]))
    print(array_front9([]), "\n")

    print("Task24: Write a function that computers the area of a circle with radius r. Using MAP function. ")
    areas = []
    radii = [2, 5, 7.1, 0.3, 10]
    for r in radii:
        a = area(r)
        areas.append(a)
    print(areas, "\n")

    #   Alternative way using the MAP function
    # map takes 2 arguments, function, tuple/list
    map(area, radii)
    print(list(map(area, radii)))
    print(b, "\n")

    print("Task25: Write a function that converts the temperature from celsius to fahrenheit within a list. ")
    print(c_to_f1(temps), "\n")

    print("Task26: Find all data above the average. Use filter. ")
    print(filter_data(data), "\n")

    print("Task27: Remove missing data from list. ")
    print(rmv_msing_data(countries), "\n")

    print("Task28: Extract values from 2 lists at the same time using the ZIP function. ")
    print(loop_over_2_lists(x_list, y_list))

    print("Task29: Switch over the values of 2 variables. ")
    # x = -10
    # y = 15
    x, y = 10, -10
    print("Before: x = %d, y = %d" % (x, y))
    print(switch_variables(x, y), "\n")

    print("Task30: Try to get or find a value from dictionary. Use the GET function. ")
    print(find_value_in_dict(ages))
    print(find_value_in_dict(ages2), "\n")

    print("Task31: The correct way to open a file and print the output. Using the WITH function. ")
    # print(open_read_file('README.md'))
    print("\n")

    print("Task32: Build a function that converts the input to integer if possible. ")
    print(int_conv('full'))
    print(int_conv(4.5))


# dunder == double underscore
# allows you to check whether the file is being run as a script or not
# __main__ = script
# if __name__ = '__main__' is used to signal that this file is a script and you can run it
# if your file doesn't contain it then assume the file is used as a library or you should import it.
if __name__ == '__main__':
    main()
