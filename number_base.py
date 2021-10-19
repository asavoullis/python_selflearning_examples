#Write a function that when passed two unsigned integers, a value and a base. It should print the supplied value in the supplied base. The base is in the range 2 to 36, and digit values greater than 9 are represented in the output by the alphabetic characters such that 10 is 'A' etc.




def Converter(number,base):
#create a list of the all the possible outputs
    convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
#check if the integer is between 2 and 36
    if base < 2 or base > 36:  
        return('Wrong parameters')
    else:
#if the number is lower than the base then convert it to string 
        if number < base:
            return convertString[number]
        else:
#else convert if higher then number diveided by the base and the remainder to string
            return Converter(number//base,base) + convertString[number%base]
            

            
n = int(input('Enter the value:'))
p = int(input('Enter the base (from 2 to 36):'))

Converter(n,p)
print(Converter(n,p))

