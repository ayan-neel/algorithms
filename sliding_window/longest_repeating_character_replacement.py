def brute(s,k):
    counter =  dict()
    maxLength = 0
    for i in range (65,91):
        counter[chr(i)] = 0
    for i in range(0,len(s)):
        for j in range (i,len(s)):
            substring = s[i:j+1] #substring second index is exclusive
            
            counter = dict.fromkeys(counter, 0)

            for char_index in range (0,len(substring)):
                counter[substring[char_index]]+=1

            maxFrequency = 0

            for value in counter.values():
                maxFrequency = max(maxFrequency,value)

            if (len(substring)-maxFrequency)<=k: ## this is the core idea, you would always want to replace remaining characters with k replacements and make the string uniform, if its greater then you won't know where the replacement should happen
                maxLength = max(maxLength,len(substring))

    return maxLength

def optimal(s,k):
    l=r=0
    counter = {chr(i):0 for i in range(65,91)}
    maxLen = 0
    while(r<len(s)):
        counter[s[r]]+=1
        maxFrequency = 0
        for value in counter.values():
            if value> maxFrequency:
                maxFrequency = value
        if(r-l+1-maxFrequency<=k): #business logic as we say it!
            maxLen = max(maxLen, r-l+1)
        else:
            counter[s[l]]-=1
            l+=1
        r+=1
    return maxLen
    


if __name__ == '__main__':
    print(brute('ABBD',1))
    print(optimal('ABBD',1))     
            

