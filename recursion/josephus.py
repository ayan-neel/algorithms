def josephus(n, k):
    if n == 1:
        return 0
    else:
        return (josephus(n-1,k) + k)%n # refer to notes for complete explanation.
                                        # circle gets shifted by k, modulus is required to keep our circle in bound within n
                                        # modulus is always required in case of cyclic expressions.
                                

if __name__ == '__main__':
    print(josephus(190,2))