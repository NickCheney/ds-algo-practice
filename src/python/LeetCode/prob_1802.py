class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        arr = n*[0]
        while sum(arr) <= maxSum:
            res = arr[:]
            arr[index] += 1
            for i in range(index-1,-1,-1):
                if abs(arr[i]-arr[i+1]) > 1:
                    arr[i]+=1
            for i in range(index+1,n):
                if abs(arr[i]-arr[i-1]) > 1:
                    arr[i]+=1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxValue(4,0,4))
