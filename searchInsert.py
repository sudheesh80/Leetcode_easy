import numpy as np
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for idx, num in enumerate(nums):
            if (num >= target):
                return idx
        if target > nums[-1]:
            return nums.index(nums[-1])+1
nums = [1,3,5,6]
target = 7
ans = Solution()
run = ans.searchInsert(nums, target)
print(run)
