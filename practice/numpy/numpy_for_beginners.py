import math

import numpy as np

if __name__ == "__main__":
    a = np.array([1, 2, 3, 4, 5, 6])
    b = a[3:]
    b[0] = 40
    print(a)
    # [ 1  2  3 40  5  6]
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(a)
    # [[ 1  2  3  4]
    #  [ 5  6  7  8]
    #  [ 9 10 11 12]]
    print(a[1, 3])
    # 8
    print(a.ndim)
    # 2
    print(a.shape)
    # (3, 4)
    print(len(a.shape) == a.ndim)
    # True
    print(a.size)
    # 12
    print(a.size == math.prod(a.shape))
    # True
    print(a.dtype)
    # int64

    print(np.zeros(2))
    # [0. 0.]
    print(np.ones(2))
    # [1. 1.]
    # The function empty creates an array whose initial content is random and depends on the state of the memory.
    # The reason to use empty over zeros (or something similar) is speed - just make sure to fill every element afterwards!
    print(np.empty(2))
    # [1. 1.]
    print(np.arange(4))
    # [0 1 2 3]
    print(np.arange(2, 9, 2))
    # [2 4 6 8]
    print(np.linspace(0, 10, num=5))
    # [ 0.   2.5  5.   7.5 10. ]
    x = np.ones(2, dtype=np.int64)
    print(x)
    # [1 1]

    arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
    print(np.sort(arr))
    # [1 2 3 4 5 6 7 8]
    print(arr)
    # [2 1 5 3 7 4 6 8]

    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    print(np.concatenate((a, b)))
    # [1 2 3 4 5 6 7 8]

    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6]])
    print(np.concatenate((x, y), axis=0))
    # [[1 2]
    #  [3 4]
    #  [5 6]]

    array_example = np.array([[[0, 1, 2, 3],
                               [4, 5, 6, 7]],

                              [[0, 1, 2, 3],
                               [4, 5, 6, 7]],

                              [[0, 1, 2, 3],
                               [4, 5, 6, 7]]])

    print(array_example.ndim)
    # ndarray.ndim will tell you the number of axes, or dimensions, of the array.
    # 3
    print(array_example.size)
    # ndarray.size will tell you the total number of elements of the array. This is the product of the elements of the array’s shape.
    # 24
    print(array_example.shape)
    # ndarray.shape will display a tuple of integers that indicate the number of elements stored along each dimension of the array. If, for example, you have a 2-D array with 2 rows and 3 columns, the shape of your array is (2, 3).
    # (3, 2, 4)

    a = np.arange(6)
    print(a)
    # [0 1 2 3 4 5]
    b = a.reshape(3, 2)
    print(b)
    # [[0 1]
    #  [2 3]
    #  [4 5]]

    a = np.array([1, 2, 3, 4, 5, 6])
    print(a.shape)
    # (6,)
    # means it is a 1-D array
    a2 = a[np.newaxis, :]
    print(a2.shape)
    print(a2)
    # Using np.newaxis will increase the dimensions of your array by one dimension when used once.
    # (1, 6)
    # [[1 2 3 4 5 6]]

    col_vector = a[:, np.newaxis]
    print(col_vector.shape)
    print(col_vector)
    # (6, 1)
    # [[1]
    #  [2]
    #  [3]
    #  [4]
    #  [5]
    #  [6]]

    data = np.array([1, 2, 3])
    print(data[1])
    # 2
    print(data[0:2])
    # [1 2]
    print(data[1:])
    # [2 3]
    print(data[-2:])
    # [2 3]

    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(a[a < 5])
    # [1 2 3 4]
    five_up = (a >= 5)
    print(five_up)
    # [[False False False False]
    #  [ True  True  True  True]
    #  [ True  True  True  True]]
    print(type(five_up))
    # <class 'numpy.ndarray'>
    print(a[five_up])
    # [ 5  6  7  8  9 10 11 12]
    print(a[a % 2 == 0])
    # [ 2  4  6  8 10 12]
    print(a[(a > 2) & (a < 11)])
    # [ 3  4  5  6  7  8  9 10]
    five_up = (a > 5) | (a == 5)
    print(five_up)
    # [[False False False False]
    #  [ True  True  True  True]
    #  [ True  True  True  True]]
    print(np.nonzero(a < 7))
    # (array([0, 0, 0, 0, 1, 1]), array([0, 1, 2, 3, 0, 1]))
    # The first array represents the row indices where these values are found, and the second array represents the column indices where the values are found.
    a1 = np.array([[1, 1],
                   [2, 2]])
    a2 = np.array([[3, 3],
                   [4, 4]])
    print(np.vstack((a1, a2)))
    # [[1 1]
    #  [2 2]
    #  [3 3]
    #  [4 4]]
    print(np.hstack((a1, a2)))
    # [[1 1 3 3]
    #  [2 2 4 4]]
    x = np.arange(1, 25).reshape(2, 12)
    print(x)
    # [[ 1  2  3  4  5  6  7  8  9 10 11 12]
    #  [13 14 15 16 17 18 19 20 21 22 23 24]]
    print(np.hsplit(x, 3))
    # [array([[ 1,  2,  3,  4],
    #        [13, 14, 15, 16]]), array([[ 5,  6,  7,  8],
    #        [17, 18, 19, 20]]), array([[ 9, 10, 11, 12],
    #        [21, 22, 23, 24]])]

    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    arr1 = a[3:8]
    print(type(arr1))
    # <class 'numpy.ndarray'>
    arr1[0] = 19
    print(a)
    # [ 1  2  3 19  5  6  7  8  9 10]


    b = a.copy()
    b[0] = 12
    print(a)
    # [ 1  2  3 19  5  6  7  8  9 10]
    print(b)
    # [12  2  3 19  5  6  7  8  9 10]

    
