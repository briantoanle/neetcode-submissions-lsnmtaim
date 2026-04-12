# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # make a temp head node
        # point the head to the new temp head
        # then start reversing

        prev = None
        
        temp = head
        while temp:
            nodetotheright = temp.next
            temp.next = prev
            prev = temp
            temp = nodetotheright
        return prev

            
