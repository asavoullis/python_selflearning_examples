# Python practise examples and tasks 8

"""1 break """
for i in range(1, 6): 
  if i % 2 == 0: 
    break 
  print(i) # 1 then it breaks
print("") 


"""2 even """
for i in range(1, 6): 
  if i % 2 == 0: 
    print(i) # 2 4
print("")


"""3 continue """
for i in range(1, 6): 
  if i == 3 or i == 4: 
    continue 
  print(i)
print("")


"""4  while if continue """
x = 0 
while x < 10: 
  x += 2 
  if x % 3 == 0: 
    continue 
  print(x)
print("")


"""5  """
for i in range(5): 
  if i == 2: 
    break 
  print(i)
print("")


"""6 for else break """
# the else block is executed if the loop naturally finishes its iteration without being prematurely exited by a break.
for i in range(1, 6): 
  if i == 3 or i == 4: 
    break 
  print(i) 
else: 
    print("Loop completed") 
print("Done")
print("") 


"""7 for else """
# start end  step
for i in range(1, 4, 2): 
  print(i)
# after the for loop is completed successfully the else loop is executed
else: 
    print("Loop completed") 
print("")


"""8  """
for i in range(3):
# range(0) is nothing so its not executed
  for j in range(i):
    print(i, j)
print("")


"""9  """
def calculate_average(numbers): 
  total = sum(numbers) 
  average = total / len(numbers) 
  return average 
my_numbers = [1, 2, 3, 4, 5] 
result = calculate_average(my_numbers)
print(result) #3.0
print("")


"""10  """
def multiply_list(lst): 
  for i in range(len(lst)): 
    lst[i] *= 2 
my_list = [1, 2, 3, 4] 
multiply_list(my_list) 
print(my_list)
print("")


"""11  """
def square_root(n): 
  guess = n / 2 
  # Using the Newton-Raphson method for approximating square roots
  while abs(guess * guess - n) > 0.0001: 
    guess = (guess + n / guess) / 2 
  return guess 
result = square_root(16) 
print(result)
print("")


"""12  """
def bubble_sort(lst): 
  n = len(lst) 
  for i in range(n): 
    for j in range(0, n - i - 1): 
      if lst[j] > lst[j + 1]: 
        lst[j], lst[j + 1] = lst[j + 1], lst[j] 
my_list = [5, 2, 8, 1, 9] 
bubble_sort(my_list) 
print(my_list)
print("")


"""13  """
def factorial(n): 
  if n == 0: 
    return 1 
  else: 
    return n * factorial(n - 1) 
result = factorial(4) 
print(result)
print("")


"""14  """
def reverse_string(word): 
  if len(word) == 1: 
    return word 
  else: 
    return reverse_string(word[1:]) + word[0] 
result = reverse_string("Hello") 
print(result)
print("")


"""15  """
def binary_search(lst, target): 
  low = 0 
  high = len(lst) - 1 
  while low <= high: 
    mid = (low + high) // 2 
    if lst[mid] == target: 
      return True 
    elif lst[mid] < target: 
      low = mid + 1 
    else: 
      high = mid - 1 
    return False 
my_list = [1, 3, 5, 7, 9] 
result = binary_search(my_list, 5) 
print(result)
print("")


"""16  """
def is_palindrome(word): 
  return word == word[::-1] 
result = is_palindrome("radar") 
print(result)
print("")


"""17  """
def add_numbers(a, b): 
  return a + b 
result = add_numbers(2, 3) 
print(result)
print("")


"""18  """
def power_of_two(n): 
  if n == 0: 
    return 1 
  else: 
    return 2 * power_of_two(n - 1) 
result = power_of_two(3) # 2^ 3
print(result)
print("")


"""19  """
def increment(x): 
  x += 1 
  return x 
a = 5 
print(increment(a)) 
print("")


"""20  """
def count_vowels(word): 
  vowels = ['a', 'e', 'i', 'o', 'u'] 
  count = 0 
  for letter in word: 
    if letter.lower() in vowels: 
      count += 1 
  return count 
result = count_vowels("Hello World") 
print(result)
print("")


"""21  """
def fibonacci(n): 
  if n <= 1: 
    return n 
  else: 
    return fibonacci(n - 1) + fibonacci(n - 2) 
result = fibonacci(5) 
print(result)
print("")


"""22  """
def remove_duplicates(lst): 
  return list(set(lst)) 
my_list = [1, 2, 2, 3, 4, 4, 5] 
result = remove_duplicates(my_list) 
print(result)
print("")


"""23  """
def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    # # Recursive case: Find the maximum value in the rest of the list
    max_value = find_max(numbers[1:])
    # Return the maximum of the current element and the maximum value from the rest of the list
    return numbers[0] if numbers[0] > max_value else max_value
my_numbers = [3, 7, 2, 9, 4]
result = find_max(my_numbers)
print(result)
print("")


"""24  """
def func(lst=[1,2]):
  lst.append(100)
  return lst
lst1 = func()
lst2 = func()
lst3 = func()
# the default list is [1,2]
# the lists will be exactly the same, [1,2,100,100,100]
# because we run it 3 times
print(lst1,lst2,lst3)
print("")


"""25  """
def func(lst=[1,2]):
  lst.append(100)
  return lst
lst1 = func()
lst2 = func([]) # here we pass in an empty list
lst3 = func()
lst4 = func([44])
print(lst1,lst2,lst3,lst4)
print("")


"""26  """
def func(lst=[1,2]):
  lst.append(100)
  return lst
a = []
lst1 = func(a) # [1,2,100,100]
lst2 = func([]) 
lst3 = func(a) # [1,2,100,100]
lst4 = func([44])
print("")


"""27 Create a copy of the list """
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[:])
print("")


"""28 Reverse string  """
print(lst[::-1])
print("")


"""29 Replace the elements 2 and 3 to be 1  """
lst[2:4] = [1]
print(lst)
print("")


"""30 Modify the elements 2 and 3 to be 100 and 100  """
lst[2:4] = [100, 100]
print(lst)
print("")


"""31  """
contains = 2 in lst
print(contains)
print(lst.count(100)) # 2
print(lst.index(2)) # 1
print("")


"""32  """
print(lst.sort(reverse=True)) # descending order - returns None - does that inplace
print(lst)
print("")


"""32  """
print(lst.reverse()) # returns None - does that inplace
print(lst)
print("")


"""32  """
print(sorted(lst)) # returns the list of sorted elements
print("")


"""33 """
print(list(reversed(lst))) # returns an iterator so we have to wrap it in a list
print("")


"""34 """
lst = [1, 2, 3, 4, 5, 6, 7]
lst2 = lst[:]
lst2[0] = 100
print(lst, lst2)
print("")


"""35 zip """
names = ["Tim", "Joe", "Sam"]
ages = [23, 45, 33]
zipped = zip(names,ages)
print(list(zipped))
print("")


"""36 """
lst = [x for x in range(10)]
print(lst)
print("")


"""37 """
lst = [[x] for x in range(10) if x % 2 == 0] 
print(lst)
print("")


"""38 """
lst = [[x for x in range(10) if x % 2 == 0] for _ in range(2)] 
print(lst)
print("")


"""39 """
n1 = [x for x in range(10) if x % 2 == 0]
n2 = [x for x in range(10) if x % 2 != 0]
print(n1, n2)
# Zip the two lists together and reverse the resulting list of tuples
zipped = (list(zip(n1, n2)))
zipped2 = zipped[::-1]
print(zipped2)
print("")


"""40 """
# Insert the value 999 at index -5 in list 'n1'
n1[-5:-5] = [999]
print(n1)
# Replace elements at indices 1 to 4 in list 'n1' with the values 'a', 'b', and 'c'
n1[1:4] = ['a', 'b', 'c']
print(n1)
print("")


"""41 """
# Sort list 'n1' with a custom sorting order:
# - First, sort by whether the element is an integer or not
# - Second, sort in descending order
lst = sorted(n1, key=lambda x: (isinstance(x,int), x), reverse=True)
print(lst)
print("")