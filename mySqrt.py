class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while i*i <= x:
            if i*i == x:
                return i
            else:
                i += 1
                if i*i > x:
                    i -= 1
                    return i
        return x               
ans = Solution()
run = ans.mySqrt(80)
print(run)
