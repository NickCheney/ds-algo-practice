from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while True:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif left >= right:
                return -1
            #check if left sorted
            elif nums[mid] >= nums[left]:
                if nums[mid] >= target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid+1]<= target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
