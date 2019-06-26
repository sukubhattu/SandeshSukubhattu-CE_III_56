startarr=[1,0,1,4,2,5,3,4]
endarr= [3,4,2,6,9,8,5,5]
mapped = zip(startarr, endarr)
mapped= list(mapped)
mapped.sort(key=lambda l:l[1])
print(mapped)

# this code sorts 2D list from the second element from each tuple