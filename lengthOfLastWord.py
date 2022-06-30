class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    
ans = Solution()
run = ans.lengthOfLastWord("How are you doing")
print(run)
