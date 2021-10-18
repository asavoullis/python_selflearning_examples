#define function that checks if its an even number then takes the square of the number if its even and then adds it to the sum
def sumofsquares(list):  

  ESumsquares = 0
  for x in list:  #loop through a given list
    if x % 2 == 0:   #check if even
      ESumsquares = ESumsquares + (x * x)  #square it and then add to sum
  return ESumsquares

list=[] #create a list 
#asks for how many elements will be in the list to see the length of the list
print("insert only 1 number each time please")
n = int(input('Enter number of elements for list 1 : '))   
for i in range(0, n):         
  ele = int(input())
  list.append(ele)


print("Sum of the squares of all even numbers of that list:")
print(sumofsquares(list))
