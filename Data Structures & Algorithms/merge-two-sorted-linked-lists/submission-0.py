# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        fakeNode = ListNode()
        tempHead = fakeNode
        while list1 and list2:
            #print('currently list1:',list1.val,'and list2:',list2.val)
            if list1.val < list2.val:
                fakeNode.next = list1
                list1 = list1.next
            else:
                fakeNode.next = list2
                list2 = list2.next
            fakeNode = fakeNode.next

        fakeNode.next = list1 or list2
        
        return tempHead.next