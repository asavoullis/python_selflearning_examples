#Write a function that merges two sorted lists into a new sorted list.

def listMerge():
  list1 = [] 		#initialise the 2 sorted lists
  list2 = []		
  n = int(input('Enter number of elemnts for list 1 : '))	#select number of elements to add to list1
  for i in range(0, n):										#add the elements
    ele = int(input())
    list1.append(ele)
  p = int(input('Enter number of elemnts for list 2 : '))	#select number of elements to add to list2
  for i in range(0, p):										#add the elements 
    ele = int(input())
    list2.append(ele)
  
#remember both lists need to be sorted from before! But we can also sort them again, just to be sure :)
  list1.sort()
  list2.sort()
  list3 = []		#create a 3rd list that where we will merge them
  #1 index for each list
  index1=0			#initialise 2 indexes with initial value 0
  index2=0




#while the indexes are less than the length of the 2 lists
  while(index1 < len(list1) and index2 < len(list2)):	
#if the value of the first elemeent in list 1 is less than the value of the 1st element in the 2nd list   
    if list1[index1] < list2[index2]:
#add that list element at that index position to list3 and increment the index of the list 1	
      list3.append(list1[index1])			
      index1 += 1
    else:
#if not (element in list2 is higher) then add it  list3 and increment the index of the list 2
      list3.append(list2[index2])
      index2 += 1

#after the above while loop is done one put the rest of the values from list1 into list 3
  while ( index1 <  len(list1) ):
    list3.append(list1[index1])
    index1 += 1
#after the above while loop is done one put the rest of the values from list2 into list 3
  while ( index2 <  len(list2) ):
    list3.append(list2[index2])
    index2 += 1

  return list3

print(listMerge())
