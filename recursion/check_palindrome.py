def check_palindrome_string(s):
    str(s)
    return check_palindrome_sub_string(0, len(s)-1, s)

def check_palindrome_sub_string(lo,hi,s):
    if lo >= hi :
        return True
    return s[lo] == s[hi] and check_palindrome_sub_string(lo+1, hi-1, s)

def check_palindrome_number(n):
    return n == compute_palindrome_number(n,0)

def compute_palindrome_number(n1,n2):
    if(n1 == 0):
        return n2
    n2 = n2*10 + n1%10
    return compute_palindrome_number(n1//10,n2)


if __name__ == '__main__' :
    print(check_palindrome_string('racecar'))
    print(check_palindrome_number(12321))