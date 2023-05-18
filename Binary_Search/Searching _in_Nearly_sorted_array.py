def binarysearch(arr,low,high,x):
    while(low<=high):
        mid = low+(high-low)//2
        if arr[mid]==x:
            return mid
        if mid>low and arr[mid-1]==x:
            return mid-1
        if mid< high and arr[mid+1]==x:
            return mid+1
        if arr[mid]>x:
            return binarysearch(arr, low, mid-2,x)
        return binarysearch(arr,mid+2,high,x)
    
arr = [3, 2, 10, 4, 40]
low=0
high=len(arr)-1
x=4
print(binarysearch(arr,low,high,x))
