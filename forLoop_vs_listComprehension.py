"""  For Loops vs List Comprehensions, in Python

In this script I will be analysing the difference between For Loops and List Comprehensions in Python

The .py file (the code) in order to be executed needs to be passed through an intepreter.
The intepreter has 3 parts. The complier the bytecode and the python virtual machine (PVM).
The compiler scans your py file and simplifies its functionality into little instructions called Bytecodes.
These bytecodes then get sent to the PVM which reads this bytecode instructions and performs the corresponding 
functionality in C which is a much lower programming languange that the gets turned into machine code 
which is what runs on the CPU.

https://www.youtube.com/watch?v=U88M8YbAzQk
"""

import random
import time
import matplotlib.pyplot as plt

def for_loop(n):
    my_list = []
    for x in range(n):
        my_list.append(x)
    return my_list

def list_comprehension(n):
    return [x for x in range(n)]

# Repeat the experiment multiple times and calculate average execution time
num_trials = 10
execution_times_for_loop = []
execution_times_list_comprehension = []

for _ in range(num_trials):
    n = random.randint(10_000, 25_000_000)
    
    start = time.perf_counter()
    _ = for_loop(n)
    execution_time_for_loop = time.perf_counter() - start
    execution_times_for_loop.append(execution_time_for_loop)

    start = time.perf_counter()
    _ = list_comprehension(n)
    execution_time_list_comprehension = time.perf_counter() - start
    execution_times_list_comprehension.append(execution_time_list_comprehension)

# Calculate average execution time
avg_execution_time_for_loop = sum(execution_times_for_loop) / num_trials
avg_execution_time_list_comprehension = sum(execution_times_list_comprehension) / num_trials

print("Average execution time for for loop:", avg_execution_time_for_loop)
print("Average execution time for list comprehension:", avg_execution_time_list_comprehension)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_trials+1), execution_times_for_loop, label='For Loop')
plt.plot(range(1, num_trials+1), execution_times_list_comprehension, label='List Comprehension')
plt.xlabel('Trial')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time Comparison: For Loop vs List Comprehension')
plt.legend()
plt.grid(True)
plt.show()



""" looking into the bytecode of the function """
import dis
dis.dis(for_loop)
dis.dis(list_comprehension)