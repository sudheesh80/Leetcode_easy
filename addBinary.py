class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = bin(int(a, 2) + int(b,2))
        return sum[2::]        
a = "100110"
b = "110101"
ans = Solution()
run = ans.addBinary(a,b)
print(run)
