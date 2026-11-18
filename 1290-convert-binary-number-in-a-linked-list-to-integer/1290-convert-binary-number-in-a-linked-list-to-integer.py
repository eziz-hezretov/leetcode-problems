# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        
        seen = []

        current = head

        while current is not None:
            seen.append(current.val)

            current = current.next

        binary = "".join(map(str, seen))

        number = int(binary, 2)

        return number