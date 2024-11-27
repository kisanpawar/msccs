def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def print_array(arr):
    print(" ".join(map(str, arr)))

# Driver code
arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array: ", end="")
print_array(arr)

bubble_sort(arr)

print("Sorted array: ", end="")
print_array(arr)
