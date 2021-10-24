#Python practise examples and tasks 

print("Task 1: Print the cube of the ints inside a list.")
#cube number
num = [2,5,7,3,2,4]
cube = []
for i in num:
#add to the list the element to the power of 3
	cube.append(i**3)
print("Cube of ints in list: {}".format(cube))
print("\n")



print("Task 2: Prints a patern depending on users input. ")
#pattern printing with user input
#asks the user to enter a number as input, wil return error if not integer
n = int(input("Enter the number of rows: "))
  #nested LOOPS
#first we loop by how many rows the user has set
for i in range(0,n):
#then we loop with addition of 1 because python starts from 0
	for j in range(0, i+1):
		print("*", end = "")
	print()
print("\n")



print("Task 3: use the break. ")
#print only the first numbers of the first 10 numbers using break
for i in range(1, 10):
	if(i == 6):
		break
	print(i, end = " ")
	
print("\n")



print("Task 4: Type the word Gilly .")
#make the user enter the word Gilly!
while True:
  name = input()
  if name.lower() == 'gilly':
    break
  elif name == "Gilly":
    break
  elif name.upper() == "GILLY":
    break
print("Finally!")
print("\n")



print("Task 5: Print the average of positive integer numbers, enter a negative integer to stop. ")
#output the average of positive numbers
num5 = 0
count = 0 
sum = 0
#countineu until the user inputs a negative number 
while num5 >= 0:
#note here that characters or strings will result in error

#ask the user to input a number
	num5 = int(input('Enter any number: '))
	if num5 >= 0:
		count = count+1
		sum = sum + num5
avg = sum/count
print('Total sum of numbers: ', sum, 'Average: ', avg)
print("\n")



print("Task 6: Reverse order print the strings in a list. ")
#reverse sort the string list 
players = ['Messi', 'Benzema', 'Neymar','Ronaldo', 'Salah', 'Harry', 'Rooney']
for i in sorted(players, reverse = True):
	print(i)
print("\n")



print("Task 7: Sort the dictionary. ")
#Sort the dictionary
dictio = {'f': 1, 'b':4, 'a':3, 'e':9, 'c':2}
for x in sorted(dictio.items()):
	print(x)
print("\n")



print("Task 8: Output only the even aged animals. ")
#Sort the dictionary
animals = [{'name': "Dog", "age": 11}, {'name': "Cat", "age": 16},
{'name': "Elephant", "age": 44},{'name': "Tiger", "age": 33}]
for animals in filter(lambda i: i["age"] %2 ==0, animals):
	print(animals)
print("\n")



print("Task 9: Weekday or Vacation. ")
## BOOLEAN IMPLIMENTATION FUNCTION ##
#Write a function where if you input:
# True and True  you get: True
# True and False you get: False
# False and True  you get: True
# False and False  you get: True
def sleep_in(weekday, vacation):
  ##if not weekday or vacation:  #same as the statement below
  if (weekday == False) or (vacation == True):
    return True
  else:
    return False

#in python if an input is used and you type something it sets it to True so set it in the program instead!
#weekday_input = input("Insert True or False for Weekday: ")
#weekday_input = bool(weekday_input)  
#vacation_input = [input("Insert True or False for Vacation: ")]
#vacation_input = bool(vacation_input)  

#setting the input values manually here. ignore 16-20 lines.
weekday_input  = True
vacation_input = False

#debugging
#print(weekday_input)
#print(vacation_input)
print(sleep_in(weekday_input, vacation_input))
# print(type(vacation_input))
# print(type(weekday_input))
print("\n")



print("Task 10: Check how many even numbers in a list using a function. Additionally, if it finds a number takes squares it and adds it to the sum. ")
#Create function that checks if its an even number then takes the square of the number if its even and then adds it to the sum -VERSION 2
inputlist1 = [1,2,3,4,5,6,7,9]   #3
inputlist2 = [5,8,15,33,5,6,8,2] #4
inputlist3 = [12,5,8,9,2,4,5,7,3,1,6,6] #6

def count_even_in_list(inputlist):
  sumofeven = 0
  count = 0
  #loop over the elements in the list
  for x in inputlist:
  #if that element when divided by 2 has a remainder of 0 (its even)
    if x % 2 == 0:
	#add one to the count
      count += 1
	#add the square of that number to the sum
      sumofeven = sumofeven + x**2
  return count, sumofeven

count_even_in_list(inputlist1)
print(f"We have {count_even_in_list(inputlist1)[0]} even integers in {inputlist1}, with a sum of {count_even_in_list(inputlist1)[1]}")

count_even_in_list(inputlist2)
print(f"We have {count_even_in_list(inputlist2)[0]} even integers in {inputlist2}, with a sum of {count_even_in_list(inputlist2)[1]}")

count_even_in_list(inputlist3)
print(f"We have {count_even_in_list(inputlist3)[0]} even integers in {inputlist3}, with a sum of {count_even_in_list(inputlist3)[1]}")
print("\n")



print("Task 11: Check if the first or the last element in a list is 7. ")
#given an array of ints within a list check if the first or the last element is a 7
#if its a 7 print True else False
list1 = [7,5,6,8,9,6,7,8]
list2 = [77,5,6,8,9,6,7,78]
list3 = [9,5,6,8,9,6,7,7]

def first_last_7(nums):
#if the first element of the list or the last element of the list is 7
  if nums[0] == 7 or nums[-1] == 7:
    return True
  else:
    return False
	
print(f"In {list1} its {first_last_7(list1)}")
print(f"In {list2} its {first_last_7(list2)}")
print(f"In {list3} its {first_last_7(list3)}")
print("\n")



print("Task 12: Return the string with every chracter outputted twice in the same order. ")
#Given a string return the string where every char in the original,
#there are 2 same chars in the same order
str1 = 'Hello'
str2 = 'Alkis'
str3 = "John"	

def double_chars(string):
#initialize an empty string
  to_return = ''
#loop over the inputted string
  for c in string:
#add 2 times the character in a string
	  to_return += c*2
  return to_return

print(double_chars(str1))
print(double_chars(str2))
print(double_chars(str3))
print("\n")



print("Task 13: String manipulation with the input of the user. ")
#this function returns the string you entered X times the input integer you entered
def string_multiplier(string1, integer1):
#just multiply the inputted string n times
  return string1 * n

#this program just says hello to your inputted string!
def hello_name(nam):
  return "Hello " + nam + "!"

# Using a while True loop to get the different elements for a list of integers.
while True:
      number1 = input("Please enter an integer: ")
      try:
          n = int(number1)  
          #used for testing
          #print("Input is an integer number.")
          #print("Input number is: ", n)
          break;
          #if not an integer
      except ValueError:
          print("This is not an integer.\nPlease enter a valid integer...") 

name = input("Please enter your name: ")
print(hello_name(name))
print(string_multiplier(name, n))
print("\n")

print("Task 14: Using context manager - with. ")
#using with allows you not to have to have to close that file manually  f.close() - this is not only for files, its whenever you are setting up and tearing down resources eg threads and releasing logs OR with databases
with open('test.txt', 'r') as f:    #opens the file
	file_contents = f.read()          #reads the file

#splits the number of words and saves them as elements in a list called words
#it parses over the file contents and splits the words whenever there is a space
words = file_contents.split(' ')     
print(words)

#counts the number of elements inside the list 
word_count = len(words)
print(f'There are {word_count} words')
