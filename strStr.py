class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if haystack.find(needle) != -1:
            return haystack.index(needle)
        else:
            return -1
        
        # Below is another way of doing it
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

