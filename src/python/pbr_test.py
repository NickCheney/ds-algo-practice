def recurse_wrapper():
    d = {}
    recurse(5,d)
    print(d)

def recurse(n, d):
    if n == 0:
        d[n] = n

    else:
        recurse(n-1, d)
        d[n] = n

if __name__ == '__main__':
    recurse_wrapper()
    
