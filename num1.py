




def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        print(arr[i])
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
            return arr


data = [12, 11, 13, 5, 6]
print("Original array:", data)
insert_sort(data)
print("Sorted array:", data)

        