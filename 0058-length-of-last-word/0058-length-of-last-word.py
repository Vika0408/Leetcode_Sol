class Solution(object):
    def lengthOfLastWord(self, s):
        if len(s) <= 10**4 and 1 <= len(s) :
            x = s.split()
            length = len(x)
            return len(x[length-1])
        """
        :type s: str
        :rtype: int
        """
        