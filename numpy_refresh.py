# NumPy Full course - DataScience RoadMap   -- Data Analyst self learning examples

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
    print(a.shape)
    # prints the length of the array (horizontally)
    print(len(a))
    # prints the number of array dimensions
    print(a.ndim)
    # prints the type of elements in the array
    print(a.dtype)
    print("\n")

    print(b)
    print(b.ndim)
    # (x,y) - (h,v)
    print(b.shape)
    # 2 because we have 2  1D arrays
    print(len(b))
    # how many elements we have in the array
    print(b.size)
    print(b.dtype)
    print("\n")

    print(c)
    print(c.ndim)
    # (2, 2, 3) - 3 dimensions
    print(c.shape)
    # we have 2 2D arrays in the 3d array
    print(len(c))
    # 12 elements
    print(c.size)
    print(c.dtype)
    print("\n")

    # convert array into matrix
    mat = np.matrix(b)
    print(mat)
    print(type(b))
    print(type(mat))
    print("\n")

    # create an array of zeros
    zeros = np.zeros(5)
    print(zeros)
    print("\n")
    mat_1 = np.zeros((3, 3))
    print(mat_1)
    vec_1 = np.ones((3, 5))
    print(vec_1)
    print("\n")

    # np.arange(start, end, step)
    # in this case it will create a 1d array with only the odd numbers from 1 to 19
    vec_3 = np.arange(1, 20, 2)
    print(vec_3)
    print("\n")

    # np.linspace(start, stop, values) - creates evenly spaced values
    bins = np.linspace(1, 20, 10)
    print(bins)
    print("\n")

    # create an identity matrix
    i_4 = np.identity(4)
    print(i_4)
    print("\n")
    # alternative way
    i_5 = np.eye(5)
    print(i_5)
    print("\n")

    # create a full matrix
    # create a full matrix containing the element 5
    full_m = np.full((3, 3), 5)
    print(full_m)
    print("\n")

    # create a random matrix with values from 0 to 1
    r = np.random.random((2, 2))
    print(r)
    print("\n")

    # create an empty matrix
    e = np.empty((2, 5))
    print(e)
    print("\n")

    # create an array with fixed values
    arr = np.array([3, 7, 6, 8, 9, 1, 2, 3])
    print(arr)
    # we can also copy it!
    arr_copy = arr.copy()
    print(arr_copy)
    print("\n")

    """ SORTING ARRAY """
    ba = np.array([8, 7, 5, 4, 3])
    print(ba)
    # # now lets sort it! - Use it as a function np.sort()
    print(np.sort(ba))
    # you can also store it
    ab = np.sort(ba)
    print(ab)
    print("\n")

    # alternative way 2
    # When using it as the method of class - these will sort them in place and will return None - return original array
    arr2 = np.array([9, 11, 5, 15, 3])
    print(arr2)
    np.ndarray.sort(arr2)
    print(arr2)
    print("\n")

    # alternative way 3
    arr3 = np.array([4, 9, 5, 0, 3])
    print(arr3)
    arr3.sort()
    print(arr3)
    print('\n')

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
    print(b[1, 2])
    # prints the first 1D array
    print(b[0, ])
    print('\n')

    """ Array Slicing """
    # get the 3rd element from every 1D array
    print(b[:, 2])
    print("\n")

    """ Boolean Indexing """
    # prints a 1D array with elements only greater than 1
    print(b[b > 1])
    print("\n")

    """ Reshaping an Array """
    # transposing the array
    b_trans = b.T
    print(b_trans)
    print(b.shape)
    print(b_trans.shape)
    print("\n")

    # flattening the array - From 2D array to 1D array
    print(b)
    b_flat = b.ravel()
    print(b_flat)
    print("\n")
    print(c)
    c_flat = c.ravel()
    print(c_flat)
    print("\n")

    # lets reshape c_flat!
    c_flat2 = c_flat.reshape(4, 3)
    print(c_flat2)
    print("\n")

    """ Inserting Elements into the array """
    d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print(d)
    # flattens the array and adds in the 4th (3) position  a 10
    d = np.insert(d, 3, 10)
    print(d)
    print("\n")

    e = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print(e)
    e = np.insert(e, 2, [10, 20, 30])
    print(e)
    print("\n")
    f = e.reshape(5, 3)
    print(f)
    print("\n")

    """ Deleting Elements from array """
    # deletes the 2nd element (1)
    g = np.delete(f, 1)
    # f = np.delete(f, [1]) - same thing
    print(g)
    g = np.delete(g, 1)
    print(g)
    print("\n")

    """ Combining Arrays """
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])

    # axis = 1 vertically
    arrh = np.concatenate((arr1, arr2), axis=0)
    print(arrh)
    print("\n")

    # Rows x Columns
    arr3 = np.array([[1, 2], [3, 4]])
    arr4 = np.array([[5, 6], [7, 8]])
    arrV = np.concatenate((arr3, arr4), axis=1)
    # from  2 x 2,2     to   1 x  2, 4
    print(arrV)
    print("\n")

    # from  2 x 2,2     to   1 x  4, 2
    arrH = np.concatenate((arr3, arr4), axis=0)
    print(arrH)
    print("\n")

    # alternative way Vertically:
    arrv2 = np.vstack((arr3, arr4))
    print(arrv2)
    print("\n")

    # alternative way Horizontally:
    arrh2 = np.hstack((arr3, arr4))
    print(arrh2)
    print("\n")

    """ Splitting Arrays """
    # horizontal split of array
    a1 = np.hsplit(arrh2, 2)
    print(a1)
    # vertical split of array
    a2 = np.vsplit(arrh2, 2)
    print(a2)
    print("\n")

    a = arrh2.ravel()
    print(a)







if __name__ == '__main__':
    main()
