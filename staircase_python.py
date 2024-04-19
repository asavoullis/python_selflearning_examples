def create_staircase1(nums):
    step = 1
    subsets = []
    while len(nums) != 0:
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False
      
    return subsets

# y = create_staircase1([1,2,3])
# x = create_staircase1([1,2,3,4,5,6,7])
# print(y)
# print(y)

def test_create_staircase1():
    assert create_staircase1([1,2,3,4,5,6,7]) == False
    assert create_staircase1([1,2,3,4,5,6]) == [[1], [2, 3], [4,5,6]]
    assert create_staircase1([1,2,3,4,5]) == False
    assert create_staircase1([1,2,3,4]) == False
    assert create_staircase1([1,2,3]) == [[1], [2, 3]]
    assert create_staircase1([1,2]) == False
    assert create_staircase1([1]) == [[1]]
    assert create_staircase1([]) == []

# Call the test function
test_create_staircase1()

# Print a success message
print("All tests passed successfully.")
