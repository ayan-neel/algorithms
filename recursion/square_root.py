class SquareRoot:
    def root(self, n):
        return self.helper(0,n,n)
    
    def helper(self,low,high,n):
        if(low<=high):
            mid = low + (high-low)//2
            if(mid*mid<=n and (mid+1)*(mid+1) >n): #base case
                return mid
            elif (mid*mid<n):
                return self.helper(mid+1,high,n)
            else:
                return self.helper(low,mid-1,n)
        else:
            return low
                 
if __name__ == '__main__':
    sqroot = SquareRoot()
    print(sqroot.root(179))