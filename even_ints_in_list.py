#define function that checks if its an even number then takes the square of the number if its even and then adds it to the sum

inputlist1 = [1,2,3,4,5,6,7,9]   #3
inputlist2 = [5,8,15,33,5,6,8,2] #4
inputlist3 = [12,5,8,9,2,4,5,7,3,1,6,6] #6

def count_even_in_list(inputlist):  
	count = 0
	for x in inputlist:
		if x % 2 == 0:
			count += 1
	return count

print(count_even_in_list(inputlist1))
print(count_even_in_list(inputlist2))
print(count_even_in_list(inputlist3))