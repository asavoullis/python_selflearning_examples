# NumPy Full course - DataScience RoadMap   -- Data Analyst self learning examples

# NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and
# matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
# Written in: Python and C


import numpy as np
import sys


def main():

    """ Array Creation """
    # 1d array
    a = np.array([1, 2, 3, 4])
    # 2d array
    b = np.array([[1, 2, 3], [1, 2, 3]])
    # 3d array
    c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

    print(a)
    # prints the shape of the array - in this case it will be a 1D (4,) array
    # "shape" is an attribute of the ndarray, rather than a method, so it's not callable (doesn't need "()" at the end)
    print(a.shape)
    # prints the length of the array (horizontally)
    print(len(a))
    # prints the number of array dimensions
    print(a.ndim)
    # prints the type of elements in the array
    print(a.dtype, '\n')

    print(b)
    print(b.ndim)
    # (x,y) - (h,v)
    print(b.shape)
    # 2 because we have 2  1D arrays
    print(len(b), "\n")
    # how many elements we have in the array
    print(b.size)
    print(b.dtype, "\n")

    print(c)
    print(c.ndim)
    # (2, 2, 3) - 3 dimensions
    print(c.shape)
    # we have 2 2D arrays in the 3d array
    print(len(c), "\n")
    # 12 elements
    print(c.size)
    print(c.dtype, "\n")

    # convert array into matrix
    mat = np.matrix(b)
    print(mat, "\n")
    print(type(b))
    print(type(mat), "\n")

    # create an array of zeros
    zeros = np.zeros(5)
    print(zeros, "\n")

    mat_1 = np.zeros((3, 3))
    print(mat_1)
    vec_1 = np.ones((3, 5))
    print(vec_1, "\n")

    # np.arange(start, end, step)
    # in this case it will create a 1d array with only the odd numbers from 1 to 19
    vec_3 = np.arange(1, 20, 2)
    print(vec_3, "\n")

    # np.linspace(start, stop, values) - creates evenly spaced values
    bins = np.linspace(1, 20, 10)
    print(bins, "\n")

    # create an identity matrix
    i_4 = np.identity(4)
    print(i_4, "\n")
    # alternative way
    i_5 = np.eye(5)
    print(i_5, "\n")

    # create a full matrix
    # create a full matrix containing the element 5
    full_m = np.full((3, 3), 5)
    print(full_m, "\n")

    # create a random matrix with values from 0 to 1
    r = np.random.random((2, 2))
    print(r, "\n")

    # create an empty matrix
    e = np.empty((2, 5))
    print(e, "\n")

    # range vs np.arange
    print(range(10))

    abc = list(range(10))
    print(abc, "\n")

    # array_rng = np.arange(start = 0, stop = 30, step = 2.5, dtype = np.float32) or np.int32
    array_rng = np.arange(10)
    print(array_rng)

    """ Be Careful when copying arrays """
    # create an array with fixed values
    arr = np.array([3, 7, 6, 8, 9, 1, 2, 3])
    print(arr)
    # we can also copy it!
    arr_copy = arr.copy()
    print(arr_copy, "\n")

    a3 = np.array([1, 2, 3])
    print(a3, "\n ")
    # b3 points to a3 so if you change a value of b3 a3 will also change
    b3 = a3
    b3[0] = 100
    # changing b3's first element also changes a3's first element because of b3 = a3 they point to each other
    print(a3, "\n ")
    print(b3, "\n ")

    # BETTER USE COPY to copy an array!
    a4 = a3.copy()
    print(a4, "\n ")


    """ Sorting Array """
    ba = np.array([8, 7, 5, 4, 3])
    print(ba)
    # # now lets sort it! - Use it as a function np.sort()
    print(np.sort(ba))
    # you can also store it
    ab = np.sort(ba)
    print(ab, "\n")

    # alternative way 2
    # When using it as the method of class - these will sort them in place and will return None - return original array
    arr2 = np.array([9, 11, 5, 15, 3])
    print(arr2)
    np.ndarray.sort(arr2)
    print(arr2, "\n")

    # alternative way 3
    arr3 = np.array([4, 9, 5, 0, 3])
    print(arr3)
    arr3.sort()
    print(arr3, '\n')

    """ Assigning Values in Array """
    print(arr3)
    # sets the first (0) element of the array equal to 2
    arr3[0] = 2
    print(arr3, "\n")

    array_a = np.array([[1, 2, 3], [4, 5, 6]])
    list_a = [8, 7, 8]
    # sets the first 1D array to the values of list_a
    array_a[0] = list_a
    print(array_a)
    print(type(array_a[0]), "\n")


    """ Elementwise Properties """
    array_a = np.array([7, 8, 9])
    array_b = np.array([[1, 2, 3], [4, 5, 6]])
    # multiplies all elements inside array_c by 2
    array_c = array_a * 2
    print(array_c, "\n")
    # adds the value of 2 to each element of the array_a
    print(array_a + 2, "\n")

    # We multiply each individual element of array_a by its corresponding element in the second row of array_b.
    array_d = array_a * array_b[1]
    print(array_d, "\n")

    list_a = [1, 2, 3]
    list_a = list_a + [2]
    print(list_a, "\n")

    print(array_b - array_a)
    # The order of the elements matters for elementwise subtraction, division, as well as other operations.

    """
    arr = np.array([3, 7, 6, 8, 9, 1, 2, 3])
    a = np.array([1, 2, 3, 4])
    b = np.array([[1, 2, 3], [1, 2, 3]])
    c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    """

    """ Array Indexing """
    # displays the 5th element - starting from 0
    print(arr[4])
    # prints the 3rd element of the 2nd 1D array
    print(b[1, 2], "\n")
    # prints the first 1D array
    print(b[0, ])
    # prints last value
    print(arr[-1], '\n')


    """ Array Slicing """
    print(b, "\n")
    # slicing = interval indexing

    # get the 3rd element from every row
    print(b[:, 2], "\n")

    # get the first row only from array
    print(b[0, :], "\n")

    # assigning all the elements of the first position at the 1st (0) position vertically to 9
    b[:, 0] = 9
    print(b, "\n")

    matrix_A = np.array([[1, 2, 3], [4, 5, 6]])
    # prints from first until second 0->1 but 1 excluded
    print(matrix_A[:1], "\n")


    """ Stepwise Slicing """
    matrix_B = np.array([[1, 1, 1, 2, 0], [3, 6, 6, 7, 4], [4, 5, 3, 8, 0]])
    # prints entire array
    print(matrix_B[::, ::])
    # we take the first and the 3rd row
    print(matrix_B[::2, ::], "\n")
    # we take every other column
    print(matrix_B[::, ::2], "\n")
    # print Every other value of every other row, starting from the first
    print(matrix_B[::2, ::2], "\n")

    # getting a little more fancy [startindex:endindex:stepsize]
    print(b[0, 1:-2: 2])
    print(matrix_B[::-2, ::2], "\n")
    print(matrix_B[-1::-2, ::2], '\n')


    """ Conditional Slicing"""
    matrix_C = np.array([[1, 1, 1, 2, 0], [3, 6, 6, 7, 4], [4, 5, 3, 8, 0]])
    # slice the first column
    print(matrix_C[:, 0], "\n")
    # outputs an array with boolean elements True or False depending opn the condition
    print(matrix_C[:, 0] > 2, "\n")

    print(matrix_C[:, 0] > 2, "\n")
    print(matrix_C[:, :] > 2, "\n")

    print(matrix_C[matrix_C[:, :] > 2], '\n')
    print(matrix_C[matrix_C[:, :] == 2], "\n")
    print(matrix_C[matrix_C[:, :] >= 2], "\n")
    print(matrix_C[matrix_C[:, :] != 2], "\n")
    print(matrix_C[matrix_C[:, :] % 2 == 0], "\n")
    print(matrix_C[(matrix_C[:, :] % 2 == 0) & (matrix_C[:, :] <= 4)], "\n")


    """ Boolean Indexing """
    # prints a 1D array with elements only greater than 1
    print(b[b > 1], "\n")


    """ Types of Data Supported By Numpy """
    # Defining all the values as floats (decimals).
    array_a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float16)
    print(array_a, "\n")

    # Defining all the values as complex numbers.
    array_a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.complex64)
    print(array_a, "\n")

    # array_a = np.array([[1,2,0],[4,5,6]], dtype = np.bool)
    # array_a = np.array([[10,2,3],[4,5,6]], dtype = np.str)


    """ Characteristics of Numpy Functions """
    array_a = np.array([1, 2, 3])
    array_b = np.array([[1], [2]])
    matrix_C = np.array([[1, 2, 3], [4, 5, 6]])

    # We can add up values, even though the arrays don't have matching shapes.
    add_a_c = np.add(array_a, matrix_C)
    print(add_a_c)
    add_b_c = np.add(array_b, matrix_C)
    print(add_b_c, "\n")


    """ Type Casting """
    # we can also change the type of the values in the arrays while adding
    array_e = np.add(array_b, matrix_C, dtype=np.float64)
    print(array_e, "\n")


    """ Reshaping an Array """
    # transposing the array
    b_trans = b.T
    print(b_trans)
    print(b.shape, "\n")
    print(b_trans.shape, "\n")

    # flattening the array - From 2D array to 1D array
    print(b)
    b_flat = b.ravel()
    print(b_flat,"\n")
    print(c, "\n")
    c_flat = c.ravel()
    print(c_flat, "\n")

    # lets reshape c_flat!
    c_flat2 = c_flat.reshape(4, 3)
    print(c_flat2, "\n")


    """ Inserting Elements into the array """
    d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print(d)
    # flattens the array and adds in the 4th (3) position  a 10
    d = np.insert(d, 3, 10)
    print(d, "\n")

    e = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print(e, "\n")
    e = np.insert(e, 2, [10, 20, 30])
    print(e, "\n")
    f = e.reshape(5, 3)
    print(f, "\n")


    """ Deleting Elements from array """
    # deletes the 2nd element (1)
    g = np.delete(f, 1)
    # f = np.delete(f, [1]) - same thing
    print(g)
    g = np.delete(g, 1)
    print(g, "\n")


    """ Combining Arrays """
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])

    # axis = 1 vertically
    arrh = np.concatenate((arr1, arr2), axis=0)
    print(arrh, "\n")

    # Rows x Columns
    arr3 = np.array([[1, 2], [3, 4]])
    arr4 = np.array([[5, 6], [7, 8]])
    arrV = np.concatenate((arr3, arr4), axis=1)
    # from  2 x 2,2     to   1 x  2, 4
    print(arrV, "\n")

    # from  2 x 2,2     to   1 x  4, 2
    arrH = np.concatenate((arr3, arr4), axis=0)
    print(arrH, "\n")

    # alternative way Vertically:
    arrv2 = np.vstack((arr3, arr4))
    print(arrv2, "\n")

    # alternative way Horizontally:
    arrh2 = np.hstack((arr3, arr4))
    print(arrh2, "\n")


    """ Splitting Arrays """
    # horizontal split of array
    a1 = np.hsplit(arrh2, 2)
    print(a1)
    # vertical split of array
    a2 = np.vsplit(arrh2, 2)
    print(a2, "\n")

    a = arrh2.ravel()
    print(a, "\n")


    """ Specific Value Extraction from Arrays """
    print(a.min())
    print(a.max(), "\n")
    print(a.sum(), "\n")

    # np.cumsum - displays array with sum up to that element
    print(np.cumsum(a))
    print(np.std(a), "\n")
    print(np.median(a))

    print(np.mean(a), "\n")
    print(a.mean(), "\n")


    """ Arithmetic Operations """
    arr3 = np.array([[1, 2], [3, 4]])
    arr4 = np.array([[5, 6], [7, 8]])
    arr5 = np.add(arr3, arr4)
    print(arr5)

    print(np.multiply(arr3, arr4), "\n")
    print(np.subtract(arr3, arr4), "\n")

    print(np.divide(arr3, arr4), "\n")
    print(np.exp(arr4), "\n")


    """ Running over an Axis of an Array """
    array_a = np.array([1, 2, 3])
    array_b = np.array([[1], [2]])
    matrix_C = np.array([[1, 2, 3], [4, 5, 6]])

    # Axis = 0 runs the function over every column.
    mean_arr = np.mean(matrix_C, axis=0)
    print(mean_arr, "\n")
    mean_arr2 = np.mean(matrix_C, axis=1)
    print(mean_arr2, "\n")


    """ Numpy DataTypes """
    print(array_b.shape)
    # We can use indexing to get a specific part of the output tuple.
    print(array_b.shape[0], "\n")
    # array_b.shape[1]


    """Dimensions and the Squeeze Function"""
    matrix_D = np.array([[1, 1, 1, 2, 0], [3, 6, 6, 7, 4], [4, 5, 3, 8, 0]])
    print(print(matrix_D[0, 0]))
    print(type(matrix_D[0, 0]))
    print(matrix_D[0, 0:1], "\n")

    print(matrix_D[0:1, 0:1])
    print(type(matrix_D[0:1, 0:1]), '\n')

    # Same value stored in 3 different ways -> 0-D, 1-D and 2-D array
    print(matrix_D[0, 0].shape)
    print(matrix_D[0, 0:1].shape, "\n")

    print(matrix_D[0:1, 0:1].shape, "\n")

    # [[1]]
    print(matrix_D[0:1, 0:1])
    # 1
    print(matrix_D[0:1, 0:1].squeeze(), '\n')

    print(np.squeeze(matrix_D[0:1, 0:1]))
    ## All excess dimensions are lost and our outputs are aligned.
    print(matrix_D[0, 0].squeeze().shape)
    print(matrix_D[0, 0:1].squeeze().shape, "\n")

    print(matrix_D[0:1, 0:1].squeeze().shape, "\n")


    """ Using Like function to create an Array """
    matrix_A = np.array([[1, 0, 9, 2, 2], [3, 23, 4, 5, 1], [0, 2, 3, 4, 1]])

    array_empty_like = np.empty_like(matrix_A)
    print(array_empty_like)

    array_0s_like = np.zeros_like(matrix_A)
    print(array_0s_like, "\n")


    """ NAN equivalent funcitons """
    matrix_A = np.array([[1, 0, 0, 3, 1], [3, 6, 6, 2, 9], [4, 5, 3, 8, 0]])
    # same as we don't have nan values
    print(np.nanmean(matrix_A))
    print(np.mean(matrix_A), "\n")

    matrix_B = np.array([[1, 0, 0, 3, 1], [3, 6, np.nan, 2, 9], [4, 5, 3, 8, 0]])
    print(np.nanmean(matrix_B))
    print(np.mean(matrix_B), "\n")

    print(np.nanquantile(matrix_B, 0.7))
    # print(np.nanvar(matrix_B,"\n"))

    z1 = np.cov(matrix_A)
    print(z1)
    z2 = np.corrcoef(matrix_A)
    print(z2, "\n")

    """ MORE FUNCTIONS """

    # np.percentile()
    # Returns a specific percentile of a given set
    # Requires a second input – the percentile
    # A percentile is a value that is greater than the corresponding % of the dataset
    q3 = np.quantile(matrix_A, 0.70)
    print(q3)
    # we get the median
    q2 = np.percentile(matrix_A, 50)
    print(q2, '\n')

    b1 = np.percentile(matrix_A, 70, interpolation="midpoint")
    print(b1)
    b2 = np.percentile(matrix_A, 70, interpolation ="higher")
    print(b2, "\n")

    print(matrix_A)
    # Returns the difference between the highest and the lowest values within an array
    print(np.ptp(matrix_A), "\n")
    # axis = 0  columns , axis = 1 row
    print(np.ptp(matrix_A, axis=0), "\n")


    """ Importing Files in Python using Numpy """
    # np.loadtxt() vs np.genfromtxt()
    #
    # Load: implies the data is ready to be directly imported and used
    # Genfromtxt: indicates that the function creates the data from the text file.
    # Generating requires constructing the array as we go through the file. This allows us only to take certain
    # rows or columns, as well as split the input into multiple variables.

    """
    LOADTXT:
    lending_co_data_numeric_NAN2 = np.loadtxt("Lending-Company-Numeric-Data-NAN.csv",
                                          delimiter = ';',
                                          dtype = np.str)
    
    GENFROMTXT:
    lending_co_data_numeric_NAN = np.genfromtxt("Lending-Company-Numeric-Data-NAN.csv",
                                            delimiter = ';',
                                            usecols = (0,1,5)) 
    """


    """ Saving File using Numpy """
    # stores the data in a special file extension called .npy
    # creates a “file-name.npy” in the same directory (folder)
    # This npy is a special type of text file native to numpy
    # np.save(“filename here”, dataset_variable)

    """
    lending_co = np.genfromtxt("Lending-Company-Saving.csv", 
                           delimiter = ',', 
                           dtype = np.str)
    np.save("Lending-Company-Saving", lending_co)
    lending_data_save = np.load("Lending-Company-Saving.npy")
    np.array_equal(lending_data_save, lending_co)

    
    np.savetxt("Lending-Company-Saving.txt", #set format .txt
           lending_co, 
           fmt = '%s', #s = strings , c for chracters , d for integers
           delimiter = ',')

    np.savez("Lending-Company-Saving", lending_co, lending_data_save)
    lending_data_savez = np.load('Lending-Company-Saving.npz')
    print(lending_data_savez)
    """


if __name__ == '__main__':
    main()
