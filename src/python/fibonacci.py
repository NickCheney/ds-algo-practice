from time_it import time_it

"""
Naive Approach

Time complexity:
T(n<2) = c1
T(n) = c2 + T(n-1) + T(n-2)
= c2 + c2 + T(n-2) + T(n-3) + c2 + T(n-3) + T(n-4)
= 3c2 + 1T(n-2) + 2T(n-3) + 1T(n-4)

If we had set n=3 here, then we'd have <= 8 (or 2^3) recursive calls

= 3c2 + c2 + T(n-3) + T(n-4) + 2(c2 + T(n-4) + T(n-5)) + c2 + T(n-5) + T(n-6)
= 7c2 + 1T(n-3) + 3T(n-4) + 3T(n-5) + 1T(n-6)

If we had set n=4 here, then we'd have <=16 (or 2^4) recursive calls

T(2) = c2 + T(1) + T(0) = c2 + 2c1
T(3) = c2 + T(2) + T(1) = 2c2 + 3c1
T(4) = c2 + T(3) + T(2) = 4c2 + 5c1
T(5) = c2 + T(4) + T(3) = 7c2 + 8c1

Notice here the number of constants is always less than 2^n but more than 2^n/2

So our upper bound time complexity is O(2^n).

For space complexity, recall that for recursive functions we only need to consider
the maximum depth of the call stack, which will be n. So O(n).
"""
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
@time_it
def fib_wrapper(n):
    return fib(n)


"""
DP Approach

Here, we build a dictionary of fib(n) values as we compute them for the first time,
so no fib(n) will have to be manually computed. This will lead to a time complexity 
of O(n), with one computation for each sequence step. The space complexity will
remain at O(n).
"""  
def fib_dp(n, fibtab={0:0, 1:1}):
    if n in fibtab:
        return fibtab[n]
    else:
        fibtab[n] = fib_dp(n-1, fibtab) + fib_dp(n-2, fibtab)
        return fibtab[n]

@time_it
def fib_dp_wrapper(n):
    return fib_dp(n)

if __name__ == '__main__':
    print(fib_wrapper(35))
    print(fib_dp_wrapper(35))