class Solution(object):
    def merge(self, nums1, m, nums2, n):
        del nums1[m:]
        nums1.extend(nums2)
        nums1.sort()
        return nums1
            




nums1 = [1,2,3,0,0,0] 
m = 3
nums2 = [2,5,6]
n = 3

example = Solution()

print(example.merge(nums1, m, nums2, n))
    