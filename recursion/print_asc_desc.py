def printNto1(n):
    if n ==0:
        return
    print(n)
    printNto1(n-1)

def print1toN(n):
    if n == 0:
        return
    print1toN(n-1)
    print(n)

if __name__ == "__main__":
    printNto1(5)
    print1toN(5)