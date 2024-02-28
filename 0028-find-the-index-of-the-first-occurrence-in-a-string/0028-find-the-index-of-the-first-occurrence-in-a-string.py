class Solution(object):
    def strStr(self, haystack, needle):
        l, ln = len(needle), len(haystack)
        for i in range (0,ln) :
            if haystack[i:l]==needle :
                return i
            i+=1
            l+=1
        return -1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        