#Python practise examples and tasks 

#used for taks5 
import sys 

#used for task7 	
from collections import Counter


"""
Task1: Iterate with enumerate instead of range + len
"""
def iterate_with_enumerate():
#iteration 	
	print("Task1:")
	data = [1, 2, -4, -3, 2]
	#for i in range(len(data)):
		#if data[i] < 0:
			#data[i] = 0

#the enumerate function returns both the element and its index as a tuple
	for idx, num in enumerate(data):
		if num < 0:
			data[idx] = 0		
	print(data)
	print("\n")



"""
Task2: Use list comprehension instead  of raw for loops
"""
def list_comprehension(): 
#lets create a list with all the squared numbers between 0-9
	print("Task2:")
	#squares = []
	#for i in range(10):
		#squares.append(i*i)
	#square every element from 0 to 9
	squares = [i*i for i in range(10)]
	print(squares)
	print("\n")



"""
Task3: Sort complex iterables with the sorted method
"""
def sort_complex_iterables():
#sort the list 
	print("Task3:")
	data = [3, 5, 1, 11, -2]
	sorted_data = sorted(data, reverse = True)
	print(sorted_data)

#lets now say we have a complex iterable
	data2 =[{"name": "Max", "age": 6},
	{"name": "Lisa", "age": 20},
	{"name": "Ben", "age": 9}]
	sorted_data2 = sorted(data2, key=lambda x: x["age"])
	print(sorted_data2)	
	print("\n")



"""
Task4: Store unique values with sets
"""
def store_unique_values_with_sets():
#need to have only unique values in a list
	print("Task4:")
	my_list = [1,2,3,3,4,5,6,7,7,7,7]
	
#a set is an unordered collection data type that has no duplicate elements - so in this case it removes all the duplicate elements 
	my_set = set(my_list)
	print(my_set)
#you can create a set with curly bracers. This allows python to make some optimizations and it also has some handy methods for calculating the intersections and differences of sets.
	primes= {2,3,5,7,11,13,17,19}
	print(primes)
	print("\n")



"""
Task5: Save memory with generators 
"""
def save_memory_with_generators(): 
#lets save memory when doing caluclations with huge numbers
	print("Task5:")
#we might get in trouble with the memory using a list
	my_list = [i for i in range(10000)]
	print(sum(my_list))
	print(sys.getsizeof(my_list), "bytes") #87632 bytes
#use generators instead that has the same syntax but uses parenthesis instead of square brackets 
	my_gen = (i for i in range(10000))
#a generator produces the elements one at a time and only when asked for it 
	print(sum(my_gen))
	print(sys.getsizeof(my_gen), "bytes") #128 bytes
	print("\n")	



"""
Task6: Define default values in dictionaries with .get and .setdefault
"""
def define_default_values_dicts():
#lets use .get and .setdefault to define default values in dictionaries 
  print("Task6:")
  my_dict ={"item": "football", "price": 10.00}
#lets get the count of the items and assume that the count key is also contained in the dictionary
	#count = my_dict["count"] #this will crash our code and raise a key error
	
#this will also return the value for the key but it will not raise a key error if the key is not available, it instead returns a default value in this case. If you don't specify a default value it will return nan .
  count = my_dict.get("count", 0.0)
  print(count)
  print('count: ', my_dict.get('count'))
#if you  want to ask our dictionary for the count and we also want to update the dictionary and put in the count - if its not there - then we can use setdefault with the default value that we specify it. The next time we check the key is now available in our dictionary.
  count = my_dict.setdefault("count", 0)
  print(count)
  print(my_dict)
  print("\n")	



"""
Task7: Count hashable objects with collections.Counter
"""
def count_hashable_objects(): 
#if you need to count the number of elements in your list there is a very handy tool in the collections module 
	print("Task7:")
	my_list = [10,10,10,5,5,2,8,7,6,6,6,6,6]
	counter = Counter(my_list)
	#this will return a dictionary with the elements as keys and their frequency - sorted with the most common item in the front.
	print(counter)
	#to print how many times it has 10 , if none then returns 0
	print(counter[10])
	#find easy the most common items
	#we can also specify if we want the most or the one before by chaning the number in the bracket
	most_common = counter.most_common(1)
	print(most_common)
	
	#this will return a list of tuples each tuple has the value as the first item and the count as the second item so if you just want to have the value of the very most common item we first call the most common method with argument one and then we access index 0 in our list and then again 0 to get the value	
	print(most_common[0][0])
	print("\n")	
	
	
"""
Task8: Format strings with f-strings
"""
def formating_strings(): 
#lets format strings!
	print("Task8:")
	name = "Alex"
	my_string = f"Hello {name}"
	print(my_string)
	i = 10
	print(f"{i} squared")
	print("\n")		



"""
Task9: Concatenate strings with .join
"""
def formating_strings(): 
#combine all elements in taht list separated by a space between each word
	print("Task9:")
	list_of_strings = ["Hello", "my", "friend"]

#bad way 
#as you know string is an immutable element so here we have to create new strings each time. This code will be slow for large lists - avoid it - use join
	#my_string = ""
	#for i in list_of_strings:
	#	my_string += i + ""
	
#this combines all the elements into one string and uses the string in the begining as a separator so here we use a string with only a space , we can also use commas "," between each word	
	my_string = " ".join(list_of_strings)
	print(my_string)
	print("\n")	
	
	
	
"""
Task10: Merge dictionaries with a **
"""
def merge_dictionaries_double_star(): 
#merge 2 dictionaries 
	print("Task10:")
	d1 = {"name": "Alex", "age": 25}
	d2 = {"name": "Alex", "city": "New York"}
#our combined dictionary has all the keys in it 
	merged_dict = {**d1, **d2}
	print(merged_dict)
	print("\n")		


	
"""
Task11: Simplify if statements with if x in list 
"""
def simplify_if_statements_ifxin(): 
#simplify if statements with if x in list instead of checking each item separately 
	print("Task11:")
	colors = ['red', 'green', 'blue']
	c = 'red'
	if c in colors:
		print(f'Yes {c} is in the {colors} list.')
	print("\n")	




def main():
	iterate_with_enumerate()
	list_comprehension()
	sort_complex_iterables()
	store_unique_values_with_sets()
	save_memory_with_generators()
	define_default_values_dicts()
	count_hashable_objects()
	formating_strings()
	merge_dictionaries_double_star()
	simplify_if_statements_ifxin()
	
if __name__ == '__main__':
	main()
	


