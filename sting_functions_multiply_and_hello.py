#this function returns the string you entered X times the input integer you entered
def string_multiplier(string1, integer1):
  return string1 * n

#this function just takes the string you entered and outputs hello Name !
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