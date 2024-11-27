# Function to calculate gcd using Euclid's algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Extended Euclidean Algorithm to find x and y such that gcd(a, b) = ax + by
def extended_gcd(a, b):
    # Base case: if b is 0, then gcd is a, and x=1, y=0
    if b == 0:
        return a, 1, 0
    else:
        gcd_value, x1, y1 = extended_gcd(b, a % b)
        # Update x and y using the recursive results
        x = y1
        y = x1 - (a // b) * y1
        return gcd_value, x, y

# Function to compare recursive calls and running time
import time

# Function to measure the time and recursive calls of Euclid's algorithm
def measure_time_and_calls(func, a, b):
    count = 0
    
    def wrapper(a, b):
        nonlocal count
        count += 1
        return func(a, b)
    
    start_time = time.time()
    result = wrapper(a, b)
    end_time = time.time()
    
    return result, count, end_time - start_time

# Example usage
a, b = 30, 12

# GCD using Euclid's algorithm
gcd_result = gcd(a, b)
print(f"GCD of {a} and {b} using Euclid's algorithm: {gcd_result}")

# Extended GCD to find x and y
gcd_extended, x, y = extended_gcd(a, b)
print(f"Extended GCD: gcd({a}, {b}) = {gcd_extended} = {a} * {x} + {b} * {y}")

# Measure time and count recursive calls for Euclid's algorithm
result, recursive_calls, exec_time = measure_time_and_calls(gcd, a, b)
print(f"Euclid's Algorithm: GCD = {result}, Recursive Calls = {recursive_calls}, Time = {exec_time:.6f} seconds")

# Measure time and count recursive calls for Extended Euclid's algorithm
def extended_gcd_wrapper(a, b):
    return extended_gcd(a, b)

result_extended, recursive_calls_extended, exec_time_extended = measure_time_and_calls(extended_gcd_wrapper, a, b)
 
print(f"Extended Euclid's Algorithm: GCD = {result_extended}, Recursive Calls = {recursive_calls_extended}, Time = {exec_time_extended:.6f} seconds")
