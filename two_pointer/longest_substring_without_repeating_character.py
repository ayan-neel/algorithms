def compute (s):
    l=0
    r=1
    maxLen = 1
    while(r<len(s)):
        count=1
        while(r<len(s) and(s[l]!=s[r] or s[r]!=s[r-1])): #this approach fails, because we don't have info on the consecutive repeating characters.
            count+=1
            r+=1
        l=r-1
        maxLen = max(maxLen,count)
    
    return maxLen

def compute_correct(s):
    if not s:
        return 0
    tracker = set()
    l = 0
    r = 1
    tracker.add(s[l])
    maxLen = 1
    while(r<len(s)):
        if s[r] not in tracker:
            tracker.add(s[r])
            r+=1
            continue
        else:
            maxLen = max(maxLen,len(tracker))
            while s[r] in tracker: #shrink the substring until the duplicate is removed. Because the substring will not be valid as long as the duplicate is part of it anyway
                tracker.remove(s[l])
                l+=1
            tracker.add(s[r])
            r+=1
    return max(maxLen,len(tracker)) ## required for a completely non repeating character string.

## optimisation, map with indices.
#If you use a Dictionary instead of a Set, you can store { character: index }. When you hit a duplicate, you can instantly teleport l to the correct position in a single step, eliminating the inner loop entirely.

if __name__ == "__main__":
    print(compute_correct('baac'))



            

        
        
