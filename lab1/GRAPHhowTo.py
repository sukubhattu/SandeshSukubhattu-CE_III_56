import time
import random
import matplotlib.pyplot as plt

# mylist = []
# size = []
# sec = []

# # given that the array/list is sorted in ascending or descending order


# def BinarySearch(array, item):
#     firstIndex = 0
#     lastIndex = len(array)-1
#     found = False
#     while firstIndex <= lastIndex and not found:
#         index = int((firstIndex+lastIndex)/2)
#         if array[index] == num:
#             found = True
#             return index
#         else:
#             if num < array[index]:
#                 lastIndex = index-1
#             else:
#                 firstIndex = index+1


# dict_ = {}
# size = 1000
# list = random.sample(range(10000), 10000)
# for i in range(int(len(list)/size)):
#     list = list[size:]
#     startime = time.clock()
#     BinarySearch(list, 5)
#     time_elapsed = time.clock()-startime
#     dict_[len(list)] = time_elapsed
# plt.plot(dict_.keys(), dict_.values())

""" OR"""

mylist = []
size = []
sec = []

# given that the array/list is sorted in ascending or descending order


def binarySearch(arr, l, r, x):

    # Check base case
    if r >= l:

        mid = l + (r - l)//2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1



for num in range(1000, 10000, 1000):
    for i in range(0, num):
        x = random.randint(1, 100)
        mylist.append(x)
    mylist.sort()
    start = time.perf_counter()
    binarySearch(mylist, 0, len(mylist)-1, mylist[5])
    end = time.perf_counter()
    size.append(num)
    sec.append(end-start)
plt.plot(size, sec)
plt.show()


