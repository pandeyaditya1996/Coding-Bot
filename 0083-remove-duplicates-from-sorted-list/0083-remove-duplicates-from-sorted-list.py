# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        curr = head
        while(curr and curr.next):
            a = curr
            while(a.next and a.next.val==a.val):
                a = a.next
            curr.next = a.next
            curr = curr.next

        return head