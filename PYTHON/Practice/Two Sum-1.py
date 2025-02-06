class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for n in range(i + 1, len(nums)):
                if (nums[i] + nums[n]) == target:
                    return n, i
                

example = Solution()

print(example.twoSum([3, 3], 6))


