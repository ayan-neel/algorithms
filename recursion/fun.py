def fun1(n):
    if n == 0:
        return
    fun1(n-1)
    print(n)
    fun1(n-1)

def fun2(n):
    if n == 0:
        return
    print(n)
    fun2(n-1)
    print(n)

def fun3(n):
    if n <=1:
        return 0
    else:
        return 1 + fun3(n/2)

def fun4(n): #binary representation of a number
    if n == 0:
        return
    fun4(n//2)
    print(n%2)


if __name__ == '__main__':
    print(fun3(16))
    print(fun4(13))
