def reverseArray(arr):
    # code here
    n = len(arr)
    if n == 1:
        return arr
    for i in range(0, n//2): # swap ith element with n-ith element (1 and last, 2 and last -1)
        arr[i] = arr[i] + arr[n-i-1]
        arr[n-i-1] = arr[i] - arr[n-i-1]
        arr[i] = arr[i] - arr[n-i-1]
    return arr