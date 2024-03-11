class Solution(object):
    def intersection(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        ans = []
        count = collections.Counter(nums1)

        for num in nums2:
            if count[num] > 0:
                ans.append(num)
                count[num] -= 1
        
        ans = list(set(ans))

        return ans
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        