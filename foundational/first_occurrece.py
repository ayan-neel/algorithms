def firstSearch(self, arr, k):
    l = 0
    r = len(arr) - 1
    while(l<=r):
        mid = l+(r - l //2)
        if( k == arr[mid]):
            while(k == arr[mid]): #shift left until the prev index of match.
                mid-=1
            return mid+1
        if(k<arr[mid]):
            r = mid-1
        else:
            l = mid+1
    return -1
    