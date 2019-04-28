import time
start = time.time()
# given that the array/list is sorted in ascending or descending order
arr = [1,2,3,4,5,6,7,8]

def BinarySearch(arr, l, r, x):
    # here l indicates the lest most index of array
    # r indicates the right most index of the array
    while l<=r:
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
print(BinarySearch(arr, 0, len(arr)-1, 9))    
print(end - start)  