class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x = 0
        while x < len(haystack):
            if haystack[x:len(needle)+x] == needle:
                return x
                break
            x += 1  
            if x == len(haystack):
                return -1

haystack = "hello"
needle = "ba"
ans = Solution()
run = ans.strStr(haystack,needle)
print(run)
