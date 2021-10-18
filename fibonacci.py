
#Program that calculates the sum of the first 100 even-valued Fibonacci numbers
#The Fibonacci sequence is defined as a sequence of integers starting with 1 and 1, where each subsequent value is the sum of the preceding two. I.e.
#f(0) = 1
#f(1) = 1
#f(n) = f(n-1) + f(n-2) where n >= 2

def countEven():
    count = 0;  #loop only for the first 100 numbers
    i = 0;      #initialize the sequence of numbers

    sumEven = 0;                                #initialize the sum          
    while count<100 :
        value = fib(i);                             #find the fibonacci
        if(value % 2 == 0):                         #check if the fibonacci number is even
          sumEven = sumEven + value;                    #if its even add it to the sum
          count+=1;                                     #increment by one 
        i+=1;                                       #incriment the sequence by 1
    return sumEven;

#take the Nth number of fibonacci, initialize the computed ie first 2 values of the fibonacci which are f(0)=1 f(1)=1
def fib(n, computed = {0: 1, 1: 1}):                    
    if n not in computed:                   #if we don't have the Nth number of the fibonacci then find it
        computed[n] = fib(n-2, computed) + fib(n-1, computed)               #f(n) = f(n-1) + f(n-2)
    return computed[n]                              #output the fibonacci number


print(countEven())
