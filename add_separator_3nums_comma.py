


def add_separator(list):
    ''' Add comma separator to format numbers '''

    # In Python, to format a number with commas we will use “{:,}” along with the .format() function and it will add a
    # comma to every thousand places starting from left. 
    new_list = []
    for num in list:
        print(num)
        new_list.append('{:,}'.format(num))

    return(new_list)

def main():
    a = [10989767, 9876780, 9908763]
    print(add_separator(a))

if __name__ == '__main__':
    main()
