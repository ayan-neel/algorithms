import sys
def rope_cutting(n, a,b,c):
    if (n == 0):
        return 0
    if (n<0):
        return -sys.maxsize - 1 #large number to avoid false positives - let's say till the second last recursive call it was 999 pieces, but in the last call, n became less than 0. if we return -1, it will be 999-1 = 998 pieces which is not true. 
    return 1+ max(rope_cutting(n-a,a,b,c),rope_cutting(n-b,a,b,c), rope_cutting(n-c,a,b,c))

if __name__ == '__main__':
    print(rope_cutting(16,5,3,7)) # pass case