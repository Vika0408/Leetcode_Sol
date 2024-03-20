# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        nodeBeforeA = list1
        for i in range(a-1) :
            nodeBeforeA = nodeBeforeA.next
        
        nodeB = nodeBeforeA.next
        for i in range(b-a) :
            nodeB = nodeB.next
        
        nodeBeforeA.next = list2
        lastnodeinlist2 = list2
        
        while lastnodeinlist2.next :
            lastnodeinlist2 = lastnodeinlist2.next
            
        lastnodeinlist2.next = nodeB.next
        nodeB.next = None
        
        return list1
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        