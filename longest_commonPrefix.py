class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs1 = ["flower","flow","flight"]
        strs = ["dog","racecar","car"]
        short_strs = min(strs,key=len)
        i=0
        while short_strs and i < len(strs):
            if not strs[i].startswith(short_strs):
                short_strs = short_strs[:-1]
            else:
                i += 1
        return short_strs
tan = Solution()
run = tan.longestCommonPrefix(str)
print(run)

