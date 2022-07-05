class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        nums1.extend(nums2)
        nums1.sort()
        for i in range(n):
            nums1.remove(0)
        return nums1
nums1 = [1,2,3,0,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
ans = Solution()
run = ans.merge(nums1, m, nums2, n)
print(run)
