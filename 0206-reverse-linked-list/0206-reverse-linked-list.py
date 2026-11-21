# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        
        if head == None:
            return None

        current = head.next #pointer to next node, or next node entirely
        current_head = head #current node entirely


        while current is not None: #while pointer to next node != None
            temp = current.next #temporarily store the value of next next node, or pointer to next next node.
            current.next = current_head #next next pointer actually just points back to previous node


            current_head = current #
            current = temp #move forward one

        head.next = None

        return current_head