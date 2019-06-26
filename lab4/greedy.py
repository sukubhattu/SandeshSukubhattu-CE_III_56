li_A=[]
li_B=[]
# li_A and li_B are the two empty list.
def iterativeActivitySelector(s,f):
    activities= len(s)
    activity_f= 0
    #first activity is always selected
    li_A.append(activity_f)
    # appendig first activity to list li_A
    for activity in range(activities):
        if s[activity]>= f[activity_f]:
            li_A.append(activity)
            activity_f = activity
    return li_A

def recursiveActivitySelector(s,f,k,n):
    m= k+1
    while m<n and s[m]<f[k] and k>=0:
        m = m+1
    if m<n:
        li_B.append(m)
        return recursiveActivitySelector(s,f,m,n)
    return li_B

s = [1,3,0,5,3,5,6,8,8,2,12]
f = [4,5,6,7,9,9,10,11,12,14,16]
#below two lines are commented because if i run test case then the it causes list to be filled
# act1=iterativeActivitySelector(s,f)
# act2 = recursiveActivitySelector(s,f,-1,len(s))
