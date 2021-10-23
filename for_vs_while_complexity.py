#Python practise examples and tasks 
#more advanced than examples_and_tasks

import timeit
"""
Sum the numbers from 0 to n-1 in different ways
"""


#although the for and the while loop are essentially doing the same, the while loop takes longer than the for loop to run

def while_loop(n=100_000_000):
	i = 0
	s = 0 #sum
	#loop all numbers
	while i < n:
		s += 1
		i += 1
	return s


def for_loop(n=100_000_000):
	s = 0 #sum
	#loop all numbers
	for i in range(n):
		s += 1
	return s



def sum_range(n=20_000_000):
	return sum(range(n))



def main():
	print('while loop\t\t', timeit.timeit(while_loop, number =1))
	print('for pure loop\t\t', timeit.timeit(for_loop, number =1))

#dunder == double underscore 
#allows you to check whether the file is being run as a script or not 
#__main__ = scritp
#if __name__ = '__main__' is used to signal that this file is a script and you can run it
#if your file doesn't contain it then assume the file is used as a library or you should import it.
if __name__ == '__main__':
	main()
	