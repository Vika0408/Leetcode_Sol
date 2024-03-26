class Solution(object):
    def countAndSay(self, n):
        ans = '1'

        for _ in range(n - 1):
            nxt = ''
            i = 0
            while i < len(ans):
                count = 1
                while i + 1 < len(ans) and ans[i] == ans[i + 1]:
                    count += 1
                    i += 1
                nxt += str(count) + ans[i]
                i += 1
            ans = nxt

        return ans
                
        """
        :type n: int
        :rtype: str
        """
        