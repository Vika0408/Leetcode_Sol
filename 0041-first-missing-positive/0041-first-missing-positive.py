class Solution(object):
    def firstMissingPositive(self, nums):
        nums.sort()
        if 1 not in nums:
            return 1
        a = nums.index(1)
        for i in range(a+1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                return nums[i-1] + 1
            if i == len(nums)-1:
                return nums[i] + 1
        return 2