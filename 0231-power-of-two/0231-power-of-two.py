class Solution(object):
    def isPowerOfTwo(self, n) :
        return False if n < 0 else bin(n).count('1') == 1
        """
        :type n: int
        :rtype: bool
        """
        