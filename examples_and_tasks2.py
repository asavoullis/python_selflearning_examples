# Python practise examples and tasks
# more advanced than examples_and_tasks

import timeit
import numpy as np
import pandas as pd

"""
Task1: Sum the numbers from 0 to n-1 in different ways
"""


# although the for and the while loop are essentially doing the same, the while loop takes longer than the for loop to run
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


# much faster because entire operation is written in c, this whole function is 1 c call, both the iteration and the adding itself is done in c.
# the downside is that arange creates a whole array in memory

# fastest way to calulate it is to use math knowledge - we are adding the first n-1 integers therefore: we can use this formula
def sum_math(n=50_000_000):
    return (n * (n - 1)) // 2


##  conclusion:
# the fastest way to loop in python is to:
# not to loop in python
# try to compute the answer mathamtically ahead of time definately do that
# loop in a c built in function such as numpy library
# call a c function that can do the looping
# use python builtin functions like sum or map
# use for loop
# use while loop


"""
Task2: Multiple input arguments and parameters in funcs
"""


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


# multiple variable input - we can pass multiple key value pairs or multiple keyword arguments to a function and python will automatically package them into a dictionary
def save_user(**user):
    # makes it a dictionary
    print(user)
    # you can also specify which key you want
    print(user["id"])
    return (user)


"""
Task3: Scope - Global vs Local Variables
"""
message = 'b'


# Scope - the region of the code where a variable is defined
def greet(name):
    # global message
    # avoid using the global inside the variable - easy to make mistakes and cause bugs

    # the scope of the variable message and name is the greet function, they are local variables inside the greet function - they don't exist anywhere else
    message = "a"


"""
Task4: create a function which takes a single integer
"""


# Create a function that when passed an integer, will return Fizz if the int is divisible by 3, Buzz if the int is divisible by 5, FizzBuzz if divisible by both 3 and 5 else the number
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


"""
Task5: Concatinate 2 tuples
"""
# create a function that concatinates 2 tuples
tup1 = (1, "a", True)
tup2 = (4, 5, 6, False)


def tupleconcat(tupl1, tupl2):
    # adds them in order first tup1 and then tup2 at its end
    return (tupl1 + tupl2)


"""
Task 6: Initialize a 5 by 5 numpy array with only zeros.
"""


def array5by5zeros():
    n1 = np.zeros((5, 5))
    return n1


"""
Task 7: Read a .csv file using Pandas.
"""


# def read_csv_file_pandas(file):
#     df = pd.read_csv(file)
#     return df


"""
Task 8: Create a Pandas Series from data.
"""
data = ["1", 2, "three", 4.0]


def createa_Pandas_Series(inputdata):
    series = pd.Series(inputdata)
    return (series)
    return (type(series))


"""
Task 9: Reverse a string.
"""
strng1 = "Hello"
strng2 = "My name is Johnas123"
def reverse_String(inputstrg):
    str_reverse = inputstrg[::-1]
    return (str_reverse)


"""
Task 10: Create a new column in pandas by using values from other column.
"""
a = [1, 2, 3]
b = [2, 3, 5]
d = {"col1": a, "col2": b}
def new_Column_Using_Values_ofOther_Columns(dict):
    df = pd.DataFrame(d)
    df["Sum"] = df["col1"] + df["col2"]
    df["Difference"] = df["col1"] - df["col2"]
    return (df)



"""
Task 11: Select columns in pandas and add them to a new dataframe.
"""
def add_Column_toNew_Dataframe(dataframe):
# If there are two columns with the same name then both columns get copied to the new dataframe.
    print(dataframe.columns)
    newdataframe = dataframe[["col1"]]
    return (newdataframe)



"""
Task 12: Select columns in pandas and add them to a new dataframe.
"""
d2={"col1":[1,2,3],"col2":["A","B","C"]}
def delete_Column_from_dataframe(inputdataframe):
    dataframe2 = pd.DataFrame(inputdataframe)
    dataframe2 = dataframe2.drop(["col1"], axis=1)
    return (dataframe2)



def main():
    print("Task 1: Find the fastest way to compute the sum of the first 50 000 000 integers. ")
    # print('for pure loop\t\t', timeit.timeit(for_loop, number =1))
    # print('built in sum func\t\t', timeit.timeit(sum_range, number =1))
    # print('built in sum func\t\t', timeit.timeit(numpy_sum, number =1))
    # print('built in sum func\t\t', timeit.timeit(sum_math, number =1))
    # , formats the output number to have , and separate every 3 numbers
    print(f'{numpy_sum():,}')
    # print(sum_math())
    print("\n")

    print("Task 2: Functions with many or a variable amount of input parameters *args and **args. ")
    print(multiply(2, 3, 4, 5))
    # function with 2 input parameters, the second if not provided will be by default 1
    print(incriment(2, 5))
    print(incriment(2))
    save_user(id=1, name="John", age=22)
    print("\n")

    print("Task 3: Scope of variables. ")
    # for example we have a global variable
    greet("John")
    print(message)
    print("\n")

    print("Task 4: The fizz_buzz function. ")
    print(fizz_buzz(15), fizz_buzz(3), fizz_buzz(5), fizz_buzz(4))
    print("\n")

    print("Task 5: Concatinate 2 tuples together. ")
    print(tupleconcat(tup1, tup2))
    print("\n")

    print("Task 6: Initialize a 5 by 5 numpy array with only zeros. ")
    print(array5by5zeros())
    print("\n")

    print("Task 7: Read a .csv file using pandas. ")
    #print(read_csv_file_pandas(file.csv))
    print("\n")

    print("Task 8: Creat a Pandas Series from data. ")
    print(createa_Pandas_Series(data))
    print("\n")

    print("Task 9: Reverse the string. ")
    print(reverse_String(strng1))
    print(reverse_String(strng2))
    print("\n")

    print("Task 10: Create a new column in pandas by using values from other column. ")
    print(new_Column_Using_Values_ofOther_Columns(d))
    print("\n")

    print("Task 11: Select columns in pandas and add them to a new dataframe. ")
    dfnew = (new_Column_Using_Values_ofOther_Columns(d))
    print(add_Column_toNew_Dataframe(dfnew))
    print("\n")

    print("Task 12: Select columns in pandas and add them to a new dataframe. ")
    print(delete_Column_from_dataframe(d2))
    print("\n")







# dunder == double underscore
# allows you to check whether the file is being run as a script or not
# __main__ = scritp
# if __name__ = '__main__' is used to signal that this file is a script and you can run it
# if your file doesn't contain it then assume the file is used as a library or you should import it.
if __name__ == '__main__':
    main()


