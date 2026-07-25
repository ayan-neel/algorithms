def deprecated_solve(n): #critical bug
    i2 = 1
    i3 = 1
    i5 = 1
    for i in range(1,n):
        nextUgly = min(2*i2,3*i3,5*i5)
        if(nextUgly%2==0):
            i2+=1
        if(nextUgly%3==0):
            i3+=1
        if(nextUgly%5==0):
            i5+=1
        i+=1
    return nextUgly
"""
Hint :
Take a look at what i2, i3, and i5 represent. 
They aren't meant to hold the raw multiplier numbers (like $1, 2, 3 \dots 7$).
Instead, they are pointers (indexes) that refer to previously generated ugly numbers stored in your array.
When calculating candidates for the next ugly number, you should be multiplying $2$, $3$, or $5$ by the ugly number at that index, not by the index/counter itself:
"""
def solve(n):
    ugly =[1]
    i2=i3=i5=0
    for i in range(1,n):
        nextUgly = min(2*ugly[i2],3*ugly[i3],5*ugly[i5])
        ugly.append(nextUgly)
        if(nextUgly%2==0):
            i2+=1
        if(nextUgly%3==0):
            i3+=1
        if(nextUgly%5==0):
            i5+=1
    return ugly[n-1]


if __name__ == '__m ain__':
    print(solve(11))