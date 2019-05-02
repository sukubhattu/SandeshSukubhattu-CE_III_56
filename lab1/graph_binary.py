import time
import random
import matplotlib.pyplot as plt

mylist = []
size = []
sec = []

# given that the array/list is sorted in ascending or descending order

for num in range(10, 10000, 100):
    for i in range(0, num):
        x = random.randint(1, 100)
        mylist.append(x)

    item = random.choice(mylist)
    mylist.sort()    
    start = time.time()
    def BinarySearch(arr, l, r, item):
        # here l indicates the lest most index of array
        # r indicates the right most index of the array
        while l <= r:
            mid = l + (r-l)//2
            # mid should be always equal to integer so (r-1)//2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                l = mid+1
            else:
                r = mid-1
        return -1
    end = time.time()
    size.append(num)
    sec.append(end-start)

print(size)
print(sec)
plt.plot(size, sec)


