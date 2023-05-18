    def searchInSorted(self,arr, N, X):
        #Your code here
        start = 0
        end = N-1
        while start<=end:
            mid = start+ (end-start)//2
            if arr[mid] == X:
                return 1
            elif arr[mid]>X:
                start = mid+1
            else:
                end = mid-1
        return -1
