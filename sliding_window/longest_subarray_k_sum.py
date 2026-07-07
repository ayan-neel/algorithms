def brute_force (k,arr):
    maxLen = 0
    for i in range(0,len(arr)):
        sum = 0
        for j in range(i,len(arr)): #range includes lower bound and excludes upper bound
            sum = sum+arr[j]
            if(sum<k):
                maxLen = max(maxLen,j-i+1)
            else:
                break
    return maxLen

def slide (k,arr):
    r=l=0
    sum=0
    maxLen = 0
    while (r<len(arr) and l<=r):  #boiler plate
        checksum = sum +arr[r] #problem statement basis
        if checksum>=k and l ==r: #edge case #also problem statement basis
            l+=1
            r+=1
            continue
        if checksum < k: #problem statement basis
            sum = checksum
            maxLen = max(maxLen,r-l+1) #problem statement basis
            r+=1 #boiler plate
        else:
            sum = sum - arr[l] #problem statement basis
            l+=1 #boiler plate
    return maxLen

if __name__ =="__main__":
    arr = [-1,-1,-1,-1,-1]
    k = 10
    print(brute_force(k,arr))
    print(slide(k,arr))

