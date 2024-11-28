from functools import reduce

# Example 1: Using map to multiply by 2
def multiply_by_2(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
print("Using map to multiply by 2:", list(map(multiply_by_2, numbers)))

# Example 2: Using filter to get even numbers
def is_even(x):
    return x % 2 == 0

print("Using filter to get even numbers:", list(filter(is_even, numbers)))

# Example 3: Using reduce to calculate the product of all numbers
def multiply(x, y):
    return x * y

print("Using reduce to multiply all numbers:", reduce(multiply, numbers))





from functools import reduce

# 1. Operations on Tuples
numbers_tuple = (1, 2, 3, 4, 5)

# map
result_map = tuple(map(lambda x: x * 2, numbers_tuple))
print("Mapped tuple (multiply by 2):", result_map)

# filter
result_filter = tuple(filter(lambda x: x % 2 == 0, numbers_tuple))
print("Filtered tuple (even numbers):", result_filter)

# reduce
result_reduce = reduce(lambda x, y: x + y, numbers_tuple)
print("Reduced tuple (sum):", result_reduce)

# 2. Operations on Frozen Sets
numbers_frozenset = frozenset([1, 2, 3, 4, 5])

# map
result_map_fs = frozenset(map(lambda x: x * 3, numbers_frozenset))
print("Mapped frozenset (multiply by 3):", result_map_fs)

# filter
result_filter_fs = frozenset(filter(lambda x: x <= 3, numbers_frozenset))
print("Filtered frozenset (<= 3):", result_filter_fs)

# reduce
result_reduce_fs = reduce(lambda x, y: x * y, numbers_frozenset)
print("Reduced frozenset (product):", result_reduce_fs)
