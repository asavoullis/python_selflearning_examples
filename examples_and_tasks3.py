#Python practise examples and tasks 

import datetime


#in Python an assignment (d = 8) is not an expression, its a statement
#in other languages assignments are also expressions and return d back to you.
#python expressions were added in 3.8

def multiple_assignment_expression():
#parenthesis are there because they have to be, you are not allowed to assign multiple expressions together unless you put them in parenthesis
  (a := (b := (c := (d := 0))))
  #d:= 0 is gonna return 0
# := goes from right to left
# normal = goes from left to right
  print(a, b, c, d,) 

def equals_debugging():
  str_value = "other 😊"
  num_value = 1234
  print(f'the value is {str_value}')
  print(f'{str_value = }') 	#for debugging
  print(f'{num_value % 2 = }')
  print("\n")
  
def conversions():
  str_value = "other 😊"
  print(f'{str_value!a}') 	#conversts non ascii characters to an ascii version 
  print(f'{str_value!s}') 	#string conversion used for formating
  print(f'{str_value!r}')		#repr
  print("\n")

#empty class
class MyClass:
#all it does is define a format method which takes a format_spec and returns a string
	def __format__(self, format_spec) -> str:
		print(f'Myclass __format__ called with {format_spec=!r}')
		return "Myclass()"
	
def formatiing():
  num_value = 123.456
  now = datetime.datetime.utcnow()
  print(f'{now =: %Y-%m-%d}') #format for datetimes
  print(f'{num_value:.2f}')	#2 decimal places
  #blah blah %%MYFORMAT%% is a  passed as an argument, the format_spec argument 
  print(f'{MyClass(): blah blah %%MYFORMAT%%}')
  nested_format = ".2f"
  print(f'{num_value:{nested_format}}')
  print("\n")
	

def useful_function(x):
	return x * x 


class UsefulClass:
	def __init__(self, x):
		self.x = x

def do_it():
	for i in range(7):
		print(useful_function(i))

#or chained assignemnts - multiple equal signs
def multiple_assignment():
  c = d = e = f = []
  print(c, d, e,f)
  print("\n")

def tuple_assignment():
	a, b = 1,2
	print(a,b)
	print("\n")

def tricky_assignments():
#recursive cyclic structure   ... = cyclic reference
  #a becomes a member of its self b = []
  a, b = a[:] = [[]], []
  print(a, b)
  #tmp = [[]], []
  #a, b = tmp
#Assigns the contents of a to [[]], []
  #a[:] = temp
#we can confirm this using:
#shows us that the first element of a is a, confirming that we have this cyclic reference
  print(a is a[0])
  print("\n")

def tricky_assignemnt2():
  a,b = a[b] = a = [1,2,3], 2
  print(a,b)
  print("\n")
 


def main():
  equals_debugging()
  conversions()
  formatiing()
  multiple_assignment()
  tuple_assignment()
  tricky_assignments()
  multiple_assignment_expression()
  tricky_assignemnt2()

#dunder == double underscore 
#allows you to check whether the file is being run as a script or not 
#__main__ = script
#if __name__ = '__main__' is used to signal that this file is a script and you can run it
#if your file doesn't contain it then assume the file is used as a library or you should import it.
if __name__ == '__main__':
	main()
	









