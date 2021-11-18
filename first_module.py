# This is always run - when executed or when imported
print("hello there!")
# print("First Module's Name: {}".format(__name__))


# This is run when this file is directly executed
def main():
    print("First Module's Main Method")

# This is run when this file is directly executed
if __name__ == '__main__':
    main()
    print("first_module is run directly")

# This is run when this file is imported from another file
else:
    print("first_module is imported")