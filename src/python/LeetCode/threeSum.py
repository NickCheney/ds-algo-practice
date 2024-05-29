from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        else:
            mid = len(nums)//2
            res = []
            res += self.threeSum(nums[:mid])
            res += self.threeSum(nums[mid:])

            #1 in left, 2 in right
            twoSums = {}
            for i in range(mid,len(nums)):
                for j in range(i+1,len(nums)):
                    two = [nums[i],nums[j]]
                    if sum(two) in twoSums:
                        twoSums[sum(two)].append(two)
                    else:
                        twoSums[sum(two)]=[two]

            for val in nums[:mid]:
                if -val in twoSums:
                    for twoSum in twoSums[-val]:
                        res.append(twoSum+[val])

            #2 in left, 1 in right
            twoSums = {}
            for i in range(mid):
                for j in range(i+1,mid):
                    two = [nums[i],nums[j]]
                    if sum(two) in twoSums:
                        twoSums[sum(two)].append(two)
                    else:
                        twoSums[sum(two)]=[two]

            for val in nums[mid:]:
                if -val in twoSums:
                    for twoSum in twoSums[-val]:
                        res.append(twoSum+[val])

            return [(threeSum) for threeSum in res]
        

if __name__ == '__main__':
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(sol.threeSum(nums))