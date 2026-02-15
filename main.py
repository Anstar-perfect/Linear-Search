def search(arr,n,x):
    for i in range(0,n):
        if (arr[i]==x):
            return i
    return -1

arr = [1,40,28,284,102,13,12]
x = 12
n=len(arr)

result = search(arr,n,x)
if result==-1:
    print('The element is not present')
else:
    print('The element is present at index',result)
