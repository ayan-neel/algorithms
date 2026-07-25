def minSubArrayLen(target, nums):
        l = 0
        r = 0
        maxLength = 10**9 + 1 
        minimumLength = maxLength
        sum = 0
        while(r<len(nums)):
            tokenSum = sum + nums[r]
            if(tokenSum < target):
                sum = tokenSum
            else:
                sum = tokenSum
                while(sum>=target):
                    minimumLength = min(minimumLength,r-l+1)
                    sum -= nums[l]
                    l+=1
            r+=1

        return 0 if minimumLength == maxLength else minimumLength

if __name__ == "__main__":
     target = 7
     nums = [7,1,1]
     print(minSubArrayLen(target,nums))
