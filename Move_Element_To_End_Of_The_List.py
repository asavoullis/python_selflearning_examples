""" From a list with numbers move the zero(s) to the end of the list """

def move_all_zeros_to_end_v1(lst):
    """ Moving all zero elements to the end v1 """

    for element in lst:
        if element == 0:
            lst.remove(0)
            lst.append(0)
    return lst


def move_all_zeros_to_end_v2(original_list):
    """ Moving all zero elements to the end v2 """

    # Create a new list without zeros
    new_list1 = [num for num in original_list if num != 0]
    # Count the number of zeros in the original list
    zeros_count = original_list.count(0)
    # Append the necessary number of zeros at the end of the new list  
    new_list1.extend([0] * zeros_count)
    return new_list1


def move_one_zero_to_end_v1(original_list):
    """ Moving just one zero to the end keep the rest at their place v1 """

    for element in original_list:
        if element == 0:
            original_list.remove(0)
            original_list.append(0)
            break
        # zeros_count = original_list.count(0)
        # if zeros_count >= 1:
    return original_list


def move_one_zero_to_end_v2(original_list):
    """ Moving just one zero to the end keep the rest at their place v2 """

    new_list = [num for num in original_list if num != 0]
    # If there's at least one zero, append a single zero to the end of the new list
    if 0 in original_list:
        new_list.append(0)
    return new_list

lst = [1, 2, 3, 4, 0, 5, 6, 0, 9, 10, 11, 8, 2, 3, 4]


print("\n","move all zeros v1: ", "\n", move_all_zeros_to_end_v1(lst.copy()))

print("\n","move all zeros v2: ", "\n", move_all_zeros_to_end_v2(lst.copy()))

print("\n","move one zeros to the end v1: ", "\n", move_one_zero_to_end_v1(lst.copy()))

print("\n","move one zeros to the end v2: ", "\n", move_one_zero_to_end_v2(lst.copy()))

# Original list remains unchanged
print("\n","Original List: ","\n", lst)
