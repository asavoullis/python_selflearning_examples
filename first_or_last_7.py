#given an array of ints within a list check if the first or the last element is a 7
#if its a 7 print True else False

list1 = [7,5,6,8,9,6,7,8]
list2 = [77,5,6,8,9,6,7,78]
list3 = [9,5,6,8,9,6,7,7]


def first_last_7(nums):
  if nums[0] == 7 or nums[-1] == 7:
    return True
  else:
    return False


print(first_last_7(list1))
print(first_last_7(list2))
print(first_last_7(list3))