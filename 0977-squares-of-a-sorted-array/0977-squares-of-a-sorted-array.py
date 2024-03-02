class Solution(object):
    def sortedSquares(self, nums):
        res=[]
        for i in nums :
            res.append(i**2)
        res.sort()
        return res