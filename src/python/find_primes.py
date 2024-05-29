def find_primes(n):
    primes = []
    for i in range(2,n+1):
        prime = True
        for j in range(2, round(i**0.5)+1):
            if i % j == 0:
                prime = False
                break

        if prime:
            primes.append(i)

    return primes


if __name__=='__main__':
    print(len(find_primes(1000000)))
