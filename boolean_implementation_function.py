#Write a function where if you input:
# True and True  you get: True
# True and False you get: False
# False and True  you get: True
# False and False  you get: True


def sleep_in(weekday, vacation):
  ##if not weekday or vacation:  #same as the statement below
  if (weekday == False) or (vacation == True):
    return True
  else:
    return False


#in python if an input is used and you type something it sets it to True so set it in the program instead!
weekday_input = input("Insert True or False for Weekday: ")
weekday_input = bool(weekday_input)  
vacation_input = [input("Insert True or False for Vacation: ")]
vacation_input = bool(vacation_input)  

weekday_input  = True
vacation_input = False

print(weekday_input)
print(vacation_input)
print(sleep_in(weekday_input, vacation_input))
# print(type(vacation_input))
# print(type(weekday_input))
