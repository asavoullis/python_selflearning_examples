# Python practise examples and tasks 3

# used for task5
import sys

# used for task7
from collections import Counter

"""Task1: Iterate with enumerate instead of range + len. """
def iterate_with_enumerate():
    # iteration
    data = [1, 2, -4, -3, 2]
    # for i in range(len(data)):
    # if data[i] < 0:
    # data[i] = 0

    # the enumerate function returns both the element and its index as a tuple
    for idx, num in enumerate(data):
        if num < 0:
            data[idx] = 0
    print(data)
    return "\n"


"""Task2: Use list comprehension instead  of raw for loops. """
def list_comprehension():
    # lets create a list with all the squared numbers between 0-9
    # squares = []
    # for i in range(10):
    # squares.append(i*i)
    # square every element from 0 to 9
    squares = [i * i for i in range(10)]
    print(squares)
    return "\n"


"""Task3: Sort complex iterables with the sorted method. """
def sort_complex_iterables():
    # sort the list
    data = [3, 5, 1, 11, -2]
    sorted_data = sorted(data, reverse=True)
    print(sorted_data)

    # lets now say we have a complex iterable
    data2 = [{"name": "Max", "age": 6},
             {"name": "Lisa", "age": 20},
             {"name": "Ben", "age": 9}]
    sorted_data2 = sorted(data2, key=lambda x: x["age"])
    print(sorted_data2)
    return "\n"


"""Task4: Store unique values with sets. """
def store_unique_values_with_sets():
    # need to have only unique values in a list
    my_list = [1, 2, 3, 3, 4, 5, 6, 7, 7, 7, 7]

    # a set is an unordered collection data type that has no duplicate elements
    # so in this case it removes all the duplicate elements
    my_set = set(my_list)
    print(my_set)
    # you can create a set with curly bracers.
    # This allows python to make some optimizations and it also has some handy methods for
    # calculating the intersections and differences of sets.
    primes = {2, 3, 5, 7, 11, 13, 17, 19}
    print(primes)
    return "\n"


"""Task5: Save memory with generators. """
def save_memory_with_generators():
    # lets save memory when doing calculations with huge numbers
    # we might get in trouble with the memory using a list
    my_list = [i for i in range(10000)]
    print(sum(my_list))
    print(sys.getsizeof(my_list), "bytes")  # 87632 bytes
    # use generators instead that has the same syntax but uses parenthesis instead of square brackets
    my_gen = (i for i in range(10000))
    # a generator produces the elements one at a time and only when asked for it
    print(sum(my_gen))
    print(sys.getsizeof(my_gen), "bytes")  # 128 bytes
    return "\n"


"""Task6: Define default values in dictionaries with .get and .setdefault. """
def define_default_values_dicts():
    # lets use .get and .setdefault to define default values in dictionaries
    my_dict = {"item": "football", "price": 10.00}
    # lets get the count of the items and assume that the count key is also contained in the dictionary
    # count = my_dict["count"] #this will crash our code and raise a key error

    # this will also return the value for the key but it will not raise a key error
    # if the key is not available, it instead returns a default value in this case.
    # If you don't specify a default value it will return nan.
    count = my_dict.get("count", 0.0)
    print(count)
    print('count: ', my_dict.get('count'))
    # if you  want to ask our dictionary for the count and we also want to update the dictionary
    # and put in the count - if its not there - then we can use setdefault with the default value that we specify it.
    # The next time we check the key is now available in our dictionary.
    count = my_dict.setdefault("count", 0)
    print(count)
    print(my_dict)
    return "\n"


"""Task7: Count hashable objects with collections. Use of Counter function. """
def count_hashable_objects():
    # if you need to count the number of elements in your list there is a very handy tool in the collections module
    my_list = [10, 10, 10, 5, 5, 2, 8, 7, 6, 6, 6, 6, 6]
    counter = Counter(my_list)
    # this will return a dictionary with the elements as keys and their frequency
    # - sorted with the most common item in the front.
    print(counter)
    # to print how many times it has 10 , if none then returns 0
    print(counter[10])
    # find easy the most common items
    # we can also specify if we want the most or the one before by changing the number in the bracket
    most_common = counter.most_common(1)
    print(most_common)

    # this will return a list of tuples each tuple has the value as the first item and the count as the second item
    # so if you just want to have the value of the very most common item we first call the most common method
    # with argument one and then we access index 0 in our list and then again 0 to get the value
    print(most_common[0][0])
    return "\n"


"""Task8: Format strings with f-strings. """
def formating_strings():
    # lets format strings!
    name = "Alex"
    my_string = f"Hello {name}"
    print(my_string)
    i = 10
    print(f"{i} squared")
    return "\n"


"""Task9: Concatenate strings with .join. """
def formating_strings2():
    # combine all elements in that list separated by a space between each word
    list_of_strings = ["Hello", "my", "friend"]

    # bad way
    # as you know string is an immutable element so here we have to create new strings each time.
    # This code will be slow for large lists - avoid it - use join
    # my_string = ""
    # for i in list_of_strings:
    # my_string += i + ""

    # this combines all the elements into one string and uses the string in the begining as a separator
    # so here we use a string with only a space , we can also use commas "," between each word
    my_string = " ".join(list_of_strings)
    print(my_string)
    print("\n")


"""Task10: Merge dictionaries with a **. """
def merge_dictionaries_double_star():
    # merge 2 dictionaries
    d1 = {"name": "Alex", "age": 25}
    d2 = {"name": "Alex", "city": "New York"}
    # our combined dictionary has all the keys in it
    merged_dict = {**d1, **d2}
    print(merged_dict)
    print("\n")


"""Task11: Simplify if statements with if x in list. """
def simplify_if_statements_ifxin():
    # simplify if statements with if x in list instead of checking each item separately
    colors = ['red', 'green', 'blue']
    c = 'red'
    if c in colors:
        print(f'Yes {c} is in the {colors} list.')
    print("\n")


"""Task12: Please write a function that returns the length of the longest sequence of ascending digits found in a string. \
Non-digit characters should terminate a sequence of digits."""
# Examples:
#  1. Input string: “834562f”. The output integer should be 4 because the longest sequence is
#  “3456”.
#  2. Input string: “12g168rfa23”. The output integer should be 3 because the longest sequence is
#  “168”
string0 = "834562f"
string1 = "12g168rfa23"
def countLongestAscending(array):
    # counts longest ascending order numbers in a string
    maxCount = 0
    currentCount = 0
    previousItem = array[0]
    for item in array:
        if item.isnumeric() and previousItem.isnumeric():
            # print("current item is:", item)
            # print("previous item is:", previousItem)
            # cast previous item to int and compare it with the next item that is also casted into int
            if int(previousItem) < int(item):
                # if the next item is greater increase current count
                currentCount += 1
            else:
                # else set it back to 1
                currentCount = 1
        else:
            # if the current element is not numeric set currentCount to 1
            currentCount = 1
        previousItem = item
        # print("storing previousItem:", item)
        # print("currentCount:", currentCount)
        # print("maxCount", maxCount)

        # if the currentCount's value is greater than the maxCount's value then
        if currentCount > maxCount:
            # set the maxCount's value to the currentCount's value
            maxCount = currentCount
    return maxCount


"""Task13: Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!". """
def hello_name(name):
    return 'Hello ' + name + "!"


"""Task14: Given two strings, a and b, return the result of putting them together in the order abba, 
e.g. "Hi" and "Bye" returns "HiByeByeHi. """
def make_abba(a, b):
    return a+b+b+a


"""Task15: Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. 
The string length will be at least 2."""
def left2(str):
    return str[2:] + str[:2]


"""Task16: Given 2 strings return their concatenation, except omit the first char of each. 
The strings will be at least length 1."""
def non_start(a, b):
    return a[1:] + b[1:]


"""Task17: Given 2 strings, a and b, return a string of the form short+long+short, 
with the shorter string on the outside and the longer string on the inside."""
def combo_string(a, b):
    if len(a) >= len(b):
        return b + a + b
    else:
        return a + b + a


"""Task18: Given a string, return a version without the first and last char, so "Hello" yields "ell". """
def without_end(input_string):
    return input_string[1:-1]


"""Task19: Given a string of even length, return the first half. So the string "WooHoo" yields "Woo"."""
def first_half(str):
    # we need // rounds it down to the lowest integer 5//2 = 2  but 5/2 = 2.5
    return str[:(len(str)//2)]


"""Task20: Given an array of ints, return True if the array contains a 2 next to a 2 somewhere. """
def has22(nums):
    # using the zip function
    # the zip function returns tuples , in this case if array is [1, 2, 2] then it will return (1, 2) and (2, 2)
    return (2, 2) in zip(nums, nums[1:])

def has22v2(nums):
    for x in range(len(nums)-1):
        if (nums[x] == 2) and (nums[x+1] == 2):
            return True
    return False


"""Task21: Return the sum of the numbers in the array, except ignore sections of numbers 
starting with a 6 and extending to the next 7 
(every 6 will be followed by at least one 7). Return 0 for no numbers."""
def sum67(nums):
    flag = False
    sum1 = 0

    for num in nums:
        if num == 6:  # Turn the flag on if the number is 6
            flag = True
            continue
        if num == 7 and flag is True:  # Turn the flag Off when 7 is seen after 6
            flag = False
            continue
        if flag is False:  # Keep on adding the nums otherwise
            sum1 += num
    return sum1


def sum67v2(nums):
    state = 0
    s = 0
    for n in nums:
        if state == 0:
            if n == 6:
                state = 1
            else:
                s += n
        else:
            if n == 7:
                state = 0
    return s


"""Task22: Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, 
so it does not count and numbers that come immediately after a 13 also do not count."""
def sum13(nums):
    sum1 = 0
    state = 0
    for i in nums:
        if state == 0 and i != 13:
            sum1 = sum1 + i
        if i == 13:
            state = 1
        else:
            state = 0
    return sum1


"""Task23: Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, 
ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may 
assume that the array is length 3 or more. """
def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)


"""Task24: Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. """
def big_diff(nums):
    return max(nums) - min(nums)


"""Task25: Return the number of even ints in the given array. """
def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
        else:
            count = count
    return count


"""Task26: Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a\
fullstop. So "xxyz" counts but "x.xyz" does not. """
def xyz_there(strg):
    for i in range(0, len(strg) - 2):
        if strg[i-1] != "." and strg[i:i+3] == "xyz":
            return True
    return False


"""Task27: Given two strings, return True if either of the strings appears at the very end of the other string,
 ignoring upper/lower case. """
def end_other(a, b):
    a_len = len(a)
    b_len = len(b)
    a = a.lower()
    b = b.lower()
    if a[-b_len:] == b:
        return True
    if b[-a_len:] == a:
        return True
    return False


def end_otherv2(a, b):
    # using the function endswith
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)


"""Task28: Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count."""
def count_code(strg):
    count = 0
    for i in range(len(strg) - 3):
        if strg[i:i + 2] == "co" and strg[i + 3] == "e":
            count += 1
    return count


"""Task29: Return the number of times that the string "hi" appears anywhere in the given string."""
def count_hi(strg):
    count = 0
    for i in range(len(strg)-1):
        if strg[i:i+2] == "hi":
            count += 1
    return count


"""Task30: Given a string, return a string where for every char in the original, there are two chars. """
def double_char(strg):
    str_output = ""
    for i in strg:
        str_output = str_output + i*2
    return str_output


def double_charv2(strg):
    result = ""
    for i in range(len(strg)):
        result += strg[i] + strg[i]
    return result


"""Task31: Return True if the string "cat" and "dog" appear the same number of times in the given string. """
def cat_dog(strg):
    if strg.count('cat') == strg.count('dog'):
        return True
    else:
        return False


"""Task32: We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done. """
def make_chocolate(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - 5 * big
    else:
        remainder = goal % 5
    if remainder <= small:
        return remainder
    return -1


def main():
    print("Task1: Iterate with enumerate instead of range + len. ")
    print(iterate_with_enumerate())

    print("Task2: Use list comprehension instead  of raw for loops. ")
    print(list_comprehension())

    print("Task3: Sort complex iterables with the sorted method. ")
    print(sort_complex_iterables())

    print("Task4: Store unique values with sets. ")
    print(store_unique_values_with_sets())

    print("Task5: Save memory with generators. ")
    print(save_memory_with_generators())

    print("Task6: Define default values in dictionaries with .get and .setdefault. ")
    print(define_default_values_dicts())

    print("Task7: Count hashable objects with collections. Use of Counter function. ")
    print(count_hashable_objects())

    print("Task8: Format strings with f-strings. ")
    print(formating_strings())

    print("Task9: Concatenate strings with .join. ")
    print(formating_strings2())

    print("Task10: Merge dictionaries with a **. ")
    print(merge_dictionaries_double_star())

    print("Task11: Simplify if statements with if x in list. ")
    print(countLongestAscending(string0))
    print(countLongestAscending(string1), '\n')

    print("Task12: Function that returns the length of the longest sequence of ascending digits found in a string. \
Non-digit characters should terminate a sequence of digits.")
    arrayexample = "123fsg213"
    arrayexample2 = "fas12f1f45678"
    print(countLongestAscending(arrayexample))
    print(countLongestAscending(arrayexample2))
    print(countLongestAscending(string1))
    print(countLongestAscending(string0), '\n')

    print('Task13: Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!". ')
    print(hello_name("Bob"))
    print(hello_name("X"), '\n')

    print("Task14: Given two strings, a and b, return the result of putting them together in the order abba. ")
    print(make_abba('Hi', 'Bye'))
    print(make_abba('What', 'Up'), '\n')

    print('Task15: Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. ')
    print(left2('Hello'))
    print(left2('Chocolate'))
    print(left2('12345'), '\n')

    print('Task16: Given 2 strings, return their concatenation, except omit the first char of each. ')
    print(non_start('shotl', 'java'))
    print(non_start('mart', 'dart'))
    print(non_start('ab', 'xy'), '\n')

    print("Task17: Given 2 strings, a and b, return a string of the form short+long+short, \
with the shorter string on the outside and the longer string on the inside.")
    print(combo_string('Hello', 'hi'))
    print(combo_string('hi', 'Hello'), '\n')

    print('Task18: Given a string, return a version without the first and last char, so "Hello" yields "ell". ')
    print(without_end('java'))
    print(without_end('coding'), '\n')

    print('Task19: Given a string of even length, return the first half. So the string "WooHoo" yields "Woo". ')
    print(first_half('WooHoo'))
    print(first_half('HelloThere'), '\n')

    print("Task20: Given an array of ints, return True if the array contains a 2 next to a 2 somewhere. ")
    print(has22([2, 1, 2, 2]))
    print(has22v2([2, 1, 2, 2]))
    print(has22([2, 1, 2]))
    print(has22v2([2, 1, 2]), '\n')

    print("Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 \
    (every 6 will be followed by at least one 7). Return 0 for no numbers")
    print(sum67([1, 2, 2, 6, 99, 99, 7]))
    print(sum67v2([1, 2, 2, 6, 99, 99, 7]))
    print(sum67([1, 1, 6, 7, 2]))
    print(sum67v2([1, 1, 6, 7, 2]))
    print(sum67([1, 2, 2]))  # 5
    print(sum67v2([1, 2, 2]), '\n')

    print("Task22: Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, \
so it does not count and numbers that come immediately after a 13 also do not count.")
    print(sum13([1, 2, 2, 1]))   # 6
    print(sum13([1, 2, 2, 1, 13]))   # 6
    print(sum13([13, 1, 2, 13, 2, 1, 13]), '\n')  # 3

    print("Task23: Return the 'centered' average of an array of ints, which we'll say is the mean average of the values, \
except ignoring the largest and smallest values in the array.")
    print(centered_average([1, 2, 3, 4, 100]))  # 5
    print(centered_average([1, 1, 5, 5, 10, 8, 7]))  # 5
    print(centered_average([-10, -4, -2, -4, -2, 0]), '\n')  # -3

    print("Task24: Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array")
    print(big_diff([10, 3, 5, 6]))  # 7
    print(big_diff([7, 2, 10, 9]))  # 8
    print(big_diff([2, 10, 7, 2]))  # 8
    print(big_diff([2, 2]), '\n')  # 0

    print("Task25: Return the number of even ints in the given array. ")
    print(count_evens([2, 1, 2, 3, 4]))  # 3
    print(count_evens([2, 2, 0]))  # 3
    print(count_evens([1, 3, 5]), '\n')  # 0

    print('Task26: Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period. ')
    print(xyz_there('abc.xyz'))  # False
    print(xyz_there('xyz.abc'))  # True
    print(xyz_there('abcxyz'))  # True
    print(xyz_there('abc.xyzxyz'))  # False
    print(xyz_there('1.xyz.xyz2.xyz'), '\n')  # False

    print("Task27: Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences. ")
    print(end_other('ab', 'ab12'))  # False
    print(end_otherv2('ab', 'ab12'))
    print(end_other('AbC', 'HiaBc'))  # True
    print(end_otherv2('AbC', 'HiaBc'))
    print(end_other('abc', 'abXabc'))  # True
    print(end_otherv2('abc', 'abXabc'))
    print(end_other('yz', '12xz'))  # False
    print(end_otherv2('yz', '12xz'), '\n')

    print('Task28: Return the number of times that the string "code" appears anywhere in the given string, \
except we will accept any letter for the "d", so "cope" and "cooe" count.')
    print(count_code('ode'))  # 0
    print(count_code('cozexxcope'))  # 2
    print(count_code('cozfxxcope'))  # 1
    print(count_code('AAcodeBBcoleCCccoreDD'), '\n')  # 3

    print("Task29: Return the number of times that the string 'hi' appears anywhere in the given string. ")
    print(count_hi('abc hi ho'))  # 1
    print(count_hi('ABChi hi'))  # 2
    print(count_hi('hiho not HOHIhi'), '\n')  # 2

    print("Task30: Given a string, return a string where for every char in the original, there are two chars. ")
    print(double_char('Hi-There'))
    print(double_charv2('Hi-There'))
    print(double_char('Word!'))
    print(double_charv2('Word!'), '\n')

    print('Task31: Return True if the string "cat" and "dog" appear the same number of times in the given string. ')
    print(cat_dog('1cat1cadodog'))  # True
    print(cat_dog('catcat'))  # False
    print(cat_dog('c'))  # True
    print(cat_dog('catxdogxdogxca'), '\n')  # False

    print("Task32: We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). \
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.")
    print(make_chocolate(4, 1, 10))  # -1
    print(make_chocolate(4, 1, 7))  # 2
    print(make_chocolate(4, 1, 9))  # 4
    print(make_chocolate(1, 2, 5), '\n')  # 0


if __name__ == '__main__':
    main()
