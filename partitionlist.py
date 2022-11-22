""" Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions. """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # make a before and after list
        # combine both lists at the end
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        curr = head

        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next

            curr = curr.next

        after.next = None
        # combine both lists
        before.next = after_head.next

        return before_head.next