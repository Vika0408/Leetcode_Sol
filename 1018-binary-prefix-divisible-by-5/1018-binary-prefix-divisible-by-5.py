class Solution(object):
    def prefixesDivBy5(self, nums):
        l = len(nums)
        res = []
        bi = ''
        for i in range(0,l) :
            bi = bi+str(nums[i])
            dec = int(bi,2)
            if (dec%5) == 0 :
                res.append(True)
            else :
                res.append(False)
            i+=1
        return res
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        