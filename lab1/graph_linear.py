import time
import random
import matplotlib.pyplot as plt

mylist = []
size = []
sec = []
for num in range(10, 10000, 100):
    for i in range(0,num):
        x = random.randint(1,100)
        mylist.append(x)

    item = random.choice(mylist)
    start = time.time()
    def LinearSearch(arr, item):
        for i in range(len(arr)):
            if arr[i] == item:
                return i
        return -1
    end = time.time()

    size.append(num)
    sec.append(end-start)
print(size)
print(sec)
# np_size = np.array(size)
# np_sec = np.array(sec)
plt.plot(size, sec)
