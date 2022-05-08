# Python practise examples and tasks 4

import datetime

# in Python an assignment (d = 8) is not an expression, its a statement
# in other languages assignments are also expressions and return d back to you.
# python expressions were added in 3.8


"""Task 1: assign multiple expressions together from right to left"""
def multiple_assignment_expression():
    # parenthesis are there because they have to be, you are not allowed to assign multiple expressions together unless you put them in parenthesis
    (a := (b := (c := (d := 0))))
    # d:= 0 is going to return 0
    # := goes from right to left
    # normal = goes from left to right
    # we assign a, b, c, d to be 0
    return (a, b, c, d)


"""Task2: Explore string formatting """
def equals_debugging():
    str_value = "other 😊"
    num_value = 1234
    print(f'the value is {str_value}')
    print(f'{str_value = }')  # for debugging
    print(f'{num_value % 2 = }')
    print("\n")


"""Task3: Explore string formatting 2"""
def conversions():
    str_value = "other 😊"
    print(f'{str_value!a}')  # converts non ascii characters to an ascii version
    print(f'{str_value!s}')  # string conversion used for formatting
    print(f'{str_value!r}')  # repr
    print("\n")


"""Task4: Explore string formatting using a class """
# empty class
class MyClass:
    # all it does is define a format method which takes a format_spec and returns a string
    def __format__(self, format_spec) -> str:
        print(f'Myclass __format__ called with {format_spec=!r}')
        return "Myclass()"


"""Task5: Explore string formatting 3"""
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


"""Task6: Explore  chained assignments - multiple equal signs"""
def multiple_assignment():
    c = d = e = f = []
    print(c, d, e, f)
    print("\n")


"""Task7: Tuple unpacking"""
def tuple_assignment():
    a, b = 1, 2
    print(a, b)
    print("\n")


# advanced unpacking
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
# pass in the object that we want to set an attirubute on
setattr(person, first_key, first_val)

# we want to get the first attirubute here
first = getattr(person, first_key)


# v2
class Person2():
    pass


person2 = Person()

person_info = {'first': 'Corey', 'last': 'Schafer'}

# the keys will be equal to the keys and the values to the values eg corey for value
for key, value in person_info.items():
    setattr(person2, key, value)


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


# dunder == double underscore
# allows you to check whether the file is being run as a script or not
# __main__ = script
# if __name__ = '__main__' is used to signal that this file is a script and you can run it
# if your file doesn't contain it then assume the file is used as a library or you should import it.
if __name__ == '__main__':
    main()
