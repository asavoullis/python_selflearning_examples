#define function that checks if its an even number then takes the square of the number if its even and then adds it to the sum
def sumofsquares(list):  

  ESumsquares = 0
  for x in list:  #loop through a given list
    if x % 2 == 0:   #check if even
      ESumsquares = ESumsquares + (x * x)  #square it and then add to sum
  return ESumsquares
      
list=[] # Create a list to store the integers.
#asks for how many elements will be in the list to see the length of the list
print("Insert only 1 number each time please.")

# Using a while True loop to get the different elements for a list of integers.
while True:
      numberofelements = input("Please enter an integer for the number of elements in the list: ")
      try:
          n = int(numberofelements)  
          #used for testing
          #print("Input is an integer number.")
          #print("Input number is: ", n)
          break;
          #if not an integer
      except ValueError:
          print("This is not an integer.\nPlease enter a valid integer for the number of elements in the list...") 

# Using a for loop to get the different elements for a list of integers.
for i in range(0, n): 
  while True: #while 
      num = input("Please enter an integer: ")
      try:
          val = int(num)
          list.append(val)
          #print("Input is an integer number.")
          #print("Input number is: ", val)
          break;
      except ValueError:
          print("This is not an integer.\nPlease enter a valid integer...")
#n = int(input('Enter number of elements for list 1 : '))   
#for i in range(0, n):         
#  ele = int(input())
#  list.append(ele)



print("Sum of the squares of all even numbers of that list:")
print(sumofsquares(list))