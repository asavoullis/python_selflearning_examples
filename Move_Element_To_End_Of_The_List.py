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




# Exercise:
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# OR move all non-zero elements to the start of the array
# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead. 
        """

        # Initialize two pointers, L and R, pointing to the start and end of the list respectively
        L, R = 0, len(nums)-1

        # Iterate until the left pointer crosses the right pointer
        while L <= R:
            # print("L:", L)
            # print("R:", R)
            # print("nums[R]", nums[R])
            # print("nums[L]", nums[L])

            # Move the right pointer towards the left until a non-zero element is found
            while nums[R] == 0 and L<=R:
                R-=1
            
            # Move the left pointer towards the right until a non-zero element is found
            while nums[L] == 0 and L <= R:
                # When a non-zero element is found at L, remove it and insert it at R,
                # effectively moving the zero at R to L's position
                temp = nums.pop(L)
                nums.insert(R, temp)
                # Decrement R to maintain its position at the end of the list
                R-=1
            else:
                # If nums[L] is not zero, increment L to continue searching for zeros
                L+=1



"""
Approach:
Two-Pointer Method: 
Utilize two pointers, L (Left) and R (Right), to scan through the array. 
L is used to find zeroes that need to be moved, and R acts as a boundary of the non-zero elements, decreasing when a zero is identified at the end.

In-Place Swap: 
When a zero is found by L, it's removed and inserted before R, effectively pushing it towards the end within the boundary. 
This ensures that the insertion of zeros does not disrupt the relative order of the non-zero elements.

Boundary Adjustment: 
The R pointer is adjusted (decremented) each time a zero is moved to ensure the zeros accumulate at the end of the array, and the non-zero elements stay within the new boundary defined by R.

Complexity:
Time complexity: The algorithm's time complexity is a bit complex due to the removal and insertion operations within the loop. 
Each pop and insert operation is O(n), making it less efficient, especially for large arrays, as these operations are executed within a while loop.
Space complexity: O(1) - The solution modifies the array in place without using any additional space proportional to the input array size, fulfilling the in-place requirement.


The algorithm uses two pointers, L and R, initialized to the start and end of the list respectively.
It iterates through the list until L crosses R.
It moves R towards the left until it finds a non-zero element.
It moves L towards the right until it finds a non-zero element. When it finds a non-zero element at L, it removes it and inserts it at R, effectively moving the zero at R to L's position.
After moving a zero from position R to L, it decrements R to maintain its position at the end of the list.
If the element at L is not zero, it increments L to continue searching for zeros.
This process repeats until all zeros are moved to the end of the list while maintaining the relative order of non-zero elements.
"""

# Initialize an instance of the Solution class
solution_instance = Solution()

# Example input list
nums = [0, 1, 0, 3, 12]

# Call the moveZeroes method to modify the list in-place
solution_instance.moveZeroes(nums)

# Output the modified list
print(nums)  # This will print: [1, 3, 12, 0, 0]


# https://youtu.be/aayNRwUN3Do?si=CWag_eDIbXGi29KW
def moveZeroes2(nums: list[int]) -> None:
    # Initialize left pointer to track the position to swap non-zero elements
    l = 0
    
    # Iterate through the list using a right pointer 'r'
    for r in range(len(nums)):
        # If the current element at 'r' is non-zero,
        if nums[r]:
            # Swap the non-zero element with the element at 'l'
            nums[l], nums[r] = nums[r], nums[l]
            # Move the left pointer 'l' one step forward
            l += 1

        


# ================================================================
# Testing with large lists
from random import randint
from time import time 

n = 100000
arr = [randint(0,9) for _ in range(n)]
arr2 = [randint(0,9) for i in range(n)]

start = time()

solution_instance = Solution()
solution_instance.moveZeroes(arr)

stop = time()
print("time took:", stop - start)
# print(arr)  



# testing 2nd funciton:

start = time()

moveZeroes2(arr2)

stop = time()
print("time took:", stop - start)
# print(arr2)  

# ================================================================

# now using extra memory:
def moveZeroes_with_memory(array):
    # Initialize an empty list 't' to store non-zero elements
    t = []
    # Initialize a counter 'z' to count the number of zeros encountered
    z = 0
    # Iterate through each element 'num' in the input array
    for num in array:
        # If the current element 'num' is not zero,
        if num != 0:
            # Append the non-zero element to the list 't'
            t.append(num)
        else:
            # If the current element is zero, increment the zero counter 'z'
            z += 1
    
    # Extend the list 't' by adding 'z' number of zeros at the end
    t.extend(z * [0])
    # Return the modified list 't' with zeros moved to the end
    return t


"""
The algorithm uses an additional list t to store non-zero elements.
It iterates through each element in the input array.
If the current element is non-zero, it appends it to the list t.
If the current element is zero, it increments the zero counter z.
After processing all elements, it extends the list t by adding z number of zeros at the end. This effectively moves all zeros encountered during the iteration to the end of the list.
Finally, it returns the modified list t with zeros moved to the end while maintaining the order of non-zero elements.
"""