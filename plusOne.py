class Solution:
    def plusOne(self, digits):
        new = []
        x = int(("".join(str(e) for e in nums))) + 1
        x = str(x)
        print(x)
        for i in x:
            new.append(i)
        print(new)

nums = [9]
ans = Solution()
run = ans.plusOne(nums)
print(run)
