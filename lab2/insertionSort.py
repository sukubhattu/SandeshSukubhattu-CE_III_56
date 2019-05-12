import random

mylist = []

for i in range(0, 100):
    x = random.randint(1, 10000)
    mylist.append(x)

def insertionSort(arr):
    # Traverse through index 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr


# Driver code to test above
insertionSort(mylist)
# print("Sorted array is:")
# for i in range(len(mylist)):
#     print("%d" % mylist[i])

