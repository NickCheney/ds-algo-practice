from itertools import combinations
import time
from random import randint
"""
Hiring Drive

You are looking to hire frontend and backend developers for a 
project that requires exactly N frontend developers and exactly M 
backend developers. You receive applications from (N+M) 
candidates.

Conditions
- Every dev can work on either the frontend or the backend 
but not on both.

- The cost of each developer can be different. The cost of the
ith developer is as follows:
    - Frontend: F(i) dollars.
    - Backend:  B(i) dollars.

Task 

Print the minimum amount that it will cost the company to run this
project.
"""
def timeit(fx):
    def run_fx(*args, **kwargs):
        t1 = time.time()
        res = fx(*args, **kwargs)
        print(f"Ran {fx.__name__} in {time.time()-t1:.2f}s")
        return res
    return run_fx

@timeit
def min_amount_brute_force(N,M,F,B):
    # Iterate over all possibilites
    # combinations will 
    min_amount = float('inf')
    f_combs = set(combinations(range(len(F)), N))
    while len(f_combs) > 0:
        f_ndxs = set(f_combs.pop())
        # print(F)
        # print(f_ndxs)
        f_curr_amt = sum([f for i, f in enumerate(F) if i in f_ndxs])
        # print(f_curr_amt)
        b_cands = [i for i in range(len(B)) if i not in f_ndxs]
        b_combs = set(combinations(b_cands, M))
        while len(b_combs) > 0:
            b_ndxs = set(b_combs.pop())
            # print(B)
            # print(b_ndxs)
            b_curr_amt = sum([b for i, b in enumerate(B) if i in b_ndxs])
            # print(b_curr_amt)
            if f_curr_amt + b_curr_amt < min_amount:
                # print(f"New min amount: {f_curr_amt + b_curr_amt}")
                min_amount = f_curr_amt + b_curr_amt

    return min_amount

@timeit
def min_amount(N,M,F,B):
    cost_diff = [(f-B[i],i) for i, f in enumerate(F)]
    cost_diff.sort(key=lambda x: x[0])

    min_cost = 0
    for i in range(M+N):
        if i < N:
            min_cost += F[cost_diff[i][1]]
        else:
            min_cost += B[cost_diff[i][1]]

    return min_cost


if __name__ == '__main__':
    print("Case 1")
    N = 1
    M = 2
    F = [3,4,7]
    B = [1,5,6]
    print(f"N={N}")
    print(f"M={M}")
    print(f"F={F}")
    print(f"B={B}")
    min_amt=min_amount_brute_force(N,M,F,B)
    print(f"Final amt: {min_amt}")
    opt_min_amt = min_amount(N,M,F,B)
    print(f"Opt final amt: {opt_min_amt}")

    print("\nCase 2")
    N = 1
    M = 2
    F = [1,1,1]
    B = [1,1,1]
    print(f"N={N}")
    print(f"M={M}")
    print(f"F={F}")
    print(f"B={B}")
    min_amt=min_amount_brute_force(N,M,F,B)
    print(f"Final amt: {min_amt}")
    opt_min_amt = min_amount(N,M,F,B)
    print(f"Opt final amt: {opt_min_amt}")

    print("\nCase 3")
    N = 2
    M = 3
    F = [0,1,2,3,4]
    B = [10,10,10000,10000,10000]
    print(f"N={N}")
    print(f"M={M}")
    print(f"F={F}")
    print(f"B={B}")
    min_amt=min_amount_brute_force(N,M,F,B)
    print(f"Final amt: {min_amt}")
    opt_min_amt = min_amount(N,M,F,B)
    print(f"Opt final amt: {opt_min_amt}")

    print("\nCase 4")
    apps = 30
    N = randint(1,apps-1)
    M = apps-N
    F = [randint(0,apps*10) for i in range(apps)]
    B = [randint(0,apps*10) for i in range(apps)]
    print(f"N={N}")
    print(f"M={M}")
    print(f"F={F}")
    print(f"B={B}")
    min_amt=min_amount_brute_force(N,M,F,B)
    print(f"Final amt: {min_amt}")
    opt_min_amt = min_amount(N,M,F,B)
    print(f"Opt final amt: {opt_min_amt}")