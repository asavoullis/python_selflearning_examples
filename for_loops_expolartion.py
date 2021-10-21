#Python loops exploration

#cube number
num = [2,5,7,3,2,4]
cube = []
for i in num:
#add to the list the element to the power of 3
	cube.append(i**3)

print("Task1: prints cube of the list: {}".format(cube))
print("\n")

#pattern printing with user input
print("Task2: prints a patter depending on users input")
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

print("Task3: use the break")
#print only the first numbers of the first 10 numbers using break
for i in range(1, 10):
	if(i == 6):
		break
	print(i, end = " ")
	
print("\n")



print("Task4: Type the word Gilly")
#make the user enter the word Gilly!
while True:
	name = input()
	if name == 'Gilly':
		break
print("Finally!")
print("\n")



print("Task5: Print the average of positive numbers, enter a negative number to stop.")
#output the average of positive numbers
num5 = 0
count = 0 
sum = 0
while num5 >= 0:
	num5 = int(input('Enter any positive number: '))
	if num5 >= 0:
		count = count+1
		sum = sum + num5
avg = sum/count
print('Total sum of numbers: ', sum, 'Average: ', avg)
print("\n")



print("Task6: Reverse order print the strings in a list.")
#reverse sort the string list 
players = ['Messi', 'Benzema', 'Neymar','Ronaldo', 'Salah', 'Harry', 'Rooney']
for i in sorted(players, reverse = True):
	print(i)
print("\n")


print("Task7: Sort the dictionary.")
#Sort the dictionary
dictio = {'f': 1, 'b':4, 'a':3, 'e':9, 'c':2}
for x in sorted(dictio.items()):
	print(x)
print("\n")

	
print("Task8: Output only the even aged animals.")
#Sort the dictionary
animals = [{'name': "Dog", "age": 11}, {'name': "Cat", "age": 16},
{'name': "Elephant", "age": 44},{'name': "Tiger", "age": 33}]
for animals in filter(lambda i: i["age"] %2 ==0, animals):
	print(animals)
print("\n")










