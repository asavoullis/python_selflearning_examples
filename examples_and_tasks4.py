# Python practise examples and tasks 4

import datetime

# in Python an assignment (d = 8) is not an expression, it's a statement
# in other languages assignments are also expressions and return d back to you.
# python expressions were added in 3.8


"""Task 1: Assign multiple expressions together from right to left. """
def multiple_assignment_expression():
    # parenthesis are there because they have to be, you are not allowed to assign multiple expressions together unless you put them in parenthesis
    (a := (b := (c := (d := 0))))
    # d:= 0 is going to return 0
    # := goes from right to left
    # normal = goes from left to right
    # we assign a, b, c, d to be 0
    return (a, b, c, d)


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
class Person():
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
class Person2():
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
        if pause == False and num != 13:
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
    sum = 0
    for element in nums:
        sum += element
    return (sum - min(nums) - max(nums)) / (len(nums)-2)


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
def xyz_there(str):
    for i in range(len(str)):
        if str[i] != '.' and str[i+1:i+4] == 'xyz':
            return True
        if str[0:3] == 'xyz':
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
    print(has22([2, 1, 2])) #False
    print(has22([1, 2, 1, 2])) #False
    print(has22([])) #False
    print(has22_v2([4, 2, 4, 2, 2, 5]), '\n') #True

    print('Task11: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and '
          'extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.')
    print(sum67([1, 2, 2])) #5
    print(sum67([1, 2, 2, 6, 99, 99, 7])) #5
    print(sum67([1, 6, 7, 7])) #1+7=8
    print(sum67([6, 7, 1, 6, 7, 7])) #1+7=8
    print(sum67([6, 8, 1, 6, 7])) #0
    print(sum67([]), '\n')

    print('Task12: Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is '
          'very unlucky, so it does not count and numbers that come immediately after a 13 also do not count. ')
    print(sum13([13, 1, 2, 13, 2, 1, 13])) #2+1=3
    print(sum13([1, 2, 13, 2, 1, 13])) #1+2+1=4
    print(sum13([5, 13, 2]), '\n') #5

    print('Task13: List-2 > centered_average. ')
    print(centered_average([-10, -4, -2, -4, -2, 0])) #3
    print(centered_average([0, 2, 3, 4, 100])) #3
    print(centered_average([-10, -4, -2, -4, -2, 0]), '\n') #-3

    print("Task14: List-2 > big_diff. ")
    print(big_diff([5, 1, 6, 1, 9, 9])) #8
    print(big_diff([7, 7, 6, 8, 5, 5, 6])) #3
    print(big_diff([10, 0])) #10
    print(big_diff([2, 2]), '\n') #0

    print("Task15: List-2 > count_evens. ")
    print(count_evens([2, 11, 9, 0])) #2
    print(count_evens([1, 3, 5])) #0
    print(count_evens([2, 5, 12]), '\n') #2

    print('Task16: String-2 > xyz_there. ')
    print(xyz_there('abc.xxyz')) #True
    print(xyz_there('1.xyz.xyz2.xyz')) #False
    print(xyz_there('abc.xyzxyz')) #True
    print(xyz_there('abc.xyz'), '\n') #False

    print('Task17: String-2 > end_other. ')
    print(end_other('abcXYZ', 'abcDEF')) #False
    print(end_other('Z', '12xz')) #True
    print(end_other_v2('Hiabcx', 'bc')) #False
    print(end_other_v2('Hiabc', 'bc')) #True
    print(end_other_v2('abc', 'abXabc'), '\n') #True




# dunder == double underscore
# allows you to check whether the file is being run as a script or not
# __main__ = script
# if __name__ = '__main__' is used to signal that this file is a script and you can run it
# if your file doesn't contain it then assume the file is used as a library or you should import it.
if __name__ == '__main__':
    main()
