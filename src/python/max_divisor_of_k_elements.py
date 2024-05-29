# Python 3 program to find subsequence  
# of size k with maximum possible GCD. 
import math 
  
import time
from random import randint

def timeit(fx):
    def run_fx(*args, **kwargs):
        t1 = time.time()
        res = fx(*args, **kwargs)
        print(f"Ran {fx.__name__} in {time.time()-t1:.2f}s")
        return res
    return run_fx

# function to find GCD of sub sequence  
# of size k with max GCD in the array 
@timeit
def findMaxGCD(arr, n, k): 
    # Time complexity of O(n*root(n))
    # Computing highest element 
    high = max(arr) 
  
    # Array to store the count of  
    # divisors i.e. Potential GCDs 
    divisors = [0] * (high + 1) 
  
    # Iterating over every element 
    for i in range(n) : 
  
        # Calculating all the divisors 
        for j in range(1, int(math.sqrt(arr[i])) + 1): 
  
            # Divisor found 
            if (arr[i] % j == 0) : 
  
                # Incrementing count for divisor 
                divisors[j] += 1
  
                # Element/divisor is also a divisor 
                # Checking if both divisors are 
                # not same 
                if (j != arr[i] // j): 
                    divisors[arr[i] // j] += 1
  
    # Checking the highest potential GCD 
    for i in range(high, 0, -1): 
  
        # If this divisor can divide at least k 
        # numbers, it is a GCD of at least one 
        # sub sequence of size k 
        if (divisors[i] >= k): 
            return i 
        

@timeit
def findMaxGCDUnoptimized(arr, n, k):
    # Time complexity of O(N^2)
    largest = 1
    for n in range(2,max(arr)+1):
        count = 0
        for num in arr:
            if num % n == 0:
                count += 1
            if count >= k:
                largest = n
                break

    return largest
  
# Driver code 
if __name__ == "__main__": 
    print("Case 1")
    # Array in which sub sequence with size 
    # k with max GCD is to be found 
    arr = [ 1, 2, 4, 8, 8, 12 ] 
    k = 3
  
    n = len(arr) 
    print(findMaxGCD(arr, n, k)) 
    print(findMaxGCDUnoptimized(arr, n, k))

    print("Case 2")
    n = 5000
    arr = [randint(1,n) for _ in range(n)]
    k = randint(1,n)
    print(findMaxGCD(arr, n, k))
    print(findMaxGCDUnoptimized(arr, n, k))

  
# This code is contributed by ita_c 
# https://www.geeksforgeeks.org/subsequence-of-size-k-with-maximum-possible-gcd/