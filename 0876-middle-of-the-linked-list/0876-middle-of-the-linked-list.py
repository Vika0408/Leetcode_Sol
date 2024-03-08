class Solution:
    def middleNode(self, head) :
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        middle = length // 2
        i = 0
        while i < middle:
            head = head.next
            i += 1
        return head