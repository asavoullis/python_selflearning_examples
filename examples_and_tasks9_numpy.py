# Python practise examples and tasks 9
import numpy as np

# numpy arrays can only contain a single data type.

"""1  Numpy reshape """
arr = np.array([8, 4, 2, 9, 8, 2])
arr.reshape((6, 1))
print(arr)
print("") 


"""2 Documentation for numpy function """
# help(np.ndarray.reshape)
print("")


"""3 AsType """
# Convert array elements to Unicode strings with a maximum length of 3 characters
result = arr.astype("<U3")
print(result)
print("")


"""4 Stack """
arr_1 = np.array([[2, 0, 1], [9, 1, 4]])
arr_2 = np.array([[3, 8, 8], [5, 2, 0]])
arr_3 = np.stack([arr_1, arr_2], axis=2)
print(arr_3)
print("")


"""5 Reshape + Concatenate """
array_1 = np.array([1, 4, 8])
array_2 = np.array([[8, 6, 4],
[1, 8, 0]])
array_1 = array_1.reshape((1,3))
array_3 = np.concatenate((array_1, array_2))
print(array_3)
print("")


"""6 dtype """
float_array = np.array([0.1, 0.9, 0.7])
print(float_array.dtype)
print("") 


"""7 Convert List to Numpy array """
int_list_of_lists = [[8, 0, 6],[4, 5, 4]]
int_arr_2D = np.array(int_list_of_lists)
print(int_arr_2D)
print("")


"""8 Find the values that are greater than 7 in the numpy array """
arr =np.array([[ 5, 1, 3, 2, 4, 6],[ 5, 8, 0, 3, 1, 2],[ 3, 10, 6, 21, 15, 1]])
print(arr[arr > 7])
print("")


"""9 Where """
arr = np.array([[ 5, 1, 3, 2, 4, 6],[ 5, 8, 7, 3, 1, 2],[ 3, 10, 6, 21, 15, 1]])
# where elements equal to 3 in the original array 'arr' are replaced with an empty string.
# The structure of the line is: np.where(condition, x, y)
# - condition: The condition to check (arr == 3)
# - x: Value to be used for elements where the condition is True (in this case, an empty string "")
# - y: Value to be used for elements where the condition is False (in this case, the original value from 'arr')
arr2 = np.where(arr == 3, "", arr)
print(arr2)
print("")


"""10 Numpy Shape """
array_2d = np.array([[6, 7, 5], 
                     [5, 6, 8]])
print(array_2d.shape) # rows, columns = (2,3)
print("")


"""11  """
array_2D = np.array([[ 5,  1,  3,  2,  4,  6],
       [ 5,  8,  0,  3,  1,  2],
       [ 3, 10,  6, 21, 15,  1]])
# Use np.where() to get the indices where the values are greater than 7
# This would indicate that the values greater than 7 are located at the following indices:
# (1, 1), (1, 2), (2, 1), (2, 3), (2, 4).
print(np.where(array_2D > 7))
print("")


"""12  """
array_1 = np.array([[8, 9, 6], [6, 1, 5]])
array_2 = np.array([[4, 2, 4], [8, 4, 8]])
print(array_1 * array_2)
print("")


"""13 Numpy Cumulative Sum """
array_2D = np.array([[ 5,  1,  6,  2,  4,  6],
       [ 5,  8,  0,  2,  1,  2],
       [ 2,  9,  6, 23, 13,  1]])
print("cum sum axis = 0: ", array_2D.cumsum(axis = 0))
print("cum sum axis = 1: ", array_2D.cumsum(axis = 1))
print("cum sum no axis : ", array_2D.cumsum())
print("")


"""14 Numpy Sum """
print("mean no axis : ", array_2D.mean())
print("mean axis 0: ", array_2D.mean(axis = 0)) # vertical
print("mean axis 1: ", array_2D.mean(axis = 1)) # horizontal)
print("")


"""15 Numpy Arange """
print(np.arange(3)) # [0,1,2]
print("")


"""16 Concatenation """
# Axis = 0 vertical (columns) , axis = 1 horizontal (rows)

# (2, 3) and (4, 3):  
# Compatible for concatenation along axis 0. The resulting shape would be (6, 3).

# (5, 2) and (2, 2): VERTICAL CONCAT
# Compatible for concatenation along axis 0. Res: (7, 2)
# result = np.concatenate((arr1, arr2))

# (3, 2) and (2, 3):  
# Incompatible for concatenation along any axis. 
# Neither the number of rows nor the number of columns matches.

# (3, 3) and (3, 4):  HORIZONTAL CONCAT
# Compatible for concatenation along axis 0. The resulting shape would be (3,7)
# result2 = np.concatenate((arr3, arr4), axis=1)
print("")


"""17 Numpy Flip """
# rgb is a 3D NumPy array with shape (2, 3, 3).
rgb = np.array([[[255, 0, 0],
                [0, 0, 0],
                [0, 0, 255]],
               [[255, 0, 255],
                [255, 255, 255],
                [255, 255, 0]]])
# Using NumPy's flip function to flip the array along specified axes
# Flipping along the second dimension (axis=1) and third dimension (axis=2)
print(np.flip(rgb, axis=(1, 2)))
print("")


"""18 Filtering """
ages = np.array([21, 17, 65, 43, 29, 50, 35])
print(ages[ages > 49]) # [65, 50]
print("")


"""19 Save a array numpy array named rgb as a .npy file called rgb-array.npy - With Open np.save """
# Using the 'with' statement to open the file in binary write mode ('wb')
# This ensures proper file handling, and the file will be closed automatically after the block is executed
with open("rgb-array.npy", "wb") as f:
    # Using NumPy's save function to save the 'rgb' array to the file
    np.save(f, rgb)
print("")


"""20  Combining the two 2D arrays into a 3D array """
array_1_2D = np.array([[9, 0, 9], [9, 6, 3]])
array_2_2D = np.array([[4, 2, 6], [0, 9, 0]])
# Combining the two 2D arrays into a 3D array named 'array_3D'
array_3D = np.array([array_1_2D, array_2_2D])
print(array_3D)
print("")


"""21  Load a .npy file called rgb-array.npy into a numpy array called rgb """
# Using the 'with' statement to open the file in binary read mode ('rb')
# This ensures proper file handling, and the file will be closed automatically after the block is executed
with open("rgb-array.npy", "rb") as f:
    # Using NumPy's load function to load the array from the file
    rgb = np.load(f)
print("")


"""22 Produce a plot of the cumulative sum of the numpy array arr """
import matplotlib.pyplot as plt
arr = np.array([8, 13, 21, 34, 55, 89])
plt.plot(np.arange(6), arr.cumsum())
plt.ylabel("Cumulative Sum")
print("")


"""23 Subtract 4 from each element in the 2D numpy array """
array_2D = np.array( [ [ 5, 1, 6], [ 5, 8, 0], [ 2, 9, 6] ] )
print(array_2D - 4)
print("")


"""24 Specifying data type in creation of Numpy array """
# Creating a NumPy array named 'arr' with specified values and data type
arr = np.array([1.2, 0.0, 2.0, 3.1], dtype=np.float64)
# Displaying the data type of the array
# The 'dtype' attribute provides information about the data type of the array
print(arr.dtype)
print("")


"""25 Using Slicing to extract specific rows and columns"""
array_2D = np.array([[1, 2, 3, 4, 5, 6],
                    [0, 1, 2, 3, 5, 8],
                    [1, 3, 6, 10, 15, 21]])
# Using slicing to extract a subarray from the original array
# The syntax [:2, :2] means selecting rows up to (but not including) index 2 and columns up to (but not including) index 2
# Extracting the subarray consisting of the first two rows and first two columns
subarray = array_2D[:2, :2]
print(subarray)
print("")


"""26 Add these 2 arrays together"""
array_2D_1 = np.array([[7, 1, 3, 6],[1, 9, 6, 4]])
array_2D_2 = np.array([[4],[9]])
print(array_2D_1 + array_2D_2) # this will add [4] to [7,1,3,6] and [9] to [1,9,6,4]
print("")


"""27 Transpose with axes """
# Creating a NumPy array 'rgb' with shape (2, 3, 3)
# The array represents a 2x3 matrix where each element is a 3-element array representing an RGB color.
rgb = np.array([[[255, 0, 0], [0, 0, 0], [0, 0, 255]],
                [[255, 0, 255], [255, 255, 255], [255, 255, 0]]])
# The 'axes' parameter specifies the new order of dimensions. In this case, (1, 0, 2) means:
# - The first dimension becomes the second dimension
# - The second dimension becomes the first dimension
# - The third dimension remains in the same position
transposed_rgb = np.transpose(rgb, axes=(1, 0, 2))
print("")


"""28  """
vec_method = np.vectorize(str.capitalize)
vec_method(np.array(["chicken", "Cow", "SHEEP"]))
print("")


"""29 Concatenating the two arrays vertically together """
array1 = np.array([[5, 5, 9], 
                   [9, 9, 8]])
array2 = np.array([[6, 5, 8], 
                   [3, 3, 8]])
print(np.concatenate((array1, array2)))
print("")


"""30  Capitalizing """
vec_method = np.vectorize(str.capitalize)
input_array = np.array(["chicken", "Cow", "SHEEP"])
# Applying the vectorized method to the input array
# This will capitalize the first letter of each string in the array
result_array = vec_method(input_array)
print(result_array)
print("")


"""31 Delete a particular column of the array"""
nums = np.array([[ 5, 1, 3, 2, 4, 6],
                 [ 5, 8, 0, 3, 1, 2],
                 [ 3, 10, 6, 21, 15, 1]])
print(np.delete(array_2D, 2, axis=1))
print("")


"""32 Vectorize len - calculating the length of each element in a Numpy array """
len_vec = np.vectorize(len)
input_array = np.array(["camel", "cat", "cow"])
# Applying the vectorized len function to the input array
# This will calculate the length of each string in the array
result_array = len_vec(input_array)
print(result_array) # [5 3 3]
print("")


"""32 Slicing a numpy array """
array_2D = np.array([[1, 2, 3, 4, 5, 6],
                     [0, 1, 2, 3, 5, 8],
                     [1, 3, 6, 10, 15, 21]])
# Using slicing to extract columns from index 0 to 7 with a step of 3
print(array_2D[:, 0:7:3])
print("")


"""32 Numpy split """
rgb = np.array([[[255, 0, 0],
                 [0, 0, 0],
                 [0, 0, 255]],
                [[255, 0, 255],
                 [255, 255, 255],
                 [255, 255, 0]]])
# Using np.split to split the array along the second axis (axis=1) into three parts
arr_1, arr_2, arr_3 = np.split(rgb, 3, axis=1)
print("")


"""33 Numpy array full of zeros """
print(np.zeros((2, 4))) 
print("")


"""34 Sort vertically """
array_2D = np.array([[ 5, 1, 3, 2, 4, 6],
                     [ 5, 8, 0, 3, 1, 2],
                     [ 3, 10, 6, 21, 15, 1]])
# Sorting vertically the array
print(np.sort(array_2D, axis =0 ))
print("")


"""35 """
array_2D = np.array([[5, 1, 6, 2, 4, 6],
                     [5, 8, 0, 2, 1, 2],
                     [2, 9, 6, 23, 13, 1]])
# Summing along the first axis (rows) and keeping the dimensions
sum_arr = array_2D.sum(axis=0, keepdims=True)
# Concatenating the original array with the sum array vertically
result_array = np.concatenate((array_2D, sum_arr))
print(result_array)
print("")


"""36 Make a 2D array to 1D array """
array_2D = np.array([[3, 3, 3],
                     [7, 5, 6]])
print(array_2D.flatten())
print("")


"""37 Random array generator """
# Generate a random array of shape (1, 2) with random numbers between 0 and 1
# (1,2) is the specified shape of the array 
random_array = np.random.random((1, 2))
print(random_array)
print("")


"""38 Reshape array_1 so that it can be concatenated with array_2 """
array_1 = np.array([1, 4, 8])
array_2 = np.array([[8, 6, 4],
                    [1, 8, 0]])
# Reshape array_1 to have 3 rows and 1 column
array_1 = array_1.reshape((1, 3))
# Concatenate array_1 and array_2 vertically
result_array = np.concatenate((array_1, array_2), axis=0)
# Print the resulting concatenated array
print(result_array)
print("")


"""39 What is the correct way to return the documentation for the numpy .reshape() array method? """
# help(np.ndarray.reshape)
print("")


"""40 Reshape the array """
arr = np.array([8, 4, 2, 9, 8, 2])
arr.reshape((6, 1)) 
print("")

