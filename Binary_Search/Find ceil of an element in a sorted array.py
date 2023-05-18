def ceil(arr,x):
    start =0
    end = len(arr)-1
    res =-1
    while start<=end:
        mid = start+(end-start)//2
        if(x==arr[mid]):
            return arr[mid]
        
        elif x<arr[mid]:
            res = arr[mid]
            end = mid-1
        else:
            start=mid+1
    return res
arr =[1,2,3,4,8,10,10,12,19]
x=5
print(ceil(arr,x))
