import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr,"\n")

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d,"\n")

zeros = np.zeros((3, 4))  # 3 rows, 4 columns
print(zeros,"\n")

ones = np.ones((2, 3))  # 2 rows, 3 columns
print(ones,"\n")

range_array = np.arange(0, 10, 2)  # Start at 0, end before 10, step by 2
print(range_array,"\n")

linspace_array = np.linspace(0, 1, 5)  # 5 equally spaced points between 0 and 1
print(linspace_array,"\n")

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = arr1 + arr2
print(result,"\n")

result = arr1 * arr2
print(result,"\n")

#dot product
dot_product = np.dot(arr1, arr2)
print(dot_product,"\n")

#scalar multiplication
scaled = arr1 * 2
print(scaled,"\n")

#indexing and slicing
print(arr[1],"\n")  # Access the second element, indexing
print(arr[1:4])  # Access elements from index 1 to 3, slicing
print(arr[arr > 2])  # Elements greater than 2, boolean Indexing

#sum, min, max
print(np.sum(arr))
print(np.min(arr))
print(np.max(arr),"\n")

#mean, median, standard deviation
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr),"\n")

#Random Values
random_values = np.random.rand(3, 3)  # 3x3 array with random values
print(random_values,"\n")
#Random Integers
random_integers = np.random.randint(1, 10, (2, 2))  # Random integers between 1 and 9
print(random_integers,"\n")
#Random Normal Distribution
random_normal = np.random.randn(5)  # 5 random numbers from a normal distribution
print(random_normal)

#shape attribute returns a tuple representing the dimensions of the array ie rows and columns
#size attribute returns the total number of elements in the array
#ndim attribute returns the number of dimensions (axes) of the array
print(arr_2d.shape, arr_2d.size, arr_2d.ndim)


