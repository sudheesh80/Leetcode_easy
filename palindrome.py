class Solution(object):
    def isPalindrome(self, x):
        return False if x < 0 else x == int(str(x)[::-1])
tan = Solution()
x = int(input(print("Enter the Roamn number to convert to Intiger:")))
run = tan.isPalindrome(x)
print(run)
