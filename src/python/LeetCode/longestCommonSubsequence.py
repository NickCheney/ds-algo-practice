class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        seq_arr = [[0]*n for _ in range(m)]

        seq_arr[0][0] = int(text1[0] == text2[0])

        for i in range(1,m):
            seq_arr[i][0] = max(seq_arr[i-1][0],int(text1[i]==text2[0]))

        for j in range(1,n):
            seq_arr[0][j] = max(seq_arr[0][j-1], int(text2[j]==text1[0]))

        for i in range(1, m):
            for j in range(1,n):
                seq_arr[i][j] = max(
                    seq_arr[i][j-1],
                    seq_arr[i-1][j],
                    seq_arr[i-1][j-1] + 1 if text1[i] == text2[j] else 0
                )


        return seq_arr[-1][-1]


def print_arr(arr):
    for row in arr:
        print(" ".join([str(v) for v in row]))

if __name__ == '__main__':
    sol = Solution()
    print()
    print_arr(sol.longestCommonSubsequence("bce","abcde"))
    print()
    print_arr(sol.longestCommonSubsequence("ace","abcde"))
    print()
    print_arr(sol.longestCommonSubsequence("bcd","abcde"))
    print()
    print_arr(sol.longestCommonSubsequence("abc","def"))
