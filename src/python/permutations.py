# Heap's Algorithm
def generate(k, A):
    if k == 1:
        print("".join(A))
    else:
        generate(k-1,A)

        for i in range(k-1):
            if k % 2 == 0:
                A[i], A[k-1] = A[k-1], A[i]
            else:
                A[0], A[k-1] = A[k-1], A[0]
            generate(k-1,A)


# My algorithm (Backwards Heap's)
def permutate(k, A):
    if k == 1:
        print("".join(A))
    else:
        # We want to call generate() with k-1 a total of k times
        generate(k-1, A)

        for i in range(k-1):
            if k % 2 == 0:
                # even length, swap 1st element with dynamic other (or won't get all elements in 1st position before cycle finishes)
                A[0], A[k - 1 - i] = A[k - 1 - i], A[0]
            else:
                # odd length, can safely swap 1st and last element every time
                A[0], A[k-1] = A[k-1], A[0]
            generate(k-1, A)

# Brute force backtracking
def backtrack(A,curr=''):
    if len(curr)==len(A):
        print(curr)
    else:
        for char in A:
            if char not in curr:
                backtrack(A,curr+char)


if __name__ == '__main__':
    ar = list("123")
    k = len(ar)
    generate(k,ar)
    print()
    permutate(k,ar)
    print()
    backtrack(ar)
