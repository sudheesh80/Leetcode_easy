class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        values = {}
        x = enumerate(nums)
        for idx,value in enumerate(nums):
            if target-value in values:
                return [values[target-value],idx]
            else:
                values[value] = idx
tan = Solution()
run = tan.twoSum(nums=[2,4,7,5],target=9)
print(run)
