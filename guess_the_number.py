#Guess the number game
from random import randrange

print("Guess the number from 0-1000")

#generate a random number between 0-1000
number = randrange(1000)

#print(number)

#keep trying until break
while True:
  #ask for user input 
  print("Make a guess of the number:")
  userinput = int(input())
  #if the input number from the user is the same as the number then 
  if number == userinput:
    print("You win!")
    break
  #else print lower if the input is lower than the number or bigger if the input is bigger than the number
  print("Smaller" if (number < userinput) else "Bigger" )