# Python practise examples and tasks 6

"""1 """
my_str = "ThIs Is a mESsy sTrInG"
def my_function():
    # Use the global keyword to indicate that we are modifying the global variable my_str
    #is used to indicate that the variable my_str refers to the global variable, not a local one. 
    # This means that changes made to my_str inside the function will affect the global variable.
    global my_str

    my_str = my_str.lower()
    return my_str

print(my_function()) # ThIs Is a mESsy sTrInG
print("")


"""2  """
def my_function(_list, _int):
  new_int = _int * 10
  _list.append(new_int)
  return _list
l = []
v = 2 
print(my_function(l, v)) #[20]
print("")


"""3  use numpy to make a 2d array from two 1d arrays """
import numpy as np
list_a = [12,14,16,18]
list_b = [2,4,6,8]
x = np.array([list_a, list_b])
print(x)
print("")


"""4  use Counter from the collections library to find the occurances of each element """
from collections import Counter
chars = [0, 3, 1, 2, 3, 2, 3, 1, 2, 3]
char_count = Counter(chars)
print(char_count.most_common(3))
# [(3, 4), (2, 3), (1, 2)] # (element,count), (element,count)
print("")


"""5  check if 'c' is a key in the d dictionary and print its value else return c """
d = {'a':0, 'b':1, 'c':2, 'd':3}
if 'c' in d :
  print(d['c'])
else:
  print('c')
print("")


"""6 Output a list with booleans checkign if each element is above 6 """
costs = [8, 5, 7, 9]
print(np.array(costs) < 6)
print(list(map(lambda x: x < 6, costs)))
print("")


"""7 Generate an array of odd numbers using numpy """
arr = np.arange(1,20,2 )
print(arr)
print("")


"""8  Perform an extended slice to select list items from the beginning up to (but not
including) the third indexed item."""
prices = [12.99, 14.97, 2.49, 1.35]
print(prices[:3])
print("")


"""9 Print the size and shape of the array """
print("array x:","\n",x)
print("Size: ",x.size )
print("Shape: ",x.shape)
print("")


"""10  checking if array elements are above 5 """
arr1 = np.array([1,5,7,9,12])
arr2 = ( arr1 > 5)
print(arr2)
print("")


"""11 Calculate the mean and standard deviation of the arr1 array """
print("Mean: ",np.mean(arr1))
# Print the standard deviation
print("Std dev: ",np.std(arr1))
print("")


"""12 Use a for loop to print the elements in the arr1 array """
for val in arr1:
  print(val)
print("")


"""13  Print items and values in the dict """
practice = {'python': 100, "r": 30, "sql": 10}
for course, number in practice.items():
  print(course + " practice has " + str(number) + " items")


"""14  Creating a df from dict """
import pandas as pd
data = {'DEVICE': ['MOBILE', 'DESKTOP'],
        'active': ['yes', 'no'],
        'login_id': [12347, 11021]}
df = pd.DataFrame(data)
print(df)
print("")


"""15  Adding more values to the df """
new_data = {'DEVICE': ['Iphone', 'PC', 'TABLET', 'LAPTOP'],
            'active': ['yes', 'no', 'yes', 'yes'],
            'login_id': [12127, 14543, 45678, 78901]}
df = pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)
print(df)
print("")


"""16 Make a new column and make it capitalized """
df['device'] = df['DEVICE'].apply(str.capitalize)
print(df)
print("")


"""17 Print the dataframe with login_id values less than 15000 """
is_less = df["login_id"] < 15000
print(df[is_less])
print("")


"""18 Print the elements of the arrays within the practise array"""
practice = [["python", 100],
            ["r", 60],
            ["sql", 45]]
for item in practice:
  print("the " + item [0] + " course has " + str(item[1]) + " item")
print("")


"""19 Make a dataframe with the following data and make the index the chapter """
data = {'chapter': ['P', 'R', 'S'],
        'course': [1, 2, 3],
        'technology': ['Data Science', 'Data Visualization', 'Databases'],
        'language': ['Python', 'R', 'SQL']}
df2 = pd.DataFrame(data)
df2.set_index('chapter', inplace=True)
print(df2)
print("")


"""20 Display the dataframe but only the data for language for rows 1 and 2 """
print(df2.iloc[[1, 2], [2]])
print("")


"""23 Print the dataframe with course number greater than 2 """
print(df2[df2["course"] > 2])
print("")


"""22 Use np.nditer() to iterate over the array """
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Using np.nditer() to iterate over the array:")
for element in np.nditer(arr2):
    print(element, end=" ")
print("")


"""23 Modifying the array values using np.nditer() """
print("\n\nModifying array values using np.nditer():")
for index, value in np.ndenumerate(arr2):
    arr2[index] = value * 2
print(arr2)
print("")


"""24 Use enumerate() to iterate over the array values """
q = [10.01, 19.08, 9.6, 6.2]
for k , z in enumerate(q):
  print('Item ' + str(k) + ' -', str(z))
print("")


"""25 Print the entry with index P """
# This statement returns a Pandas Series
print(df2.loc['P'])
print("")


"""26 Print the entry with index P PART2 """
# This statement returns a Pandas DataFrame
print(df2.loc[['P']])
print("")


"""27 Whenever you store mutable objects you are storing a refrence to them. Demonstrate that """
lst = ['a', 'b', 'c', 1, True, "abc2"]
lst2 = lst
lst2[0] = 100
print(lst2, "\n",lst)
print("")


"""28  """
rotation_period = {
   'earth': 1.0,
   'jupiter': 0.415,
   'saturn': 44}
# changing the value of a key in the dictionary 
rotation_period['saturn'] = 0.445
print(rotation_period)
print("")


"""29 """
data = {'person': ['a', 'b', 'c', 'd'],
        'year': [2003, 2007, 2011, 2015],
        'winner': ['Australia', 'Australia', 'India', 'Australia']}
cricket_wc_venues = pd.DataFrame(data)
cricket_wc_venues.set_index('person', inplace=True)
# Using the loc indexer to access the 'year' column for the row with index label 'd'
print(cricket_wc_venues.loc['d', ['year']])
print("")


"""30 """
x = np.array([0, 4, 4])
for j in x:
  # you need to convert it to str because the print function expercts all arguments to be of the same type
  print( str(j) + ' km')
print("")


"""31 """
ratio_to_earth = {
'mercury': {'density': 0.984},
'mars': {'density': 0.713}
}
print(ratio_to_earth)
print("")


"""32 """
x = {"apple": 1, "banana": 2, "cherry": 3} 
result = x.get("pear", 0) 
print(result) # 0 if key pear is in the dict print its value else 0 
print("")


"""33 """
x = {"apple": 1, "banana": 2, "cherry": 3} 
result = "apple" in x 
print(result) # TRUE
print("")


"""34 Concat the 2 lists"""
x = [1, 2, 3] 
y = [4, 5, 6] 
result = x + y 
print(result) # [1, 2, 3, 4, 5, 6]
# The extend method modifies the list in place and returns None
result2 = x.extend(y) 
print(x)
print("")


"""35 Reversing a string """ 
x = "Python" 
result = x[::-1] 
print(result)
print("")


"""36 append an element in the array and print  """
x = [1, 2, 3] 
result = x.append(4) 
print(result) # Returns None
print(x)
print("")


"""37 pop element from array and print it  """
x = [1, 2, 3] 
result = x.pop() 
print(result) # will pop the removed element, 3 
print("")


"""38 """
my_tuple = (1, 2, 3, 4, 5) 
count_of_3 = my_tuple.count(3) 
print(count_of_3)
print("")


"""39 """
my_list = [1, 2, 3, 4, 5] 
repeated_list = my_list * 2 
print(repeated_list)
print("")


"""40 """
my_tuple = (1, 2, 3) 
new_tuple = my_tuple + (4, 5, 6) 
print(new_tuple)
print("")


"""41 """
my_tuple = (1, 2, 3) 
new_tuple = my_tuple * 2 
print(new_tuple)
print("")


"""42 use del to remove elements from list """
my_list = [1, 2, 3, 4, 5] 
del my_list[1:4] 
print(my_list)
print("")

"""43 """
my_list = [1, 2, 3, 4, 5] 
del my_list[1:4] 
print(my_list)
print("")


"""44 """
my_list = [1, 2, 3, 4, 5] 
my_list.remove(3) # will remove the element 3 from the list
print(my_list)
print("")


"""45 Slicing a tuple """
my_tuple = (1, 2, 3, 4, 5) 
sliced_tuple = my_tuple[1:4] 
print(sliced_tuple)
print("")


"""46 Insert a new element into the list at a specified index - push the rest of the list back """
my_list = [1, 2, 3, 4, 5] 
# insert the elemnt 10 at index 2, does not overwrite, pushes elements back
my_list.insert(2, 10) 
print(my_list)
print("")


"""47 Remove all elements from the list """
my_list = [1, 2, 3, 4, 5] 
my_list.clear() # removes all elements in the list, makes it []
print(my_list)
print("")


"""48 Append a list to the end of the list """
my_list = [1, 2, 3] 
my_list.append([4, 5]) # [1, 2, 3, [4, 5]]
print(my_list)
print("")


"""49 Sum of tuple """
my_tuple = (1, 2, 3) 
sum_of_tuple = sum(my_tuple) 
print(sum_of_tuple)
print("")
