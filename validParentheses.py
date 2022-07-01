class Solution:
    # def isValid(self, s: str) -> bool:
    def isValid(self, s):
        stack = []
        lib = {"(":")","[":"]","{":"}"}
        for char in s:
            if char in lib:
                stack.append(lib[char])
            else:
                if not stack or stack.pop() != char:
                    return False
        return not len(stack)
  
s = "(()[]{})"
ans = Solution()
run = ans.isValid(s)
print(run)
