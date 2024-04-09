class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        ans = 0

        for i, ticket in enumerate(tickets):
            if i <= k:
                ans += min(ticket, tickets[k])
            else:
                ans += min(ticket, tickets[k] - 1)

        return ans
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        