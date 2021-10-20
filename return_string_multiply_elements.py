#Given a string return the string where every char in the original,
#there are 2 same chars in the same order


str1 = 'Hello'
str2 = 'Alkis'
str3 = "John"	


def double_chars(string):
  to_return = ''
  for c in string:
	  to_return += c*2
  return to_return


print(double_chars(str1))
print(double_chars(str2))
print(double_chars(str3))