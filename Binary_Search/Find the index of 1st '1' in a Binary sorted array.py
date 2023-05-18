def firstIndex(arr,n):
    start =0
    end = n-1
    while start<=end:
        mid = start+(end-start)//2
        if(arr[mid]==1):
            if(arr[mid-1]==1):
                end = mid-1
            else:
                return mid
        else:
            if(arr[mid]==0):
                start = mid+1
        return -1
    
arr = [0,0,0,0,0,1,1,1,1,1,1]
n=len(arr)
print(firstIndex(arr,n))
