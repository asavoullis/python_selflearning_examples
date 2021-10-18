
#Program that calculates the sum of the first 100 even-valued Fibonacci numbers
#The Fibonacci sequence is defined as a sequence of integers starting with 1 and 1, where each subsequent value is the sum of the preceding two. I.e.
#f(0) = 1
#f(1) = 1
#f(n) = f(n-1) + f(n-2) where n >= 2

def countEven():
    count = 0;
    i = 0;
    sumEven = 0;
    while count<100 :
        value = fib(i);
        if(value % 2 == 0):
          sumEven = sumEven + value;
          count+=1;
        i+=1;
    return sumEven;

def fib(n, computed = {0: 1, 1: 1}):
    if n not in computed:
        computed[n] = fib(n-2, computed) + fib(n-1, computed)
    return computed[n]


print(countEven())
