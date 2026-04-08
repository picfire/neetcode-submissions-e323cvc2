# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, l1: ListNode,l2: ListNode):
        while l1 != None:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2

            if l1_next == None:
                break
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next

    def reverse(self, head: Optional[ListNode]) -> None:
        prev = None
        curr = head
        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return
        # head of first half
        l1 = head
        #head of second half
        slow = head
        #tail of second half
        fast = head
        #tail of first half
        prev = None

        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        l2 = self.reverse(slow)

        self.merge(l1, l2)
