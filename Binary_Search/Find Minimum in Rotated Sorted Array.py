def findmin(arr):
    n= len(arr)
    start=0
    end = n-1
    if n==1:
        return arr[0]
    while start<=end:
        mid = start+(end-start)//2
        prev = (mid+n-1)%n
        next1 = (mid+1)%n
        if ((arr[mid]<arr[prev]) and (arr[mid]<arr[next1])):
            return arr[mid]
        
        elif arr[mid] > arr[end]:
            start = mid+1
            
        else:
            end = mid-1
            
            
    return -1
    
arr = [4, 5, 6, 7, 2]

print(findmin(arr))
