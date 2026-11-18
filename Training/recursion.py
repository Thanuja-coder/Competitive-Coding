def r(n):
    if n>6:
        return -1
    n+=1
    result=r(n)
    print(n-1)
    return result

r(1)


