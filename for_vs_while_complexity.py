#Python practise examples and tasks 
#more advanced than examples_and_tasks

import timeit
import numpy

"""
Sum the numbers from 0 to n-1 in different ways
"""

#although the for and the while loop are essentially doing the same, the while loop takes longer than the for loop to run
def while_loop(n=50_000_000):
	i = 0
	s = 0 #sum
	#loop all numbers
	while i < n:
		s += 1
		i += 1
	return s


#python range doesnt create an array in memory - you can run it without any worries in memory constrains
def for_loop(n=50_000_000):
	s = 0 #sum
	#loop all numbers
	for i in range(n):
		s += 1
	return s


#built-in functions take even less time than loops
def sum_range(n=50_000_000):
	return sum(range(n))


#we use numpy functions instead of python functions because python is slow thus we use numpy which is writen in c,
def numpy_sum(n=50_000_000):
  return numpy.sum(numpy.arange(n))
#much faster because entire operation is written in c, this whole function is 1 c call, both the iteration and the adding itself is done in c.
#the downside is that arange creates a whole array in memory 


#fastest way to calulate it is to use math knowledge - we are adding the first n-1 integers therefore: we can use this formula 
def sum_math(n=50_000_000):
  return (n *(n-1)) // 2




def main():
  print('while loop\t\t', timeit.timeit(while_loop, number =1))
  print('for pure loop\t\t', timeit.timeit(for_loop, number =1))
  print('built in sum func\t\t', timeit.timeit(sum_range, number =1))
  print('built in sum func\t\t', timeit.timeit(numpy_sum, number =1))
  print('built in sum func\t\t', timeit.timeit(sum_math, number =1))

#dunder == double underscore 
#allows you to check whether the file is being run as a script or not 
#__main__ = scritp
#if __name__ = '__main__' is used to signal that this file is a script and you can run it
#if your file doesn't contain it then assume the file is used as a library or you should import it.
if __name__ == '__main__':
	main()
	

#conclusion:
#the fastest way to loop in python is to:
#not to loop in python 
# try to compute the answer mathamtically ahead of time definately do that
# loop in a c built in function such as numpy library
# call a c function that can do the looping 
# use python builtin functions like sum or map 
# use for loop
#use while loop