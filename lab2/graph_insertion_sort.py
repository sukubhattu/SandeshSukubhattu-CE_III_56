import matplotlib.pyplot as plt 
import time
import random
mylist =[]
numbers = []
sec = []
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


for num in range(10, 100, 10):
    for i in range(0, num):
        x = random.randint(1, 100)
        mylist.append(x)
    start = time.perf_counter()
    insertionSort(mylist)
    end = time.perf_counter()
    numbers.append(num)
    sec.append(end-start)
print(numbers)
print(sec)
plt.xlabel("size of inputs")
plt.ylabel("time taken")
plt.title("graph for insertion sort")
plt.plot(numbers,sec)
plt.show()
