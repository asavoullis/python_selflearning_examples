""" Department Metrics

In a multination company, the performance data of the employees is given in three seprate arrays:
A: an arrray of strings containing the names of the employees.
D: an arrray of strings containing the department names for each employee.
T: an arrray of strings containing the number of tasks completed by each employee.

Print the metrics using the data:
The total number of employees in the department.
The average number of tasks completed by employees in the department. ( round in 2 decimal places)
The name of the employee with the highest number of tasks completed in the department.

In the provided code snippet, implement the provided departMetrics(...) method to print the mertics. 
There will be multiple test cases running so the input and output should match exactly as provided.

Input Format:
The first line contains an integer N, denoting the number of employees.
The second line contains N space-separated strings of array A, denoting the names of each employee.
The third line contains N space-separated strings of array D, denoting department names of each employee
The fourth line cotanins N space-separated integers of array T, denoting the number of tasks each employee completes.
The fifth line cotains a string dept, denoting the department name for whcih the performance must be calculated

Output Format:
The output contains space-separated values denoting the total number of employees in the given department, 
the average number of tasks completed by employees in the department rounded to 2 dp, and the name of the employee 
with the highest number of tasks completed in the department.

Sample Output:
2 11.0 Bob

"""
def calculate_performance(N, A, D, T, dept):
# def departmentMetrics():
    # # These can be used for inputs but I hard coded them
    # N = int(input("Enter the number of employees: "))  # Number of employees
    # A = input("Enter names of employees separated by spaces: ").split()  # Names of employees
    # D = input("Enter department names of employees separated by spaces: ").split()  # Department names of employees
    # T = list(map(int, input("Enter number of tasks completed by each employee separated by spaces: ").split()))  # Number of tasks completed by each employee
    # dept = input("Enter the department for which performance must be calculated: ")  # Department for which performance must be calculated

    # Initialize variables to store the metrics
    total_employees = 0
    total_tasks = 0
    max_tasks = -1
    employee_max_tasks = ""

    # Iterating through each employee
    for i in range(N):
        if D[i] == dept:
            total_employees += 1
            total_tasks += T[i]
            if T[i] > max_tasks:
                max_tasks = T[i]
                employee_max_tasks = A[i]

        print(i, N, D, D[i], total_employees, total_tasks, employee_max_tasks, max_tasks)

    # Calculate the average number of tasks, if there are employees in the department
    avg_tasks = round(total_tasks / total_employees, 2) if total_employees > 0 else 0

    result = f"{total_employees} {avg_tasks} {employee_max_tasks}"
    print("\n Performance Metrics for Department\n", dept, ":", result, "\n")

# Provided inputs
N = 3
A = ["John", "Bob", "Greg"]
D = ["Marketing", "Economics", "Science"]
T = [3, 5, 2]
dept = "Marketing"

# Run the function with provided inputs
calculate_performance(N, A, D, T, dept)


################################################################


def departMetrics(N, A, D, T, dept):
    # Initialize variables to store metrics
    total_employees = 0
    total_tasks = 0
    max_tasks = 0
    max_tasks_employee = ""

    # Iterate through employees' data
    for i in range(N):
        if D[i] == dept:
            total_employees += 1
            total_tasks += T[i]
            if T[i] > max_tasks:
                max_tasks = T[i]
                max_tasks_employee = A[i]

    # Calculate average tasks
    average_tasks = total_tasks / total_employees if total_employees > 0 else 0

    result = f"{total_employees} {average_tasks} {max_tasks_employee}"
    print("\n Performance Metrics for Department\n", dept, ":", result, "\n")



# Read input
print("Please entere the input for the department Metrics:")
N = int(input())
A = input().split()
D = input().split()
T = list(map(int, input().split()))
dept = input()

# Call departMetrics function
departMetrics(N, A, D, T, dept)

"""
5
John Alice Bob Mary Peter
HR Sales HR Sales Finance
10 8 12 6 14
HR


Answer: 2 11.00 Bob
"""