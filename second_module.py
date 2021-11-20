# we are importing the file we created
import first_module

import datetime

import time
import math


#  We can also call the main method of the first_module directly!
first_module.main()

print("Second Module's Name: {}".format(__name__))


def is_prime_v1(n):
    """ Return 'True' if 'n' is a prime number. False otherwise """
    # 1 is not prime
    if n == 1:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

# let's now reduce the amount of calculations we do as after dividing by the square root of n the divisions are the same
def is_prime_v2(n):
    """ Return 'True' if 'n' is a prime number. False otherwise """
    if n == 1:
        return False

    # floor rounds it down
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

# lets now remove the testing for even numbers
def is_prime_v3(n):
    """ Return 'True' if 'n' is a prime number. False otherwise """
    if n == 1:
        return False

    # if it's even and not 2, then it's not prime
    if n == 2:
        return True

    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    # adding a step value
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True




def main():

    """ Exploring Sets """
    # sets are built-in data types
    # sets only have unique elements
    example = set()
    # to see
    # print(dir(example))
    example.add(42)
    example.add(False)
    example.add(3.14159)
    example.add("Thorium")
    print(example)
    example.remove(42)
    print(len(example))

    # print(help(example.discard))
    print("\n")

    odds = set([1, 3, 5, 7, 9])
    evens = set([2, 4, 6, 8, 10])
    primes = set([2, 3, 5, 7])
    composites = set[4, 6, 8, 9, 10]

    print(odds.union(evens))
    print(odds.intersection(primes))
    print("\n")

    print(2 in primes)
    print(6 in primes, "\n")


    """ Datetime Module """
    # yyyy-mm-dd

    # print(dir(datetime), "\n")
    # print(help(datetime), "\n")
    gvr = datetime.date(1956, 1, 31)
    print(gvr, "\n")

    mill = datetime.date(2000, 1, 1)
    dt = datetime.timedelta(100)
    print(mill + dt, "\n")

    # Lets create our own time format
    # Day-name, Month-name -Day-#, Year
    print(gvr.strftime("%A, %B %d, %Y"), "\n")

    # alternative - more modern way
    message = "GRV was born on {:%A, %B %d, %Y}"
    print(message.format(gvr), "\n")

    #   Let's create a launch date object
    # datetime.date (yyyy-mm-dd)
    launch_date = datetime.date(2017, 3, 30)
    #   Let's create a launch time object
    # datetime.time (hh-mm-ss)
    launch_time = datetime.time(22, 27, 0)
    #   Let's create an object with both the date and the time
    launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
    print("launch date:", launch_date)
    print("launch time:", launch_time)
    print("launch datetime:", launch_datetime, "\n")

    # access the individual components
    print(launch_time.hour)
    print(launch_date.month)
    print(launch_datetime.minute, "\n")

    # Access current datetime:
    now = datetime.datetime.today()
    print(now)
    print("Microseconds:", now.microsecond, "\n")

    moon_landing = "7/20/1969"
    moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
    print(moon_landing_datetime)
    # this is an instance of the datetime class in the datetime module
    print(type(moon_landing_datetime))


    """ Prime and Composite Numbers """
    # 1 is a unit number
    # Prime number is a positive integer number that can be divided only by itself and 1
    # Composite numbers can be factored into smaller integers

    for n in range(1, 10):
        print(n, is_prime_v1(n))
    print("\n")


    t0 = time.time()
    for n in range(1, 10):
        print(n, is_prime_v2(n))
    t1 = time.time()
    print("Time required: ", t1 - t0)
    print("\n")

    t0 = time.time()
    for n in range(1, 21):
        print(n, is_prime_v3(n))
    t1 = time.time()
    print("Time required: ", t1 - t0)
    print("\n")




                                                        

if __name__ == '__main__':
    main()