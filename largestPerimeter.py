class Solution:
    def largestPerimeter(self, nums) -> int:
        nums.sort(reverse=True)  
        for i in range(len(nums)):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
                break
            elif i+3 == len(nums):
                return 0
                break
nums = [3,2,3,4,5,7,3,2,8,5,9,8,9,9,10,11,11,11] 
x = Solution() 
print(x.largestPerimeter(nums))
