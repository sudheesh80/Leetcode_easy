class Solution:
    def climbStairs(self, n: int) -> int:
        count = 1
        a,b = 1,1
        for i in range(n-1):
            count = a+b
            b = a
            a = count
        return count       
ans = Solution()
run = ans.climbStairs(1)
print(run)
