class Solution(object):
    def countStudents(self, students, sandwiches):
        count = collections.Counter(students)

        for i, sandwich in enumerate(sandwiches):
            if count[sandwich] == 0:
                return len(sandwiches) - i
            count[sandwich] -= 1

        return 0

        
            
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        