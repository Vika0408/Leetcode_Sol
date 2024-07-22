class Solution(object):
    def sortPeople(self, names, heights):
        return [height for _, height in
            sorted([(height, name) for name, height in zip(names, heights)], reverse=True)]
            
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
    