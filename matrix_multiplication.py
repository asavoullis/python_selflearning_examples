import numpy as np

# Given matrices A and B
A = np.array([[2.7, 1.8, 2, 9],
              [10, 20, 30, 40],
              [5, 7.5, 9, 4.8],
              [6.2, 1, 2, 3]])

B = np.array([[2.7, 1.8, 2, 9],
              [10, 20, 30, 40],
              [5, 7.5, 9, 4.8],
              [6.2, 1, 2, 3]])


# Only if the columns in the first matrix is equal to the number of rows in the second matrix.
# if A is an m × n matrix, and B is an n × p matrix, the resulting matrix will be an m × p matrix.

# A is of size 2 × 3  and B is of size 3 × 4, the resulting matrix C will be of size 2 × 4.
# A: 2 rows and 3 columns
# B: 3 rows and 4 columns
# C:    2 × 4

if __name__ == "__main__":
  A1 = np.random.randint(5, size=(2,2))
  B1 = np.random.randint(5, size=(2,2))
  result = np.dot(A1, B1)
  print("Matrix Multiplication Result of A1 and B1 :")
  print(result, "\n")

  result = np.dot(A, B)
  print("Matrix Multiplication Result of A and B :")
  print(result, "\n")

  