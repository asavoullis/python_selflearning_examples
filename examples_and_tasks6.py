# Python practise examples and tasks 6

"""1 Zip function """
names = ['James','Izzy','Maham','Yash']
cookies = ['chocolate chip','oatmeal','triple chocolate','brown sugar','M&M']
# zip combines the elements of the 2 lists into a tuple but we also have the code inside [] so it is a list
# we slice the list from the last element to the end of the list
print("\n",*[*zip(names,cookies)][-1:])
# ('Yash', 'brown sugar') # we have 5 elements in the 2nd array and 4 in the first array


"""2 prints all possible pairs (from the elements in the list)"""
from itertools import combinations
languages = ['Python','R','SQL','Julia']
programers = [*combinations(languages,3)]
print("\n",programers)


"""3
What is the difference between %timeit and %%timeit ?
%timeit is used for single lines, %%timeit is used with multiple lines of code. 
"""


"""4
How do you save the outcome of %timeit command into a variable?
We are interested in timing the  numpy.random.rand() function.

time = %timeit -o numpy.random.rand() PRES S 2
"""


"""5 What is the most efficient way to obtain unique elements from a list? """
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, "a", "a"]
set1= set(list1)
print("\n",set1)


"""6 line_profiler 
%timeit and %lprun are both magic commands in IPython, a powerful interactive shell for Python. 
These commands are not standard Python but are specific to IPython.
%timeit uses multiple runs and loops to calculate an average. This is particularly useful for quick benchmarks and performance testing.
%lprun runs the code only once. used for profiling line by line. It provides a line-by-line analysis of the execution time of a Python function.

# loads the line profiler extension
%load_ext line_profiler 

def my_function():
    # some code to profile
    pass

# profiles the my_function line by line.
%lprun -f my_function my_function()
"""


"""7 * operator """
"""
In Python, the * operator is often referred to as the "unpacking" operator. 
It is used to unpack the elements of an iterable (like a list or tuple) or the values of a dictionary 
into individual elements.
"""
print("\n",*enumerate(['a','b','c']))
# (0, 'a') (1, 'b') (2, 'c')


"""8
%lprun -f my_function -o output.txt -s my_function(data)

-o output.txt specifies the name of the file where the profiling results will be saved.
-s my_function(data) specifies the statement to be profiled. It's essentially the function call you want to analyze.
-f my_function specifies the name of the function to be profiled.
"""


"""9 What is the most efficient code for creating a list of even numbers between 1 and 15? """
print("\n",list(range(2,15,2)))


"""10 select only 1 column and apply string formatting """
import pandas as pd
data = {'Color': ['Red', 'ReD', 'red']}
df = pd.DataFrame(data)
print("\n",df['Color'].apply(str.upper))

"""11 Advantages of using numpy arrays over lists
It is easy to slice multidimensional arrays. 
We can easily apply operations on all elements of an array through broadcasting.
They are memory efficient as they can contain only one data type.
"""


"""12 Making a new column 2 """
df['temp'] = [25, 30, 22]
# Adding a new column 'temp_f' using the apply function
df['temp_f'] = df.apply(
    lambda row: row['temp'] * 1.8 + 32,axis=1)
print("\n",df.head())


"""13 MAP Unpack in upper case """
names_upper = map( str.upper , ["Dr. Jekyll","&","Mr. Hyde" ] )
print("\n", [*names_upper] )


"""13 Classes Properties
Encapsulation:
Bundling of data and methods that operate on that data into a single unit known as a class
Group related variables and functions together 
Reduce complexity + increaase reusuability

Abstraction: 
Involves hides/simplifying complex systems by modeling classes based on the essential properties and 
behaviors they share. 
Reduces Complexity + Isolate Impact of changes

Inheritance:
allows a new class (subclass or derived class) to inherit attributes and behaviors from an 
existing class (superclass or base class). 
The subclass can extend or override the functionality of the superclass.

Polymorphism (overriding): 
Allows objects of different types to be treated as objects of a common type. 
There are two main types of polymorphism: compile-time (or static) polymorphism and runtime (or dynamic) polymorphism.
A subclass provides a specific implementation of a method that is already defined in its superclass
"""

# Polymorphism
class Calculator:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

# Example
calc = Calculator()
result1 = calc.add(1, 2)      # Invokes the first add method
result2 = calc.add(1, 2, 3)   # Invokes the second add method


# Overriding polymorphism
class Animal1:
    def speak(self):
        pass

class Dog1(Animal1):
    def speak(self):
        return "Woof!"

class Cat1(Animal1):
    def speak(self):
        return "Meow!"

# Example
dog = Dog1()
cat = Cat1()
print(dog.speak())  # Outputs: Woof!
print(cat.speak())  # Outputs: Meow!


# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

# Example
animal = Animal("Generic Animal")
print(animal.speak())  # Outputs: Some generic sound


class Dog(Animal):
    def speak(self):
        return "Woof!"

# Example
dog = Dog("Buddy")
print(dog.speak())  # Outputs: Woof!
print(dog.name)     # Accesses the 'name' attribute from the base class

# Polymorphism
class ShapeCalculator:
    def area(self, length, width=None):
        if width is not None:
            return length * width  # Rectangle area
        else:
            return 3.14 * (length ** 2)  # Circle area with a default width

# Example
calculator = ShapeCalculator()

# Rectangle
rectangle_area = calculator.area(5, 8)
print(f"Area of the rectangle: {rectangle_area}")

# Circle
circle_area = calculator.area(4)
print( f"Area of the circle: {circle_area}")
print("")


"""14  If key in dictionary print value"""
d = {'a':0, 'b':1, 'c':2, 'd':3}
if 'c' in d:
    print(d['c'])
else:
    print('c')


"""15  Print all element in the list """
for name in names:
    print(name)
print("")


"""16 Make a list with tuples inside that have each element of numbers and their squared values"""
numbers = [8, 0, 4, 7]
numbers_squared = [n ** 2 for n in numbers]
print(list(zip(numbers, numbers_squared)))
print("")


"""17 Adding key-value pair in a dictionary"""
d = {'a':0, 'b':1, 'c':2, 'd':3}
d['d'] = 9
print(d)
print("")

"""18 Get the value of a key if inside the dictionary else return string"""
d = {'a':0, 'b':1, 'c':2, 'd':3}
v = d.get('b', 'Key is not in dictionary!')
print(v)
print("")

"""19 Combine the lists, make them into 1, extend the first one"""
l = [5, 2, 4, 0]
e = [8, 6, 1, 8]
l.extend(e)
print(l)
print("")

"""20 Add element to a list"""
l.append(1)
print(l)
print("")


"""21 Print all key-value pairs from dictionary"""
d = {'aa':30, 'bb':31, 'cc':32, 'dd':33}
for k, v in d.items():
    print(k, v)
print("")


"""22 Convert to set and add element 5"""
s = ([8, 8, 2, 8])
s.append(5)
print(s)
print("")


"""23 Sort the list"""
l = [8, 9, 2, 4, 6, 7]
print(sorted(l))
print("")


"""24 creates a dlist"""
from collections import defaultdict

# This line creates a defaultdict with default values of type int. 
# A defaultdict is a dictionary subclass in Python that returns a default value for a nonexistent key rather 
# than raising a KeyError. In this case, the default value is set to 0.
d = defaultdict(list)
print(d)
for x in range(4):
    d[x].append(x * 2)
print(list(d.items()))
print("")


"""25 Initialize a new dictionary and add a key-value pair to the dictionary"""
d = dict()
d[8] = 1
print(d)
print("")


"""26 Print in a list the keys of the dictionary"""
d = {'aa':10, 'bb':11, 'cc':12, 'dd':13}
print(list(d.keys()))
print("")


"""27 Print difference that set s1 has from s2 """
# there is also .union .intersection 
s1 = set([45, 83, 69, 84])
s2 = set([31, 39, 22, 37])
res = s1.difference(s2)
print(res)
print("")


"""28 enumerate and exponentials"""
n1 = [5, 4, 9, 3]
n2 = [n ** 3 for n in n1]
pairs = zip(n1, n2)

# Iterate over each pair and their index using 'enumerate'.
for idx, pair in enumerate(pairs):
    # Unpack the pair into variables 'n' and 'm'.
    n, m = pair
    
    # Print a formatted string indicating the result of raising 'n' to the power of 3 and displaying 'm'.
    print('{} ^ {} = {}'.format(n, 3, m))
print("")


"""29"""
from collections import Counter
chars = [0, 3, 1, 2, 3, 2, 3, 1, 2, 3]
# Use Counter to count the occurrences of each element in the list
char_count = Counter(chars)

# Print the three most common elements and their counts
print(char_count.most_common(3))
print("")


"""30 Print the poped element"""
l1 = [3, 0, 8, 5, 9, 4]
p = l1.pop()
print(p)
print("")