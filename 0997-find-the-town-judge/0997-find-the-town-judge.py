class Solution(object):
    def findJudge(self, n, trust):
        count = [0] * (n + 1)

        for a, b in trust:
            count[a] -= 1
            count[b] += 1

        for i in range(1, n + 1):
            if count[i] == n - 1:
              return i

        return -1
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        