arr = [1, 0, 5, 6, 9, 10, 19, 16]
def LinearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

print(LinearSearch(arr, 11))