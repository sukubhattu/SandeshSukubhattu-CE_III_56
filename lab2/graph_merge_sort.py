import matplotlib.pyplot as plt
import time
import random
mylist = []
numbers = []
sec = []


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
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
    return arr


for num in range(10, 100, 10):
    for i in range(0, num):
        x = random.randint(1, 100)
        mylist.append(x)
    start = time.perf_counter()
    mergeSort(mylist)
    end = time.perf_counter()
    numbers.append(num)
    sec.append(end-start)
# print(numbers)
# print(sec)
plt.xlabel("size of inputs")
plt.ylabel("time taken")
plt.title("graph for merge sort")
plt.plot(numbers, sec)
plt.show()
