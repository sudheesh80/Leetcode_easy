class Solution:
    def removeDuplicates(self, nums) -> int:
        x=0
        while x < len(nums)-1:
            if nums[x] == nums[x+1]:
                nums.pop(x)
                x -= 1
            x += 1
        return len(nums)
n = [1,1,2]
ans = Solution()
run = ans.removeDuplicates(n)
print(run)
