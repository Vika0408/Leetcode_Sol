class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        j = -1
        lastSeen = {}
        for i, c in enumerate(s):
            j = max(j, lastSeen.get(c, -1))
            ans = max(ans, i - j)
            lastSeen[c] = i
        return ans
        """
        :type s: str
        :rtype: int
        """
        