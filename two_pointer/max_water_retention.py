#Leetcode 11

def compute(arr):
    l=0
    r=len(arr)-1
    maxArea = 0
    while(l<r):
        maxArea = max(maxArea,calcArea(l,r,arr))
        if (arr[l]==arr[r]):
            l+=1
            r-=1
            continue
        else: #move one of the pointer based on which side is a bottleneck
            if(arr[l]<arr[r]):
                l+=1
            else:              
                r-=1
    return maxArea

def calcArea(l,r,arr):
    return (r-l) * (min(arr[l],arr[r]))

if __name__ == "__main__":
    arr = [1,8,6,2,5,4,8,3,7] 
    print(compute(arr))


    


