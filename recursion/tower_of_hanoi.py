def solve (n,a,b,c): #(just towers A,B,C)
    if n == 0:
        return
    solve(n-1,a,c,b)  # (source, destination, auxiliary) # first move from source to 'auxiliary' using destination as pivot 
    print(f'move disc {n} from {a} to {b}') 
    solve(n-1,c,b,a) # from aux to destination using source as pivot

if __name__ == '__main__':
    solve(2,'A','B','C')