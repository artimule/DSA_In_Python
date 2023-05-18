def search(arr,x):
    start=0
    end=len(arr)-1
    if(arr[0]>arr[1]): #desending
        while start<=end:
            mid = start+(end-start)//2
            if(x==arr[mid]):
                return mid
            elif (x<arr[mid]):
                start = mid+1
            else:
                end = mid-1
        return -1
    
    if (arr[0]<arr[1]):
        while start<=end:
            mid = start+(end-start)//2
            if(x==arr[mid]):
                return mid
            elif(x<arr[mid]):
                end = mid-1
            else:
                start = mid+1
                
        return -1
    
arr = [9,8,5,4,1]
x=8
print(search(arr,x))        
