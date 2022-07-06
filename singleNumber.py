class Solution:
    def singleNumber(self, nums) -> int:   
        temp = []
        for i in range(len(nums)):
            if nums[i] in temp:
                i += 1
            elif nums[i] in nums[i+1::]:
                temp.append(nums[i])
            else:
                return nums[i]
nums = [4]
ans = Solution()
run = ans.singleNumber(nums)
print(run)
