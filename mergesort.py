def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the elements into 2 halves
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0
        print(len(L))
        print(len(R))

        # Copy data to temporary arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array:", arr)

# [12,11,13] [5,6,7]

# L: [12] [11,13]
# R: [5] [6,7]

# ----------------------------------
# L = 12, [11,13] 
# if(arr[i] <  arr[j]){
#    arr[i] = arr[j] 
# }
# L = 



