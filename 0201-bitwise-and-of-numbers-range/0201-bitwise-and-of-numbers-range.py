class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        return self.rangeBitwiseAnd(left >> 1, right >> 1) << 1 if left < right else left
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        