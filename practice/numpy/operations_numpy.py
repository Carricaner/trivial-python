import numpy as np

if __name__ == "__main__":
    data = np.array([1, 2])
    ones = np.ones(2, dtype=int)
    print(data + ones)
    # [2 3]
    print(data - ones)
    # [0 1]
    print(data * data)
    # [1 4]
    print(data / data)
    # [1. 1.]

    a = np.array([1, 2, 3, 4])
    print(a.sum())
    # 10
    b = np.array([[1, 1], [2, 2]])
    print(b.sum(axis=0))
    # [3 3]
    print(b.sum(axis=1))
    # [2 4]

    data = np.array([1.0, 2.0])
    print(data * 1.6)
    # [1.6 3.2]

    print(data.max())
    # 2.0
    print(data.min())
    # 1.0
    print(data.sum())
    # 3.0

    a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
                  [0.54627315, 0.05093587, 0.40067661, 0.55645993],
                  [0.12697628, 0.82485143, 0.26590556, 0.56917101]])
    print(a.sum())
    # 4.8595784
    print(a.min())
    # 0.05093587
    print(a.min(axis=0))
    # [0.12697628 0.05093587 0.26590556 0.5510652 ]

    data = np.array([[1, 2], [3, 4], [5, 6]])
    print(data[0, 1])
    # 2
    print(data[1:3])
    # [[3 4]
    #  [5 6]]
    print(data[0:2, 0])
    # [1 3]
    print(data.max())
    # 6
    print(data.min())
    # 1
    print(data.sum())
    # 21
    print(data.max(axis=0))
    # [5 6]
    print(data.max(axis=1))
    # [2 4 6]

    data = np.array([[1, 2], [3, 4]])
    ones = np.array([[1, 1], [1, 1]])
    print(data + ones)
    # [[2 3]
    #  [4 5]]
    data = np.array([[1, 2], [3, 4], [5, 6]])
    ones_row = np.array([[1, 1]])
    print(data + ones_row)
    #  [[2 3]
    #  [4 5]
    #  [6 7]]

    print(np.ones(3))
    # [1. 1. 1.]
    print(np.zeros(3))
    # [0. 0. 0.]
    rng = np.random.default_rng()
    print(rng.random(3))
    # [0.01129317 0.64570382 0.10750858]

    print(np.ones((3, 2)))
    # [[1. 1.]
    #  [1. 1.]
    #  [1. 1.]]
    print(np.zeros((3, 2)))
    # [[0. 0.]
    #  [0. 0.]
    #  [0. 0.]]
    print(rng.random((3, 2)))
    # [[0.98098058 0.73192854]
    #  [0.10642189 0.48817391]
    #  [0.55319335 0.43614705]]
    print(rng.integers(5, size=(2, 4)))
    # [[2 4 0 4]
    #  [2 1 1 3]]

    a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
    print(np.unique(a))
    # [11 12 13 14 15 16 17 18 19 20]
    unique_values, indices_list = np.unique(a, return_index=True)
    print(indices_list)
    # [ 0  2  3  4  5  6  7 12 13 14]
    unique_values, occurrence_count = np.unique(a, return_counts=True)
    print(occurrence_count)
    # [3 2 2 2 1 1 1 1 1 1]

    a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
    print(np.unique(a_2d))
    # [ 1  2  3  4  5  6  7  8  9 10 11 12]
    # 2-D array will ne flattened
    print(np.unique(a_2d, axis=0))
    # [[ 1  2  3  4]
    #  [ 5  6  7  8]
    #  [ 9 10 11 12]]
    unique_rows, indices, occurrence_count = np.unique(
        a_2d, axis=0, return_counts=True, return_index=True)
    print(indices)
    # [0 1 2]
    print(occurrence_count)
    # [2 1 1]

    data = np.array([[1, 2], [3, 4], [5, 6]])
    print(data.reshape(2, 3))
    # [[1 2 3]
    #  [4 5 6]]
    print(data.reshape(3, 2))
    # [[1 2]
    #  [3 4]
    #  [5 6]]
    arr = np.arange(6).reshape((2, 3))
    print(arr)
    # [[0 1 2]
    #  [3 4 5]]
    print(arr.transpose())
    # [[0 3]
    #  [1 4]
    #  [2 5]]
    print(arr.T)
    # [[0 3]
    #  [1 4]
    #  [2 5]]

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    reversed_arr = np.flip(arr)
    print(reversed_arr)
    # [8 7 6 5 4 3 2 1]

    arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    reversed_arr = np.flip(arr_2d)
    print(reversed_arr)
    # reversed_arr = np.flip(arr_2d)
    reversed_arr_rows = np.flip(arr_2d, axis=0)
    print(reversed_arr_rows)
    # [[ 9 10 11 12]
    #  [ 5  6  7  8]
    #  [ 1  2  3  4]]
    reversed_arr_columns = np.flip(arr_2d, axis=1)
    print(reversed_arr_columns)
    # [[ 4  3  2  1]
    #  [ 8  7  6  5]
    #  [12 11 10  9]]
    arr_2d[1] = np.flip(arr_2d[1])
    print(arr_2d)
    # [[ 1  2  3  4]
    #  [ 8  7  6  5]
    #  [ 9 10 11 12]]
    arr_2d[:, 1] = np.flip(arr_2d[:, 1])
    print(arr_2d)
    # [[ 1 10  3  4]
    #  [ 8  7  6  5]
    #  [ 9  2 11 12]]

    x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(x.flatten())
    # [ 1  2  3  4  5  6  7  8  9 10 11 12]
    a1 = x.flatten()
    a1[0] = 99
    print(x)  # Original array
    # [[ 1  2  3  4]
    #  [ 5  6  7  8]
    #  [ 9 10 11 12]]
    print(a1)
    # [99  2  3  4  5  6  7  8  9 10 11 12]
    # When you use flatten, changes to your new array won’t change the parent array.
    a2 = x.ravel()
    a2[0] = 98
    print(x)  # Original array
    # [[98  2  3  4]
    #  [ 5  6  7  8]
    #  [ 9 10 11 12]]
    print(a2)  # New array
    # [98  2  3  4  5  6  7  8  9 10 11 12]
    # But when you use ravel, the changes you make to the new array will affect the parent array.

    # docstr
    help(max)
    # Help on built-in function max in module builtins:
    #
    # max(...)
    #     max(iterable, *[, default=obj, key=func]) -> value
    #     max(arg1, arg2, *args, *[, key=func]) -> value
    #
    #     With a single iterable argument, return its biggest item. The
    #     default keyword-only argument specifies an object to return if
    #     the provided iterable is empty.
    #     With two or more arguments, return the largest argument.
    a = np.array([1, 2, 3, 4, 5, 6])




