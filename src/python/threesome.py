class Solution:
    def __init__(self):
        return
    def threeSum(self, nums):
        res = []
        if len(nums) < 3:
            return res
        nums.sort()
        for i in range(len(nums) - 2):
            print(i)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while True:
                print((j,k))
                if j >= k:
                    break
                elif j > i + 1 and nums[j] == nums[j-1]:
                    j+=1
                    continue
                elif k < len(nums) - 1 and nums[k] == nums[k+1]:
                    k-=1
                    continue
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                elif sum3 > 0:
                    k-=1
                else:
                    j+=1
        return res

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    sol = Solution()
    print(sol.threeSum(nums))
