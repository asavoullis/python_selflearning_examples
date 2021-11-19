import first_module

#  We can also call the main method of the first_module directly!
first_module.main()

print("Second Module's Name: {}".format(__name__))


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
    print(6 in primes)
                                                        

if __name__ == '__main__':
    main()