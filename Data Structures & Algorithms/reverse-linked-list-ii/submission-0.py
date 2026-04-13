# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)

        node_before_reverse = dummy
        for _ in range(left - 1):
            node_before_reverse = node_before_reverse.next

        current = node_before_reverse.next
        previous = None

        for _ in range(right - left + 1):
            next_temp = current.next
            current.next = previous
            previous = current
            current = next_temp
        
        first_node_of_reversed = node_before_reverse.next
        first_node_of_reversed.next = current
        node_before_reverse.next = previous

        return dummy.next