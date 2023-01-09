def binarysearch(list,n,lb,ub):
    

    
    while ub>=lb:
        mid=(lb+ub)//2
        if list[mid]==n:
            return mid
        elif  list[mid]<n:
                lb=mid+1
        else:
            ub=mid-1
    return -1
        
list=[5,6,7,9,45,66,90]
n=7 
result = binarysearch(list, n, 0, len(list)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


