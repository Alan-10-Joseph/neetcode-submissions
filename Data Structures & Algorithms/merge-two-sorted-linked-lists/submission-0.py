# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode(0)
        dummy=dum
        curr1=list1
        curr2=list2
        while curr1 and curr2:
            if curr1.val<=curr2.val:
                nextNode1=curr1.next
                dummy.next=curr1
                dummy=dummy.next
                curr1=nextNode1
            else:
                nextNode2=curr2.next
                dummy.next=curr2
                dummy=dummy.next
                curr2=nextNode2
        if curr1:
            dummy.next=curr1
        else:
            dummy.next=curr2
        return dum.next
        