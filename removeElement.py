class Solution:
    def removeElement(self, nums, val) -> int:
        x =0 
        while (x<= len(nums)-1):
            if nums[x] == val:
                nums.pop(x)
                x -= 1
                nums.append("_")
            x += 1
n = [3,2,2,3]
tan = Solution()
run = tan.removeElement(n, 3)
print(run)
