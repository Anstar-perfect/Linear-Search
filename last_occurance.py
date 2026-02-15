def last_occur(a,n,x):
    occurances = []
    for i in range(0,n):
        if(a[i]==x):
            occurances.append(i)
    if not occurances:
        return "The element does not occur"
    else:
        return occurances[len(occurances)-1]
a = [1,2,3,6,2,3,0,3,9,2]
n = len(a)
x =2
print("The value last occures at index number:",last_occur(a,n,x))                    
